# Some scripts to benchmark the performance

1. Ran CASP13 targets vs unrief90 (feb 2022) to get lists of putative
homologues, capped at 500 results
2. parse_blast_data.py - parse the uniref blasts in to a csv file (uniref_results_summary.csv)
3. parse_pfam_blast.py - parse the pfamA target blasts so we know which casp13 target is which (target_membership.csv)
4. calculate_accuracy.py - work out the accuracy in finding H-family members given blast
   cut offs.


## OBSOLETE
1. Ran CASP13 targets vs gene3d to Identify which H-family the belong to (top hit)
gene3d release is too old
2. parse_cath_blast.py - parse the gene3d target blasts so we know which casp13 target is which (target_membership.csv)3
3. calculate_result_md5.py - work out the MD5 sum of the hits in the uniprot data so we can marry them up with the gene4d memberships (uniref_md5sums.csv)
