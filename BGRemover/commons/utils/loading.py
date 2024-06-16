import os
import cv2
import itertools


def inspect_folder(path, extensions):
        
        '''        
        Inspect the folder at the given path and generates list of file names with
        a given extension (multiple extensions each time)
        
        Keyword arguments:   
            path (str):        path of the target folder (str)
            extensions (list): list of target file extension
        
        Returns: 
            list of target files with various extensions
        
        '''                
        all_files = os.listdir(path)
        multiext_files = []
        for ext in extensions:
            single_ext_files = [f for f in all_files if f.endswith(ext)]
            multiext_files.append(single_ext_files)
        ext_files = list(itertools.chain.from_iterable(multiext_files))
        if len(ext_files) > 0:
            folder_state = 0
        else:
            folder_state = 1
            
        return ext_files, folder_state


# [READING PICTURES]
#------------------------------------------------------------------------------
class ImageOperations:
    
    
    #--------------------------------------------------------------------------
    def resize_same_AR(self, original_height, original_width, target_size, image):
        
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
        # Calculate the aspect ratio
        aspect_ratio = original_width / original_height        
        # Determine the new dimensions while maintaining the aspect ratio
        if original_height >= original_width:
            new_height = target_size
            new_width = int(target_size * aspect_ratio)
        else:
            new_width = target_size
            new_height = int(target_size / aspect_ratio)
        
        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height))
        return resized_image 
    
   
