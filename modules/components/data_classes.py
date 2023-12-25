import os
import cv2
import itertools


# [FOLDER INSPECTION]
#==============================================================================
# define the class for inspection of the input folder and generation of files list.
# The extension as argument allows identifying specific files (.csv, .xlsx, .pdf, etc)
# and making a list of those than can be called with the 'target_files' method
#==============================================================================
class FolderInspector:    
    
    
    #--------------------------------------------------------------------------
    def multiext_inspector(self, path, extensions):
        
        '''        
        Inspect the folder at the given path and generates list of file names with
        a given extension (multiple extensions each time)
        
        Keyword arguments:   
            path (str):        path of the target folder (str)
            extensions (list): list of target file extension
        
        Returns: 
            list of target files with various extensions
        
        '''
        os.chdir(path)
        self.all_files = os.listdir(path)
        self.multiext_files = []
        for ext in extensions:
            single_ext_files = [f for f in self.all_files if f.endswith(ext)]
            self.multiext_files.append(single_ext_files)
        self.ext_files = list(itertools.chain.from_iterable(self.multiext_files))
        if len(self.ext_files) > 0:
            self.empty_folder = False
        else:
            self.empty_folder = True
            
        return self.ext_files

# Reading pictures and operating with them
#==============================================================================
# Operations with images in different format
#==============================================================================
class ImageOperations:
    
    #--------------------------------------------------------------------------
    def resize_same_AR(self, H, W, target_size, picture):
        
        '''       
        Resizes an image while maintaining its aspect ratio (AR).
    
        Keyword arguments:   
            H (int):             The original height of the image
            W (int):             The original width of the image
            target_size (tuple): The desired size of the resized image
            picture (array):     The image to be resized
    
        Returns: 
            the resized image with the same aspect ratio as the original image
        
        '''
        if H > W:
            new_height = target_size
            new_width = int((new_height/H) * W)
        elif W > H:
            new_width = target_size
            new_height = int((new_width/W) * H)
        elif H == W:
            new_width, new_height = target_size, target_size        
        res_picture = cv2.resize(picture, (new_width, new_height))
        return res_picture 
    
   
