
#! /bin/bash/

# This bash script makes an assembly summary table
# for the target species genomes. Note, for eukaryotes
# there is only one 'representative' or 'reference' genome.
# Note that the script takes a list of species taxids as
# input (not subspecies).

# Run as make_summary_table.sh taxid_list.txt assembly_summary_genbank.txt outfile.txt

INFILE1=$1
INFILE2=$2
OUTFILE1=$3


# Find 'representative' genomes
>$OUTFILE1
while read p
do
	# Get line from assembly summary file
	awk -F '\t' -v txid="$p" '($7==txid) && (/representative genome/ || /reference genome/)' $INFILE2 >> $OUTFILE1
done < $INFILE1

