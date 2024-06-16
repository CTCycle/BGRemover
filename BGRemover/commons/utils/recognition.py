import os
import numpy as np
import cv2
    
    
# [PATTERN RECOGNITION]
#------------------------------------------------------------------------------
class PatternRecognition:
    
    #--------------------------------------------------------------------------
    def background_removal(self, images_path, savepath, model):

        '''
        Removes the background from a list of images using a given model.
    
        Keyword arguments:     
            self (object): The object instance.
            images_path (list): A list of paths to the images.
            savepath (str): The path where the images with removed backgrounds will be saved.
            model (object): The model used for background removal.            
        
        Returns:        
            final_pic (ndarray): The last picture processed with the background removed.

        '''
        BG_pictures = []
        for id, path in enumerate(images_path):
            pic_name = path.split('\\')[-1]
            image = cv2.imread(path, cv2.IMREAD_COLOR)
            height, width, _ = image.shape
            x = cv2.resize(image, (512, 512))
            x = x/255.0
            x = x.astype(np.float32)
            x = np.expand_dims(x, axis=0)
            y = model.predict(x)[0]
            y = cv2.resize(y, (width, height))
            y = np.expand_dims(y, axis=-1)
            y = y > 0.5     
            photo_mask = y
            background_mask = np.abs(1-y)        
            masked_photo = image * photo_mask
            background_mask = np.concatenate([background_mask, background_mask, background_mask], axis=-1)
            background_mask = background_mask * [255, 255, 255]
            final_pic = masked_photo + background_mask
            final_pic = np.squeeze(final_pic)   
            BG_pictures.append(final_pic)   
            pic_savepath = os.path.join(savepath, pic_name)                
            cv2.imwrite(pic_savepath, final_pic)                       
        
        return final_pic       
    
  
     

