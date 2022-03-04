import csv
import hashlib

uniref_list = set()
with open('uniref_results_summary.csv') as fhTarg:
    csvreader = csv.reader(fhTarg, delimiter=",")
    next(csvreader)
    for entries in csvreader:
        uniref_list.add(entries[1])

uniref_list = list(uniref_list)
print("uniref,md5")

id = ''
seq = ''
with open('/home/dbuchan/Data/uniref/uniref90.fasta') as fhuniref:
    for line in fhuniref:
        if line.startswith(">"):
            if len(seq) > 0:
                if id in uniref_list:
                    md5 = hashlib.md5(seq.encode('utf-8')).hexdigest()
                    print(f'{id},{md5}')
                # print(id+"")
                # print(seq+"\n\n\n\n\n")
                seq = ''
                id = ''
                #exit()
            entries = line.split()
            id = entries[0][1:]
        else:
            seq += line.rstrip()
