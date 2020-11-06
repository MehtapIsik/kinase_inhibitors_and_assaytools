import json
import numpy as np
from glob import glob

inputs = {
    'xml_file_path' :  "./",
    'file_set'      :  {'p38' : glob( "./*.xml")},
    'section'       :  'em280', # '280_480_TOP_100'
    'wavelength'    :  '480',
    'ligand_order'  :  ['LOXO-101','LOXO-195','TPX0005','ONO5390556'],
    'Lstated'       :  np.array([20.0e-6,9.15e-6,4.18e-6,1.91e-6,0.875e-6,0.4e-6,0.183e-6,0.0837e-6,0.0383e-6,0.0175e-6,0.008e-6,0.0], np.float64),  # ligand concentration, M
    'Pstated'       :  0.5e-6 * np.ones([12],np.float64), # protein concentration, M
    'assay_volume'  :  100e-6, # assay volume, L
    'well_area'     :  0.3969, # well area, cm^2 for 4ti-0234
    }

inputs['Lstated'] = inputs['Lstated'].tolist()
inputs['Pstated'] = inputs['Pstated'].tolist()

with open('inputs.json', 'w') as fp:
    json.dump(inputs, fp)
