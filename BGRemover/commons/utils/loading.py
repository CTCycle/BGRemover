import os
import cv2
import itertools


# inspect a folder to find all files with a valid extension
###############################################################################
def inspect_folder(path, extensions):
        
        '''        
        Inspect the folder at the given path and generate a list of file names with
        the given extensions.
        
        Keyword arguments:   
            path (str):        The path of the target folder.
            extensions (list): A list of target file extensions.
        
        Returns: 
            tuple: A tuple containing:
                - list of str: A list of files with the specified extensions.
                - int: The state of the folder (0 if files with the given extensions are found, 1 otherwise).
        
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
###############################################################################
class ImageOperations:
    
    
    #--------------------------------------------------------------------------
    def resize_same_AR(self, original_height, original_width, target_size, image):
        
        '''       
        Resizes an image while maintaining its aspect ratio (AR).
    
        Keyword arguments:   
            original_height (int): The original height of the image.
            original_width (int): The original width of the image.
            target_size (int): The desired size for the longer dimension of the resized image.
            image (array): The image to be resized.
    
        Returns: 
            array: The resized image with the same aspect ratio as the original image.
        
        '''
        # Calculate the aspect ratio of the image
        aspect_ratio = original_width / original_height        
        # Determine the new dimensions while maintaining the aspect ratio
        if original_height >= original_width:
            new_height = target_size
            new_width = int(target_size * aspect_ratio)
        else:
            new_width = target_size
            new_height = int(target_size / aspect_ratio)
        
        # Resize the image with opencv
        resized_image = cv2.resize(image, (new_width, new_height))

        return resized_image 
    
   
