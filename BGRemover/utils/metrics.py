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
    
    
