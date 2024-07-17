import numpy as np
import tensorflow as tf


# [METRICS]
###############################################################################
class BGRMetrics:

    def __init__(self, seed):

        np.random.seed(seed)
        tf.random.set_seed(seed)

    #--------------------------------------------------------------------------
    def compute_IoU(self, y_true, y_pred):

        '''
        Computes the Intersection over Union (IoU) for two binary masks.

        Keyword arguments:
            y_true (array): The true binary mask.
            y_pred (array): The predicted binary mask.

        Returns:
            x (float): The IoU value as a float32.

        '''        
        intersection = (y_true * y_pred).sum()
        union = y_true.sum() + y_pred.sum() - intersection
        x = (intersection + 1e-15) / (union + 1e-15)
        x = x.astype(np.float32)

        return x


    # Intersection over Union
    #--------------------------------------------------------------------------
    def IoU(self, y_true, y_pred):
        
        '''
        Calculates the Intersection over Union (IoU) metric for two binary masks.
        
        Keyword arguments:         
            y_true (array): The true binary mask.
            y_pred (array): The predicted binary mask.
        
        Returns:         
            x (tf.tensor): tensor containing the IoU value
        
        '''        
        IoU_array = tf.numpy_function(self.compute_IoU, [y_true, y_pred], tf.float32)
            
        return IoU_array

    # Dice coefficient
    #--------------------------------------------------------------------------
    def dice_coef(self, y_true, y_pred):
        
        '''
        Calculates the Dice coefficient, a metric used to evaluate the similarity 
        of two sets of data, typically used for binary image segmentation.
    
        Keyword arguments: 
        
        y_true (tensor): A tensor representing the true labels.
        y_pred (tensor): A tensor representing the predicted labels.
        
        Returns:
        dice_coef (float): The Dice coefficient.
        
        '''       
        smooth = 1e-15       
        y_true = tf.keras.layers.Flatten()(y_true)
        y_pred = tf.keras.layers.Flatten()(y_pred)
        intersection = tf.reduce_sum(y_true * y_pred)
        reducer = (tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) + smooth)
        dice_coef = (2 * intersection + smooth)/reducer
        
        return dice_coef

    # Dice loss
    #--------------------------------------------------------------------------
    def dice_loss(self, y_true, y_pred):
        
        '''
        Calculates the loss of the Dice function as 1 - Dice coefficient.
    
        Keyword arguments:     
            y_true (tensor): A tensor representing the true labels.
            y_pred (tensor): A tensor representing the predicted labels.
        
        Returns:        
            dice_loss (float): the Dice loss
        
        '''              
        dice_loss = 1.0 - self.dice_coef(y_true, y_pred)
        
        return dice_loss  
        
        
