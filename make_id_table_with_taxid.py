# This script makes a taxon lokup table for
# the contigs in the multi-genome assembly
# fasta file. It takes the assembly summary
# file that was made while building the fasta
# and a fasta headers file as input. 

# This script is part of the snakemake
# pipeline: Snakefile_make_assm_db

# Run as:
# python make_id_table_with_taxid.py {input[0]} {input[1]} {output[0]}
# python make_id_table_with_taxid.py assembly_summary_target_species.txt seq_ids.txt taxon_table.csv

import csv
import sys

input0 = sys.argv[1]
input1 = sys.argv[2]
output = sys.argv[3]

# Get species and taxid from assembly summary file
# dic1{species:taxid}. Note only the first 2 strings
# in the species field are taken
dic1 = {}
fh1=open(input0,'r')
for l in fh1:
	line = l.strip().split('\t')
	genus = line[7].split(' ')[0]
	species = line[7].split(' ')[1]
	gs = str(genus + ' ' + species)
	dic1[gs] = int(line[6])

fh1.close()

# Get contig and species names from
# fasta header file. dic2{contig:species}
dic2 = {}
fh2=open(input1,'r')
for a in fh2:
	b = a.strip().strip(',').split(' ')
	species = str(b[1] + ' ' + b[2])
	contig = str(b[0])
	dic2[contig] = list()
	dic2[contig].append(species)

fh2.close()

# Add taxid to dictionary
for ctg,sp in dic2.items():
	for c,d in dic1.items():
		# Update if the species names match
		if sp[0] == c:
			dic2[ctg].append(d)

# Write contig,species, taxid to taxon 
# lookup table
w = csv.writer(open(output, "w"))
for key,value in dic2.items():
	ctg = str(key)
	sp = str(value[0])
	txid = int(value[1])
	w.writerow([ctg, sp, txid])

