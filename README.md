# BGRemover

## 1. Project Overview
BGRemover is a python-based application to remove background from pictures. This app is inspired by the work of nikhilroxtomar (https://github.com/nikhilroxtomar/Remove-Photo-Background-using-TensorFlow), which makes use of the DeepLabV3+ model trained on the human image segmentation dataset. BGRemover includes a GUI (written using PySimpleGUI) that allows selecting a folder where the pictures are contained, as well as the output folder where you want to store pictures with removed background. Once you have loaded the pictures, just hit the "Remove background" button and wait for the magic to happen! The embedded progress bar will show the current progress of the operations. Pictures are kept with same size ratio of the original images! 

## 2. DeepLabV3+ model
DeepLabv3+ is a semantic segmentation architecture that improves upon DeepLabv3 with several modifications. It was introduced by Chen et al. in 2018. The model employs atrous convolution in cascade or in parallel to capture multi-scale context by adopting multiple atrous rates. Furthermore, the Atrous Spatial Pyramid Pooling (ASPP) module from DeepLabv2 augmented with image-level features encoding global context and further boost performance. The changes to the ASPP module are that the authors apply global average pooling on the last feature map of the model, feed the resulting image-level features to a 1 × 1 convolution with 256 filters (and batch normalization), and then bilinearly upsample the feature to the desired spatial dimension. In the end, the improved ASPP consists of (a) one 1×1 convolution and three 3 × 3 convolutions with rates = (6, 12, 18) when output stride = 16 (all with 256 filters and batch normalization), and (b) the image-level features. _Remember that the pretrained DeepLabV3+ model works best on images of humans, and you results may vary when used with other subjects._

![DeepLabV3+ model architecture](./docs/snapshots/DeepLabV3_snapshot.png)

## 3. Installation 
The installation process on Windows has been designed for simplicity and ease of use. To begin, simply run `BGRemover.bat`. On its first execution, the installation procedure will automatically start with minimal user input required. The script will check if either Anaconda or Miniconda is installed on your system. If neither is found, you will need to install it manually. You can download and install Miniconda by following the instructions here: (https://docs.anaconda.com/miniconda/).

After setting up Anaconda/Miniconda, the installation script will install all the necessary Python dependencies. If you'd prefer to handle the installation process separately, you can run the standalone installer by executing `setup/BGRemover_installer.bat`. You can also use a custom python environment by modifying `settings/launcher_configurations.ini` and setting use_custom_environment as true, while specifying the name of your custom environment.

**Important:** After installation, if the project folder is moved or its path is changed, the application will no longer function correctly. To fix this, you can either:

- Open the main menu, select "BGRemover setup," and choose "Install project packages"
- Manually run the following commands in the terminal, ensuring the project folder is set as the current working directory (CWD):

    `conda activate BGRemover`

    `pip install -e . --use-pep517` 

## 4. How to use
On Windows, run `BGRemover.bat` to launch the GUI (alternatively, you can launch the main app file running `python BGRemover/commons/main.py`). In the main window, you can select both the source folder where your pictures are located, and the output folder where you want to save your processed images. Then, click on **Remove background** to process your pictures. 

### 4.1 Pretrained model weights 
Remember to add the pretrained weights in `BGRemover/commons/model` or the software won't function properly. 
**DeepLabV3+ model weights:** https://drive.google.com/file/d/17QKxSIBFhyJoDps93-sCVHnVV6UWS1sG/view

## 5. License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.




