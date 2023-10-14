# BGRemover

## Project description
BGRemover is a python-based application to remove background from pictures. This app is inspired by the work of nikhilroxtomar (https://github.com/nikhilroxtomar/Remove-Photo-Background-using-TensorFlow), which makes
use of the DeepLabV3+ model trained on the human image segmentation dataset. BGRemover includes a GUI (written using PySimpleGUI) that allows selecting a folder where the pictures are contained, as well as the output folder where you want to store pictures with removed background. Once you have loaded the pictures, just hit the "Remove background" button and wait for the magic to happen! The embedded progress bar will show the current progress of the operations. Pictures are kept with same size ratio of the original images! 

## DeepLabV3+ model
DeepLabv3+ is a semantic segmentation architecture that improves upon DeepLabv3 with several modifications. It was introduced by Chen et al. in 2018. The model employs atrous convolution in cascade or in parallel to capture multi-scale context by adopting multiple atrous rates. Furthermore, the Atrous Spatial Pyramid Pooling (ASPP) module from DeepLabv2 augmented with image-level features encoding global context and further boost performance. The changes to the ASPP module are that the authors apply global average pooling on the last feature map of the model, feed the resulting image-level features to a 1 × 1 convolution with 256 filters (and batch normalization), and then bilinearly upsample the feature to the desired spatial dimension. In the end, the improved ASPP consists of (a) one 1×1 convolution and three 3 × 3 convolutions with rates = (6, 12, 18) when output stride = 16 (all with 256 filters and batch normalization), and (b) the image-level features.

**Weight file (for the DeepLabV3+ model):** https://drive.google.com/file/d/17QKxSIBFhyJoDps93-sCVHnVV6UWS1sG/view
_Remember that the pretrained DeepLabV3+ model works best on images of humans, and you results may vary when used with other subjects._

## How to use
Run the main python file (BGRemover.py) and use the GUI to navigate the various options and process the pictures. Here you can find a snapshot of the main GUI. Select the input folder where you images are located, and an output folder to save the processed pictures. First click on Load images to preload all images from the input folder, then click on Remove background. The progress bar will show the current state of the operations!

### Requirements
Requirement.txt file is provided to ensure full compatibility with the python application. The application has been tested using Python 3.10.12 

### Program structure
The root folder of BGRemover contains different files and subfolders.



**Add the pretrained weights (model.h5) in modules/pretrained model, or else the software will throw an error!!!**


### Graphic interface

Here you can find a snapshot of the main program GUI.

![GUI_snapshot](https://github.com/CTCycle/BGRemover/assets/101833494/35c5a90e-20a5-4b60-af86-bcad99271452)


