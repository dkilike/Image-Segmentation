# Image Segmentation
### Work Log
- Thursday 25th April 2019 at 08:30 AM: Initiailize Project Image Segmentation
- Thursday 25th April 2019 at 08:35 AM: Record key words
- Thursday 25th April 2019 at 08:50 AM: study basic knowledges
- Thursday 25th April 2019 at 09:00 AM: set up PyCharm coding environment
- Thursday 25th April 2019 at 09:30 AM: practise pydicom to play with the given DICOM files
- Thursday 25th April 2019 at 09:50 AM: download MicroDicom viewer to checkout the given DICOM files
- Thursday 25th April 2019 at 10:00 AM: start to do Question 1(a)
- Thursday 25th April 2019 at 10:45 AM: end morning session

## Study Log
- Thursday 25th April 2019 at 08:50 AM: CT scan
  - motorized x-ray source
  - narrow beams of x-rays
  - rotating around the patient
  - image slice can be displayed individually in 2 dimensional form, or stacked together to generate a 3 dimensional image
- Thursday 25th April 2019 at 08:55 AM: DICOM
  - short for Digital Imaging and Communications in Medicine (where is the O?)
  - international standard to transmit, store, retrieve, print, process and display medical imaging information
  - just a data format is all need to know, so far
- Thursday 25th April 2019 at 09:00 AM: pydicom
  - A python package for working with DICOM files
- Thursday 25th April 2019 at 10:00 AM: maximum voxel intensity
  - voxel is 'volume' and 'pixel' and represents a value on a regular grid in three dimensional space
  - '3D pixels'
  - voxel intensity is the number, which represents the extent to which x-rays are attenuated when they pass through it.
  - example one: bone. Voxel will be a high number as bone tends to attenuate x-rays (may not let x-rays through at all)
  - example two: skin. Voxel will be a low number as skin does not hinder the x-rays penetration.
  

### Key Words
- CT scan
- DICOM format
- Each slice of CT scan in DICOM format can be stacked to form a 3D image
- DICOM file contains metadata, i.e. image size, image position and size relative to the CT scanner, and scanner settings
- DICOM viewer
- The maximum voxel intensity
- The mean voxel intensity
- The coordinates of the centre of the image volume, in the scanner coordinate system

### Steps
- Read scan and print out 
  - the maximum voxel intensity
  - the mean voxel intensity
  - the coordinates of the centre of the image volume, in the scanner coordinate system
- Segment the metal objects (generate labels)
  - treat all metal objects in a CT scan as ONE object
  - one segmentation for each slice of CT scan
  - binary images files
- train a Image Segmentation neural network
  - metric to quantify the error

### Hint
- In each slice, the spacing between pixels is 0.97 mm x 0.97 mm
- The distance between each slice is 1.6 mm
- Use DICOM header to help you calculate coordinates
- pydicom package

### Required Packages
- pydicom
- numpy
- matplotlib
