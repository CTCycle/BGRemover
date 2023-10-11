# BGRemover

A python-based application to remove background from pictures. This app is inspired by the work of nikhilroxtomar (https://github.com/nikhilroxtomar/Remove-Photo-Background-using-TensorFlow), which makes
use of the DeepLabV3+ model trained on the human image segmentation dataset. BGRemover includes a GUI (written using PySimpleGUI) that allows selecting a folder where the pictures are contained, 
as well as the output folder where you want to store pictures with removed background. Once you have loaded the pictures, just hit the "remove background" button and wait for the magic to happen! The embedded progress bar will show the current progress of the operations. Pictures are kept with same size ratio of the original images! 

_Remember that the pretrained DeepLabV3+ model works best on images of humans, and you results may vary when used with other subjects._

**Weight file (for the DeepLabV3+ model):** https://drive.google.com/file/d/17QKxSIBFhyJoDps93-sCVHnVV6UWS1sG/view

## Requirements

Requirement.txt file is provided to ensure full compatibility with the python application. The application has been tested using Python 3.10.12  

## How to use

Run the main python file (BGRemover.py) and use the GUI to navigate the various options and process the pictures. Here you can find a snapshot of the main GUI. Select the input folder where you images are located, and an output folder to save the processed pictures. First click on Load images to preload all images from the input folder, then click on Remove background. The progress bar will show the current state of the operations!

![GUI_snapshot](https://github.com/CTCycle/BGRemover/assets/101833494/35c5a90e-20a5-4b60-af86-bcad99271452)

**Add the pretrained weights (model.h5) in modules/pretrained model, or else the software will throw an error!!!**
