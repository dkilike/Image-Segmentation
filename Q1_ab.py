'''Please write a program to read the scan and print out
The maximum voxel intensity
The mean voxel intensity
The coordinates of the centre of the image volume, in the scanner coordinate system.
'''

import pydicom
import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
import os
import image_slicer

'''form a 3D array by stacking all CT scan slices'''
# load the DICOM files
src_path = r'C:\Users\GGPC\SegmentationTest\Image-Segmentation'
DICOM_dir_path = src_path + '\DICOM data'

# snapshot dicom file
files = []
for fname in glob.glob(DICOM_dir_path+'\*', recursive=False):
    print("loading: {}".format(fname))
    files.append(pydicom.read_file(fname))
print("file count: {}".format(len(files)))

# skip files with no SliceLocation
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

input("Press Enter to continue showing Question 1 (a) results...")
'''start solving Q1_a read and print'''
# first two questions are straight-forward
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

input("Press Enter to continue showing Question 1 (b) results...")
'''start solving Q1_b'''
# plot the maximum voxel intensity of each slice
MaxVoxelList=[]
MeanVoxelList=[]
for s in slices:
    MaxVoxelList.append(s.pixel_array.max())
    MeanVoxelList.append(s.pixel_array.mean())

print('Close plot to continue')
plt.scatter(range(0,len(MaxVoxelList)), MaxVoxelList)
plt.xlabel('slice index (1-200)')
plt.ylabel('maximum voxel intensity')
plt.title('Scatter of Max Voxel over Slice Index')
plt.show()

# selection voxel intensity threshold of 3000
Threshold = 3000

print('Close plot of an mask dection example to continue')
a1 = plt.subplot(2, 2, 1)
plt.imshow(img3d[:, :, 30])
a1 = plt.subplot(2, 2, 2)
plt.imshow(img3d[:, :, 30]>Threshold)
a1 = plt.subplot(2, 2, 3)
plt.imshow(img3d[:, :, 176])
a1 = plt.subplot(2, 2, 4)
plt.imshow(img3d[:, :, 176]>Threshold)
plt.show()


input("Press Enter to continue generating images and masks to Folders: SegmentationMask(metal mask) and Images(ct scan slices)...")
# generate images and masks
NameCount = 300
for s in slices:
    ImageName = '\SegmentationMask\IM00' + str(NameCount) + '.png'
    img = s.pixel_array>Threshold
    img = img.astype('uint8')*255
    cv2.imwrite(src_path + ImageName, img)
    print(ImageName + ' has been saved')
    NameCount+=1

NameCount = 300
for s in slices:
    ImageName = '\Images\IM00' + str(NameCount) + '.png'
    img = (s.pixel_array - img3d.min())/(img3d.max()-img3d.min())*255
    cv2.imwrite(src_path + ImageName, img)
    print(ImageName + ' has been saved')
    NameCount+=1

# NameCount = 300
# for s in slices:
#     ImageName = '\SegmentationBoneMask\IM00' + str(NameCount) + '.png'
#     img = s.pixel_array>0
#     img = img.astype('uint8')*255
#     cv2.imwrite(src_path + ImageName, img)
#     print(ImageName + ' has been saved')
#     NameCount+=1

# NameCount = 300
# for s in slices:
#     ImageName = '\Dataset_Slicer\masks\IM00' + str(NameCount) + '.png'
#     img = s.pixel_array>Threshold
#     img = img.astype('uint8')*255
#     cv2.imwrite(src_path + ImageName, img)
#     image_slicer.slice(src_path + ImageName,14)
#     os.remove(src_path + ImageName)
#     print(ImageName + ' has been saved')
#     NameCount+=1
#
# NameCount = 300
# for s in slices:
#     ImageName = '\Dataset_Slicer\images\IM00' + str(NameCount) + '.png'
#     img = (s.pixel_array - img3d.min())/(img3d.max()-img3d.min())*255
#     cv2.imwrite(src_path + ImageName, img)
#     image_slicer.slice(src_path + ImageName, 14)
#     os.remove(src_path + ImageName)
#     print(ImageName + ' has been saved')
#     NameCount+=1
#
# NameCount = 300
# for s in slices:
#     ImageName = '\Dataset_Slicer\masks\IM00' + str(NameCount) + '.png'
#     img = s.pixel_array>0
#     img = img.astype('uint8')*255
#     cv2.imwrite(src_path + ImageName, img)
#     print(ImageName + ' has been saved')
#     NameCount+=1

# os.mkdir(src_path + '\\Dataset')
# for fname in glob.glob(DICOM_dir_path + '\*', recursive=False):
#     os.mkdir(src_path + '\\Dataset' + fname[-8:])
#     os.mkdir(src_path + '\\Dataset' + fname[-8:] + '\\images')
#     os.mkdir(src_path + '\\Dataset' + fname[-8:] + '\\masks')
#
# NameCount = 300
# for s in slices:
#     ImageName = '\Dataset\IM00' + str(NameCount) + '\masks\MetalMask.png'
#     img = s.pixel_array>Threshold
#     img = img.astype('uint8')*255
#     cv2.imwrite(src_path + ImageName, img)
#     print(ImageName + ' has been saved')
#     NameCount+=1
#
# NameCount = 300
# for s in slices:
#     ImageName = '\Dataset\IM00' + str(NameCount) + '\images' + '\IM00' + str(NameCount) + '.png'
#     img = (s.pixel_array - img3d.min())/(img3d.max()-img3d.min())*255
#     cv2.imwrite(src_path + ImageName, img)
#     print(ImageName + ' has been saved')
#     NameCount+=1
#
# NameCount = 300
# for s in slices:
#     ImageName = '\Dataset\IM00' + str(NameCount) + '\masks\PositiveVoxelMask.png'
#     img = s.pixel_array>0
#     img = img.astype('uint8')*255
#     cv2.imwrite(src_path + ImageName, img)
#     print(ImageName + ' has been saved')
#     NameCount+=1