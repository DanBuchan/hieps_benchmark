from Bio.Blast import NCBIXML
import os
import glob

path = '/home/dbuchan/Projects/hieps/cath_blasts/'

def read_blast(id, path):
    file = f'{path}{id}/{id}.bls'
    if os.path.isfile(file):
        result_handle = open(file)
        blast_records = NCBIXML.parse(result_handle)
        record = next(blast_records)
        if len(record.alignments) > 0:
            first_alignment = record.alignments[0]
            entries = first_alignment.title.split("|")
            print(f'{id},{entries[3]}')

print("chain,h_family")
for dir in os.listdir(path):
    if os.path.isdir(path+dir):
        read_blast(dir, path)
