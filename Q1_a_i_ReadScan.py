'''Please write a program to read the scan and print out
The maximum voxel intensity
The mean voxel intensity
The coordinates of the centre of the image volume, in the scanner coordinate system.
'''

import pydicom
import numpy as np
import matplotlib.pyplot as plt
import glob

# load the DICOM files
files = []
for fname in glob.glob(r'D:\One Drive Daily\OneDrive\CT scan Image Segmentation\Image-Segmentation\DICOM data\*', recursive=False):
    print("loading: {}".format(fname))
    files.append(pydicom.read_file(fname))
print("file count: {}".format(len(files)))

# skip files with no SliceLocation (eg scout views)
slices = []
skipcount = 0
for f in files:
    if hasattr(f, 'SliceLocation'):
        slices.append(f)
    else:
        skipcount = skipcount + 1
print("skipped, no SliceLocation: {}".format(skipcount))

# ensure they are in the correct order
slices = sorted(slices, key=lambda s: s.SliceLocation)

# create 3D array (assuming that each slice has the same pixel size)
img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
img3d = np.zeros(img_shape)

# fill 3D array with the images from the files
for i, s in enumerate(slices):
    img3d[:, :, i] = s.pixel_array

