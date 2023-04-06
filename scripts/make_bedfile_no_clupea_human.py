# This script is used to make a bed file that will
# be used for filtering bam results. Here, we want
# to exclude alignments that map to human or Clupea
# harengus contigs (herring). So, the output of this
# script is a bed formatted file that includes all
# of the contigs in the original fasta except human
# and herring. The output is tab seperated with:
# contig, start (in this case 0) and end. This
# can be used with samtools view to filter bam files.

# Run as:
# python3 make_bedfile_no_clupea_human.py file.fasta to_include.bed


import sys
import csv
from Bio import SeqIO

infile=sys.argv[1]
outfile=sys.argv[2]


w = csv.writer(open(outfile, "w"), delimiter='\t')
for seq_record in SeqIO.parse(infile, "fasta"):
	desc = seq_record.description
	x = desc.find("Homo sapiens")
	y = desc.find("Clupea harengus")
	# Check if it is a human or herring sequence. If
	# not, add it to the output file.
	# (x=-1 if string is not found)
	if x ==int(-1) and y ==int(-1):
		w.writerow([seq_record.id,int(0),len(seq_record)])
