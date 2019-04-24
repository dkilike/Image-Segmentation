# Image Segmentation
### Work Log
- Thursday 25th April 2019 at 8:30 AM: Initiailize Project Image Segmentation
- Thursday 25th April 2019 at 8:35 AM: Record key words
- Thursday 25th April 2019 at 8:50 AM: study basic knowledges
- Thursday 25th April 2019 at 9:00 AM: set up PyCharm coding environment
- Thursday 25th April 2019 at 9:30 AM: practise pydicom to play with the given DICOM files

## Study Log
- Thursday 25th April 2019 at 8:50 AM: CT scan
  -motorized x-ray source
  -narrow beams of x-rays
  -rotating around the patient
  -image slice can be displayed individually in 2 dimensional form, or stacked together to generate a 3 dimensional image
- Thursday 25th April 2019 at 8:55 AM: DICOM
  -short for Digital Imaging and Communications in Medicine (where is the O?)
  -international standard to transmit, store, retrieve, print, process and display medical imaging information
  -just a data format is all need to know, so far
- Thursday 25th April 2019 at 9:00 AM: pydicom
  -A python package for working with DICOM files

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
