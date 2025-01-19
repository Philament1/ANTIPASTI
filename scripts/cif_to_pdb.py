import pymol2

import os
# assign directory
cif_dir = '/Users/pyu/Library/CloudStorage/OneDrive-ImperialCollegeLondon/Year 4/0 M4R/ANTIPASTI/af3/af_output/'
struc_dir = '../structures/'

# iterate over files in
# that directory
for protein_name in os.listdir(cif_dir):
    cifname = os.path.join(cif_dir, protein_name, protein_name+'_model.cif')
    if os.path.isfile(cifname):
        with pymol2.PyMOL() as pymol:
            pymol.cmd.load(cifname,'myprotein')
            pymol.cmd.save(os.path.join(struc_dir, protein_name+'_af3.pdb'), selection='myprotein')