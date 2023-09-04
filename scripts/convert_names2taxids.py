# This script takes a list of species as input. It
# outputs the species taxids as a list.


# Run as python
# python convert_names2taxids.py specieslist.txt taxids_out.txt

#############################################

import sys
from ete3 import NCBITaxa
ncbi = NCBITaxa()

# Add in update taxa row?
# ncbi.update_taxonomy_database()

# In/outfiles
sp_list_in = sys.argv[1]
txid_list_out = sys.argv[2]

# List for species from original list
# that have a taxid in the database.
in_species=list()
taxids=list()


fh1=open(sp_list_in,"r")
for line in fh1:
	x = line.strip()
	dic1 = ncbi.get_name_translator([x])
	l = dic1[x]
	# Add taxids to list
	taxids.append(l[0])
fh1.close()

# Write taxids to a list
with open(txid_list_out, 'w') as f:
	for t in taxids:
		f.write(f"{t}\n")




