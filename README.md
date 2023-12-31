# BGRemover

## Project description
BGRemover is a python-based application to remove background from pictures. This app is inspired by the work of nikhilroxtomar (https://github.com/nikhilroxtomar/Remove-Photo-Background-using-TensorFlow), which makes use of the DeepLabV3+ model trained on the human image segmentation dataset. BGRemover includes a GUI (written using PySimpleGUI) that allows selecting a folder where the pictures are contained, as well as the output folder where you want to store pictures with removed background. Once you have loaded the pictures, just hit the "Remove background" button and wait for the magic to happen! The embedded progress bar will show the current progress of the operations. Pictures are kept with same size ratio of the original images! 

## DeepLabV3+ model
DeepLabv3+ is a semantic segmentation architecture that improves upon DeepLabv3 with several modifications. It was introduced by Chen et al. in 2018. The model employs atrous convolution in cascade or in parallel to capture multi-scale context by adopting multiple atrous rates. Furthermore, the Atrous Spatial Pyramid Pooling (ASPP) module from DeepLabv2 augmented with image-level features encoding global context and further boost performance. The changes to the ASPP module are that the authors apply global average pooling on the last feature map of the model, feed the resulting image-level features to a 1 × 1 convolution with 256 filters (and batch normalization), and then bilinearly upsample the feature to the desired spatial dimension. In the end, the improved ASPP consists of (a) one 1×1 convolution and three 3 × 3 convolutions with rates = (6, 12, 18) when output stride = 16 (all with 256 filters and batch normalization), and (b) the image-level features. _Remember that the pretrained DeepLabV3+ model works best on images of humans, and you results may vary when used with other subjects._

**Weights file (for the DeepLabV3+ model):** https://drive.google.com/file/d/17QKxSIBFhyJoDps93-sCVHnVV6UWS1sG/view

## How to use
Run the main python file (BGRemover.py) and use the GUI to navigate the various options. In the main window, you can select both the source folder where your pictures are located, and the output folder where you want to save your processed images. Then, you can use the **Load pictures** button to load all pictures within the selected input folder. Eventually, click on **Remove background** to process your pictures (check the progress bar to monitor current state of the operation).

### Requirements
This application has been developed and tested using the following dependencies (Python 3.10.12):

- `numpy==1.25.2`
- `opencv-python==4.8.0.76`
- `PySimpleGUI==4.60.5`
- `tensorflow==2.10.0`

These dependencies are specified in the provided `requirements.txt` file to ensure full compatibility with the application. As a very important note, remember to add the **pretrained weights** in modules/pretrained model, or else the software will throw an error!

## Graphic interface
Here you can find a snapshot of the main program GUI.
![Immagine](https://github.com/CTCycle/BGRemover/assets/101833494/4cda7251-da51-4cd2-aab9-67f10616b0c1)

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.




