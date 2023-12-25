import os
import numpy as np
import cv2
import tensorflow as tf

# Intersection over Union
#------------------------------------------------------------------------------
def IoU(y_true, y_pred):
    
    '''
    Calculates the Intersection over Union (IoU) metric for two binary masks.
    
    Keyword arguments:         
        y_true (array): The true binary mask.
        y_pred (array): The predicted binary mask.
    
    Returns:         
        x (tf.tensor): tensor containing the IoU value
    
    '''  
    np.random.seed(42)
    tf.random.set_seed(42)
    
    def f(y_true, y_pred):
        intersection = (y_true * y_pred).sum()
        union = y_true.sum() + y_pred.sum() - intersection
        x = (intersection + 1e-15) / (union + 1e-15)
        x = x.astype(np.float32)
        return x
    return tf.numpy_function(f, [y_true, y_pred], tf.float32)

# Dice coefficient
#------------------------------------------------------------------------------
def dice_coef(y_true, y_pred):
    
    '''
    Calculates the Dice coefficient, a metric used to evaluate the similarity 
    of two sets of data, typically used for binary image segmentation.
   
    Keyword arguments: 
    
    y_true (tensor): A tensor representing the true labels.
    y_pred (tensor): A tensor representing the predicted labels.
    
    Returns:
    dice_coef (float): The Dice coefficient.
    
    '''
    np.random.seed(42)
    tf.random.set_seed(42)    
    smooth = 1e-15
    y_true = tf.keras.layers.Flatten()(y_true)
    y_pred = tf.keras.layers.Flatten()(y_pred)
    intersection = tf.reduce_sum(y_true * y_pred)
    reducer = (tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) + smooth)
    dice_coef = (2 * intersection + smooth)/reducer
    
    return dice_coef

# Dice loss
#------------------------------------------------------------------------------
def dice_loss(y_true, y_pred):
    
    '''
    Calculates the loss of the Dice function as 1 - Dice coefficient.
   
    Keyword arguments:     
        y_true (tensor): A tensor representing the true labels.
        y_pred (tensor): A tensor representing the predicted labels.
    
    Returns:        
        dice_loss (float): the Dice loss
    
    '''  
    np.random.seed(42)
    tf.random.set_seed(42)    
    dice_loss = 1.0 - dice_coef(y_true, y_pred)
    
    return dice_loss  
    
    
# [PATTERN RECOGNITION]
#==============================================================================
# Perform segmentation and pattern recognition operations
#==============================================================================
class PatternRecognition:
    
    #------------------------------------------------------------------------------
    def background_removal(self, images_path, savepath, model, pbar):

        '''
        Removes the background from a list of images using a given model.
    
        Keyword arguments:     
            self (object): The object instance.
            images_path (list): A list of paths to the images.
            savepath (str): The path where the images with removed backgrounds will be saved.
            model (object): The model used for background removal.
            pbar (object): A progress bar object.
        
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
            pbar.update(id + 1, max=len(images_path))            
        
        return final_pic       
    
  
     

