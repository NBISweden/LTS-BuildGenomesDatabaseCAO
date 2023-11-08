# This script makes a taxon lokup table for
# the contigs in the multi-genome assembly
# fasta file. It takes the assembly summary
# file that was made while building the fasta
# and a fasta headers file as input. The updated
# 'v3' version of the script deals with a few 
# unusual contig headers in the human genome.
# It also adds the family level taxids to the 
# output file.

#The output file should have:
# contig name, species name, species taxid,family taxid

# This script is part of the snakemake
# pipeline: Snakefile_make_assm_db

# Run as:
# python make_id_table_with_taxid.py {input[0]} {input[1]} {output[0]}
# python make_id_table_with_taxid.py assembly_summary_target_species.txt seq_ids.txt taxon_table.csv

import csv
import sys
from ete3 import NCBITaxa
ncbi = NCBITaxa()
#ncbi.update_taxonomy_database()



input0 = sys.argv[1]
input1 = sys.argv[2]
output = sys.argv[3]

# Get species and taxid from assembly summary file
# dic1{species:taxid}. Note only the first 2 strings
# in the species field are taken. The taxid_list will 
# be used to lookup the family level taxids using
# the species taxids in the next step

dic1 = {}
taxid_list = []
fh1=open(input0,'r')
for l in fh1:
	line = l.strip().split('\t')
	genus = line[7].split(' ')[0]
	species = line[7].split(' ')[1]
	gs = str(genus + ' ' + species)
	tx = int(line[6]) 
	dic1[gs] = tx
	taxid_list.append(tx)

fh1.close()

##########################################
# Go through each of the species taxids on
# the list and lookup the family
# taxon_dic{species taxid : family taxid}

taxid_dic = {}
for i in taxid_list:
	lineage = ncbi.get_lineage(i)
	rankings = ncbi.get_rank(lineage)
	for x,y in rankings.items():
		if y == 'family':
			taxid_dic[i] = x


########################################

# Get contig and species names from
## fasta header file. dic2{contig:species}
dic2 = {}
fh2=open(input1,'r')
for a in fh2:
	b = a.strip().strip(',').split(' ')
	# This deals with a few of the human contigs
	# that have 'UNVERIFIED_ORG:' in their header
	if b[1] == 'UNVERIFIED_ORG:':
		species = str(b[2] + ' ' + b[3])
		contig = str(b[0])
		dic2[contig] = list()
		dic2[contig].append(species)
	# This works for the rest of the contig headers
	elif b[1] != 'UNVERIFIED_ORG:':
		species = str(b[1] + ' ' + b[2])
		contig = str(b[0])
		dic2[contig] = list()
		dic2[contig].append(species)

fh2.close()
# Add species taxid to dictionary
for ctg,sp in dic2.items():
	for c,d in dic1.items():
		# Update if the species names match
		if sp[0] == c:
			dic2[ctg].append(d)

# Add family taxid to the dictionary
for ctg,sp in dic2.items():
	for e,f in taxid_dic.items():
		if sp[1] == e:
			dic2[ctg].append(f)


# Update below to include family level taxid too.
# Write contig,species, species taxid, family taxid
# to taxon lookup table
w = csv.writer(open(output, "w"))
for key,value in dic2.items():
	ctg = str(key)
	sp = str(value[0])
	txid = int(value[1])
	ftxid = int(value[2])
	w.writerow([ctg, sp, txid,ftxid])

