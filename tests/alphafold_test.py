import numpy as np
import os
import pytest
import torch
import unittest

# ANTIPASTI
from antipasti.preprocessing.preprocessing import Preprocessing
from antipasti.utils.torch_utils import load_checkpoint
from tests import TEST_PATH

class TestTraining(unittest.TestCase):
    def setUp(self):
        self.path = TEST_PATH
        self.modes = 'all'
        self.n_filters = 4
        self.filter_size = 4
        self.pooling_size = 1
        self.n_max_epochs = 935

        self.pathological = ['5omm', '5i5k', '1uwx', '1mj7', '1qfw', '1qyg', '4ffz', '3ifl', '3lrh', '3pp4', '3ru8', '3t0w', '3t0x', '4fqr', '4gxu', '4jfx', '4k3h', '4jfz', '4jg0', '4jg1', '4jn2', '4o4y', '4qxt', '4r3s', '4w6y', '4w6y', '5ies', '5ivn', '5j57', '5kvd', '5kzp', '5mes', '5nmv', '5sy8', '5t29', '5t5b', '5vag', '3etb', '3gkz', '3uze', '3uzq', '4f9l', '4gqp', '4r2g', '5c6t', '3fku', '1oau', '1oay'] + ['4gqp', '3etb', '3gkz', '3uze', '3uzq', '3gm0', '4f9l', '6ejg', '6ejm', '1h8s', '5dfw', '6cbp', '4f9p', '5kov', '1dzb', '5j74', '5aaw', '3uzv', '5aam', '3ux9', '5a2j', '5a2k', '5a2i', '3fku', '5yy4', '3uyp', '5jyl', '1y0l', '1p4b', '3kdm', '4lar', '4ffy', '2ybr', '1mfa', '5xj3', '5xj4', '4kv5', '5vyf'] 
        self.stage = 'predicting'
        self.dccm_map_path = 'dccm_maps_full_ags_all/'
        self.test_data_path = os.path.join('notebooks/', 'test_data/')
        self.test_dccm_map_path = 'dccm_map/'
        self.test_residues_path = 'list_of_residues/'
        self.test_structure_path = 'structure/'

        self.test_pdbs = ['2r56', '4f3f']
        self.h_offset_list = [0, 0]
        self.l_offset_list = [0, 0]
        self.af_pred_structures = []
    
    def test_alphafold(self):

        for test_pdb, h_offset, l_offset in zip(self.test_pdbs, self.h_offset_list, self.l_offset_list):
            preprocessed_data = Preprocessing(data_path='data/', dccm_map_path=self.dccm_map_path, modes=self.modes, pathological=self.pathological, stage=self.stage, test_data_path=self.test_data_path, test_dccm_map_path=self.test_dccm_map_path, test_residues_path=self.test_residues_path, test_structure_path=self.test_structure_path, test_pdb_id=test_pdb+'_af', alphafold=True, h_offset=h_offset, l_offset=l_offset, renew_maps=False, renew_residues=True)            
            self.af_pred_structures.append(preprocessed_data.test_x)
            input_shape = preprocessed_data.test_x.shape[-1]
        
        path = 'checkpoints/full_ags_all_modes/model_epochs_' + str(self.n_max_epochs) + '_modes_' + str(self.modes) + '_pool_' + str(self.pooling_size) + '_filters_' + str(self.n_filters) + '_size_' + str(self.filter_size) + '.pt'
        model = load_checkpoint(path, input_shape)[0]
        model.eval()

        kds_af_pred = [model(torch.from_numpy(test_arr.reshape(1, 1, input_shape, input_shape).astype(np.float32)))[0].detach().numpy()[0,0] for test_arr in self.af_pred_structures]