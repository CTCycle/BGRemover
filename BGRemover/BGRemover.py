import os
import gradio as gr
import tensorflow as tf
from keras.api._v2.keras.utils import CustomObjectScope

# [IMPORT CUSTOM MODULES]
from utils.loading import ImageOperations
from utils.metrics import IoU, dice_coef, dice_loss
from utils.recognition import PatternRecognition
from config.pathfinder import MODEL_DIR

# Define the background removal function
def remove_background(images, output_folder):
    
    model_path = os.path.join(MODEL_DIR, 'model.h5')
    
    with CustomObjectScope({'iou': IoU, 'dice_coef': dice_coef, 'dice_loss': dice_loss}):
        model = tf.keras.models.load_model(model_path)
        
    image_ops = ImageOperations()
    HPR = PatternRecognition()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    def process_image(image):
        image_path = image.name
        image_name = os.path.basename(image_path)
        output_image_path = os.path.join(output_folder, image_name)
        
        # Perform background removal
        processed_image = HPR.background_removal([image_path], output_folder, model)
        
        return output_image_path

    output_images = [process_image(image) for image in images]
    return output_images

# Gradio Interface
def gradio_app():
    with gr.Blocks() as demo:
        gr.Markdown("## Pre-trained DeepLabV3+ Model with Squeeze and Excitation Network for Human Image Segmentation")
        
        with gr.Row():
            with gr.Column():
                input_images = gr.File(label="Input Images", file_count="multiple", type="filepath")
                output_folder = gr.Textbox(label="Output Folder")
                remove_bg_button = gr.Button("Remove Background")
                
            with gr.Column():
                output_gallery = gr.Gallery(label="Processed Images", elem_id="gallery")
        
        remove_bg_button.click(remove_background,
            inputs=[input_images, output_folder],
            outputs=output_gallery)
    
    return demo

# Launch the Gradio app
demo = gradio_app()
demo.launch()