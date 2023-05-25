# LTS-BuildGenomesDatabaseCAO

This repository contains code used in the longterm support project P_Snoeijs-Leijonmalm_2205.

## Description

This repository contains a Snakemake (v7.18.2) pipeline used for building a genomes database and Bowtie2 indexes. The pipeline takes a species list as input. It downloads the latest assembly summary table from GenBank and searches for the species on the list. If multiple assemblies are available for a species, the representative (or reference) genome is downloaded. The pipeline also outputs a summary table of the downloaded genomes. The genomes are downloaded and merged into a single fasta file before Bowtie2 indexes are made. The time and amount of RAM required for building the indexes depends in part on the size and number of genomes included. A fat node (256GB on Rackham or 512GB on Snowy) may be required for this step. 

The pipeline was written for use in the NBIS longterm support project P_Snoeijs-Leijonmalm_2205. In this project, DNA reads from enviromental samples are mapped to the genomes assembly database. The current pipeline therefore outputs two additional files that are used in a main pipeline which can be found here: https://github.com/NBISweden/LTS-BiodiversityAnalysisCAO. A full description of the output files can be found below.

## Usage
The pipeline takes a species list as input. Each species should be on a single line and should be spelled correctly. It is important that **no empty lines** are included in the file. If there are multiple possible spellings or names for a given species, feel free to add the alternatives to the list.

## Output files
The pipeline builds and outputs **Bowtie2 index files** for multiple genome assemblies. There pipeline also outputs a few other files that can be used downstream for filtering/parsing alignments or results. These include a list of sequence headers from the genomes included in the database.

The sequence id list is called **seq_id.txt** and looks like this:
```
CAMRHF010002182.1 Pusa hispida saimensis genome assembly, contig: 2181, whole genome shotgun sequence
CM000663.2 Homo sapiens chromosome 1, GRCh38 reference primary assembly
```

The pipeline outputs a table with taxon and species information for each sequence in the database. This file contains the contig id, species and taxon id for each sequence in the database. This file can be used in downstream processes for filtering based on species or taxon id. It is needed

The **taxon_table.csv** file looks like this: 
```
KI270707.1,Homo sapiens,9606
JAOSYZ010000001.1,Gadus macrocephalus,80720
CAMRHF010002158.1,Pusa hispida,9718
```

The pipeline also outputs a bed formatted file that can be used downstream for filtering alignments from sam/bam files. The bed file includes all of the contigs that are of interest for futher analysis. In this case, human and herring assembly contigs are included in the database so that reads originating from these species do not map elsewhere. But, human and herring contigs are excluded from the bed file (and downstream analysis) because they are not of interest.

The **to_include.bed** file looks like this:
```
KB228878.1	0	17703537
KB228879.1	0	17817800
KB228880.1	0	9835568
```

## Other
- Contigs less than 2000 base pairs are excluded from the database
- The **taxon_table.csv** and **to_include.bed** files are needed for the main pipeline (https://github.com/NBISweden/LTS-BiodiversityAnalysisCAO) 
