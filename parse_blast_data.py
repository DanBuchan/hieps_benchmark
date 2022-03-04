from Bio.Blast import NCBIXML
import os
from collections import defaultdict

path = '/home/dbuchan/Projects/hieps/uniref_blasts/'
md5_map = '/home/dbuchan/Projects/hieps/data/uniref_md5sums.csv'


def read_blast(id, path, results):
    file = f'{path}{id}/{id}.bls'

    if os.path.isfile(file):
        result_handle = open(file)
        blast_records = NCBIXML.parse(result_handle)
        record = next(blast_records)
        if len(record.alignments) > 0:
            for alignment in record.alignments:
                entries = alignment.title.split("|")
                for hsp in alignment.hsps:
                    desc = entries[2].split()
                    aligned_count = len(hsp.query)-hsp.sbjct.count('-')
                    data = {desc[1]: {
                            'evalue': hsp.expect,
                            'score': hsp.score,
                            'aligned_percentage': aligned_count/len(hsp.query),
                            'percentage_identity': hsp.identities/len(hsp.query)
                            }}
                    results[id].append(data)
    return(results)

results = defaultdict(list)
for dir in os.listdir(path):
    if os.path.isdir(path+dir):
        results = read_blast(dir, path, results)

md5_lookup = {}
with open(md5_map) as fhmd5:
    next(fhmd5)
    for line in fhmd5:
        entries = line.rstrip().split(",")
        md5_lookup[entries[0]] = entries[1]

print('target,uniref,md5,evalue,score,aligned_percentage,percentage_identity')
for target in results:
    for result in results[target]:
        for uniref in result:
            md5 = ''
            if uniref in md5_lookup:
                md5=md5_lookup[uniref]

            print(f'{target},{uniref},{md5},'
                  f'{result[uniref]["evalue"]},'
                  f'{result[uniref]["score"]},'
                  f'{result[uniref]["aligned_percentage"]},'
                  f'{result[uniref]["percentage_identity"]}')
