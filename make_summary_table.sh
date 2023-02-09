#! /bin/bash/

# This bash script makes an assembly summary table
# for the target species genomes. Note, for eukaryotes
# there is only one 'representative' or 'reference' genome.

# Run as make_summary_table.sh species_list.txt assembly_summary_genbank.txt outfile.txt

INFILE1=$1
INFILE2=$2
OUTFILE1=$3


# Find 'representative' genomes
>$OUTFILE1
while read p
do
    # Grep line from assembly summary file
    grep -E "$p" $INFILE2 | grep "representative genome" >> $OUTFILE1
done < $INFILE1


# Find species with 'reference genome'
while read p
do
    # Grep line from assembly summary file
    grep -E "$p" $INFILE2 | grep "reference genome" >> $OUTFILE1
done < $INFILE1
