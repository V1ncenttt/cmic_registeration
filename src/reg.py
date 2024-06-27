import numpy as np
import os 
#from util import suplementary_functions as sf
import nibabel as nib
import numpy as np
import scipy.ndimage as ndimage
from scipy.signal import correlate

def list_nii_gz_files(directory):
    nii_gz_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".nii.gz"):
                nii_gz_files.append(os.path.join(root, file))
    return nii_gz_files

nifti_dir = ''
niftyreg_dir = '/Applications/niftk-18.5.4/NiftyView.app/Contents/MacOS/'
scans_dir = '../data/nii_dataset/'
# Parameters for the registration
aff_par = ' -rigOnly -floLowThr -1000 -refLowThr -1000 -floUpThr 1000 -refUpThr 100  -pad -1000 '
dir_par = ' -lncc -ln 5 -lp 4 -vel -pad -1000 '


print(list_nii_gz_files(scans_dir))
'''
ct_image_path = nifti_dir + 'ct_image.nii.gz'
cbct_image_path = nifti_dir + 'cbct_image.nii.gz'
aff_path = nifti_dir + 'aff.txt'
cpp_path = nifti_dir + 'cpp.nii.gz'
res_aff_image_path = nifti_dir + 'res_aff.nii.gz'
res_dir_image_path = nifti_dir + 'res_dir.nii.gz'


# comand line to run the registrtastion script

affine_command = niftyreg_dir + 'reg_aladin -flo ' + ct_image_path + ' -ref ' + cbct_image_path + ' -res ' + res_aff_image_path + ' -aff ' + aff_path + aff_par
os.system(affine_command)

deformable_command = niftyreg_dir + 'reg_f3d -flo ' + ct_image_path + ' -ref ' + cbct_image_path + ' -res ' + res_dir_image_path + ' -aff ' + aff_path +  ' -cpp ' + cpp_path + dir_par
os.system(deformable_command)

print('Registration')

'''

print('Finito')