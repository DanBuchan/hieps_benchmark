import csv
from collections import defaultdict

targets = {}
pfam_list = {}
with open('data/target_membership.csv') as fhTarg:
    csvreader = csv.reader(fhTarg, delimiter=",")
    next(csvreader)
    for line in csvreader:
        targets[line[0]] = line[1]
        pfam_list[line[1]] = set()

uniref_hits = defaultdict(list)
with open('data/uniref_results_summary.csv') as fhuni:
    summaryreader = csv.reader(fhuni, delimiter=",")
    next(summaryreader)
    for entries in summaryreader:
        entries[1] = entries[1].replace('UniRef90_','')
        uniref_hits[entries[0]].append(entries[1:])

pfamAFasta = "/home/dbuchan/Data/pfam/Pfam-A.fasta"
with open(pfamAFasta) as fhPF:
    for line in fhPF:
        if line.startswith(">"):
            line = line.rstrip("|\n")
            entries = line.split()
            entries[0] = entries[0].lstrip(">")
            entries[0] = entries[0][:entries[0].find("_")]
            idinfo = entries[2].split(';')
            idinfo[0] = idinfo[0][:idinfo[0].find(".")]
            if idinfo[0] in pfam_list:
                pfam_list[idinfo[0]].add(entries[0])

# print("id,Pfamfamily,evalue,hit_count,family_count,true_positives,"
#       "sensitivity,precision")

def print_performances(comparison_column, value, fh):
    total = 0
    sensitivity_total = 0
    precision_total = 0
    for hitid in uniref_hits:
        total += 1
        pfam_family = ''
        if hitid in targets:
            pfam_family = targets[hitid]
        else:
            continue
        hit_set = set()
        for hit_data in uniref_hits[hitid]:
            if float(hit_data[comparison_column]) <= value:
                hit_set.add(hit_data[0])
        positives = len(pfam_list[pfam_family])
        true_pos = len(hit_set & pfam_list[pfam_family])
        false_pos = len(hit_set) - true_pos
        try:
            sensitivity_total += true_pos/positives
        except Exception:
            sensitivity_total += 0
        try:
            precision_total += true_pos/(true_pos+false_pos)
        except Exception:
            precision_total += 0
        # print(id, pfam_family, e_value, len(hit_set), positives, true_pos,
        #       sensitivity, precision)
    fh.write(f'{value},{sensitivity_total/total},{precision_total/total}\n')

fhOut = open("evalue_performance.csv", "w")
fhOut.write("evalue,average_sensitivity,average_precision\n")
base = 5
scale = 1
for step in range(0, 40):
    scale = scale/10
    value = base * scale
    print_performances(2, value, fhOut)
fhOut.close()

fhOut = open("identity_performance.csv", "w")
fhOut.write("percentage_identity,average_sensitivity,average_precision\n")
for step in range(1, 11):
    print_performances(5, step/10, fhOut)
fhOut.close()
