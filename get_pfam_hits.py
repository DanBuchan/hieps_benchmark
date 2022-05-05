from Bio.Blast import NCBIXML
import os
import glob

path = '/home/dbuchan/Projects/hieps/pfam_blasts/'

def read_blast(id, path, hit_set):
    file = f'{path}{id}/{id}.bls'
    if os.path.isfile(file):
        result_handle = open(file)
        blast_records = NCBIXML.parse(result_handle)
        record = next(blast_records)
        if len(record.alignments) > 0:
            for alignment in record.alignments:
                entries = alignment.title.split()
                hit_set.add(entries[1])
#            idinfo = entries[3].split(';')
#            print(f'{id},{idinfo[0][:idinfo[0].find(".")]}'
    return hit_set

uniref_set = set()
for dir in os.listdir(path):
    if os.path.isdir(path+dir):
        uniref_set = read_blast(dir, path, uniref_set)

for entry in uniref_set:
    halves = entry.split("/")
    print(halves[0][:halves[0].find("_")])
