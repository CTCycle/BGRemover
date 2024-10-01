import os
import gradio as gr
import tensorflow as tf
from keras.api._v2.keras.utils import CustomObjectScope

# [IMPORT CUSTOM MODULES]
from BGRemover.commons.utils.metrics import BGRMetrics
from BGRemover.commons.utils.recognition import background_removal
from BGRemover.commons.constants import MODEL_PATH
from BGRemover.commons.logger import logger


# [MAIN FUNCTION]
###############################################################################
def main_background_remover(images, output_folder):

    metrics = BGRMetrics(seed=42)   
    with CustomObjectScope({'iou': metrics.IoU, 'dice_coef': metrics.dice_coef, 'dice_loss': metrics.dice_loss}):
        model = tf.keras.models.load_model(MODEL_PATH)
        logger.debug(f'Loaded model from {MODEL_PATH}')         
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    def process_image(image):
        image_path = image.name
        image_name = os.path.basename(image_path)
        output_image_path = os.path.join(output_folder, image_name)
        
        # Perform background removal
        processed_image = background_removal([image_path], output_folder, model)
        
        return output_image_path

    output_images = [process_image(image) for image in images]
    return output_images

# [INTERFACE]
###############################################################################
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
        
        remove_bg_button.click(main_background_remover,
                               inputs=[input_images, output_folder],
                               outputs=output_gallery)
    
    return demo

# [RUN APP]
###############################################################################
demo = gradio_app()
demo.launch()