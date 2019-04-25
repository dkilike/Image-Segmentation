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
DICOM_dir_path = r'D:\One Drive Daily\OneDrive\CT scan Image Segmentation\Image-Segmentation\DICOM data'
files = []
for fname in glob.glob(DICOM_dir_path+'\*', recursive=False):
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

print()
print('Question 1 (a)')
print('i.   The maximum voxel intensity is {}'.format(img3d.max()))
print('ii.  The mean voxel intensity is {}'.format(img3d.mean()))

# centre of the image volume is at (256.5,256.5) pixel position between the 100th and 101st slices
ImagePlanePosition_of_100th_slice = np.array(slices[99].ImagePositionPatient)
RowChangeInX_of_100th_slice = np.array(slices[99].ImageOrientationPatient[0:3]) * slices[99].PixelSpacing[0] * 256.5
ColumnChangeInY_of_100th_slice = np.array(slices[99].ImageOrientationPatient[3:6]) * slices[99].PixelSpacing[1] * 256.5
coordinate_of_100th_slice = ImagePlanePosition_of_100th_slice + RowChangeInX_of_100th_slice + ColumnChangeInY_of_100th_slice

ImagePlanePosition_of_101th_slice = np.array(slices[100].ImagePositionPatient)
RowChangeInX_of_101th_slice = np.array(slices[100].ImageOrientationPatient[0:3]) * slices[100].PixelSpacing[0] * 256.5
ColumnChangeInY_of_101th_slice = np.array(slices[100].ImageOrientationPatient[3:6]) * slices[100].PixelSpacing[1] * 256.5
coordinate_of_101th_slice = ImagePlanePosition_of_101th_slice + RowChangeInX_of_101th_slice + ColumnChangeInY_of_101th_slice

coordinate_of_ImageVolumeCentre = (coordinate_of_100th_slice+coordinate_of_101th_slice)/2

print('iii. coordinates of the centre of the image volume is {} mm'.format(list(coordinate_of_ImageVolumeCentre)))