# LTS-BuildGenomesDatabaseCAO

This repository contains code used in the longterm support project P_Snoeijs-Leijonmalm_2205.

## Description

This repository contains a Snakemake pipeline used for building a genomes database and Bowtie2 indexes. The pipeline takes a species list as input. It downloads the latest assembly summary table from GenBank and searches for the species on the list. If multiple assemblies are available for a species, the representative (or reference) genome is downloaded. The pipeline also outputs a summary table of the downloaded genomes. The genomes are downloaded and merged into a single fasta file before Bowtie2 indexes are made. The time and amount of RAM required for building the indexes depends in part on the size and number of genomes included. A fat node (256GB on Rackham or 512GB on Snowy) may be required for this step. 

The pipeline was written for use in the longterm support project P_Snoeijs-Leijonmalm_2205. In this project, DNA reads from enviromental samples are mapped to the genomes assembly database. The current pipeline therefore outputs two other files that are used in a main pipeline which can be found [here](https://github.com/NBISweden/LTS-BiodiversityAnalysisCAO). A full description of the output files can be found below.

## Usage
The pipeline takes a species list as input. Each species should be on a single line and should be spelled correctly. It is important that no empty lines are included in the file. 
