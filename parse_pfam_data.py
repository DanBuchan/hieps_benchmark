from Bio.Blast import NCBIXML
import os
import glob

path = '/home/dbuchan/Projects/hieps/pfam_blasts/'

def read_blast(id, path):
    file = f'{path}{id}/{id}.bls'
    if os.path.isfile(file):
        result_handle = open(file)
        blast_records = NCBIXML.parse(result_handle)
        record = next(blast_records)
        if len(record.alignments) > 0:
            first_alignment = record.alignments[0]
            entries = first_alignment.title.split()
            idinfo = entries[3].split(';')
            print(f'{id},{idinfo[0][:idinfo[0].find(".")]}')

print("chain,pfam_family")
for dir in os.listdir(path):
    if os.path.isdir(path+dir):
        read_blast(dir, path)
