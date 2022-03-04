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

print("id,Pfamfamily,evalue,hit_count,family_count,intersection_count")
e_value = 5
for id in uniref_hits:
    pfam_family = ''
    if id in targets:
        pfam_family = targets[id]
    else:
        continue
    hit_set = set()
    for hit_data in uniref_hits[id]:
        if float(hit_data[2]) <= e_value:
            hit_set.add(hit_data[0])
    print(id, pfam_family, e_value, len(hit_set), len(pfam_list[pfam_family]),
          len(hit_set & pfam_list[pfam_family]))
