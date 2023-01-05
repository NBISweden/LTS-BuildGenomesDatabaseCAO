
#! /bin/bash/

# This bash script makes an assembly summary table
# for the target species genomes.

# Run as make_summary_table.sh species_list.txt assembly_summary_genbank.txt outfile.txt

INFILE1=$1
INFILE2=$2
OUTFILE1=$3


>$OUTFILE1
while read p
do
    # Grep line from assembly summary file
    grep -E "$p" $INFILE2 | grep "representative genome" >> $OUTFILE1
done < $INFILE1

