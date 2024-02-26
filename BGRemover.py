import os
import PySimpleGUI as sg
import tensorflow as tf
import threading
from keras.api._v2.keras.utils import CustomObjectScope

# set warnings
#------------------------------------------------------------------------------
import warnings
warnings.simplefilter(action='ignore', category = Warning)

# import modules and classes
#------------------------------------------------------------------------------    
from modules.components.data_assets import FolderInspector, ImageOperations
from modules.components.model_assets import PatternRecognition, IoU, dice_coef, dice_loss

# default folder path
#------------------------------------------------------------------------------
initial_folder = os.path.dirname(os.path.realpath(__file__))

# [WINDOW THEME AND OPTIONS]
#==============================================================================
sg.theme('LightGrey1')
sg.set_options(font = ('Arial', 11), element_padding = (6,6))
images_path = []

# [LAYOUT OF THE SELECTION FRAME]
#==============================================================================
input_path_text = sg.Text('Input folder:', font = ('Arial', 12), size = (10, 1))
input_path = sg.Input(key= '-PATHINPUT-', size = (70, 1), enable_events=True)
input_browser = sg.FolderBrowse(initial_folder = initial_folder, key = '-INBROWSER-')
output_path_text = sg.Text('Output folder:', font = ('Arial', 12), size = (10, 1))
output_path = sg.Input(key= '-PATHOUTPUT-', size = (70, 1))
output_browser = sg.FolderBrowse(initial_folder = initial_folder, key = '-OUTBROWSER-')
output_text = sg.Text('No selected folder, waiting for user input...', key = '-OUTEXT-', font = ('Arial', 12), size = (40, 1))
path_frame = sg.Frame('Select folder paths', layout = [[input_path_text, input_path, input_browser],
                                                       [output_path_text, output_path, output_browser],
                                                       [output_text]],
                                                        expand_x=True)

# [LAYOUT OF THE BOTTOM FRAME]
#==============================================================================
load_button = sg.Button('Load pictures', key = '-LOAD-', disabled=True, expand_x=True)
remove_background_button = sg.Button('Remove background', key = '-REMOVEBG-', disabled=True, expand_x=True)
console_frame = sg.Frame('Operations', layout = [[load_button], [remove_background_button]], expand_x = True)

# [LAYOUT OF THE WINDOW]
#==============================================================================
main_text = sg.Text('Pre-trained DeepLabV3+ model with squeeze and excitation network for human image segmentation', 
                    font = ('Arial', 12), expand_x=True, auto_size_text = True)
progress_bar = sg.ProgressBar(100, orientation='h', size = (50, 20), expand_x=True, key='-PROGRESS-')
main_layout = [[main_text],
               [sg.VSeparator()],
               [path_frame],
               [console_frame],
               [progress_bar]]

# [WINDOW LOOP]
#==============================================================================
main_window = sg.Window('Background remover V1.0', main_layout, 
                        grab_anywhere = True, finalize = True)
while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        break 
    if event == '-PATHINPUT-':
        if values['-PATHINPUT-'] != '':
            main_window['-LOAD-'].update(disabled = False) 
        else:
            main_window['-LOAD-'].update(disabled = True)
            
             
    # [LOAD PICTURES FROM INPUT PATH FOLDER]
    #==========================================================================
    if event == '-LOAD-':
        origin_folder = values['-PATHINPUT-']
        output_folder = values['-PATHOUTPUT-']               
        picture_parsing = FolderInspector()
        list_of_extensions = ['.jpg', '.png', '.tiff']
        images_list = picture_parsing.multiext_inspector(origin_folder, list_of_extensions)
        images_path = [os.path.join(origin_folder, x) for x in images_list]
        num_of_images = len(images_list)
        if picture_parsing.empty_folder == True:
            main_window['-OUTEXT-'].update('The selected folder does not contain pictures!')
        else:
            main_window['-OUTEXT-'].update('{} pictures found in the selected folder'.format(num_of_images))
            if values['-PATHINPUT-'] != '':         
                main_window['-REMOVEBG-'].update(disabled=False)
    
    # [REMOVE BACKGROUND FROM PICTURES]
    #==========================================================================
    if event == '-REMOVEBG-':        
        modules_path = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(modules_path, 'modules', 'pretrained model', 'model.h5')
        with CustomObjectScope({'iou': IoU, 'dice_coef': dice_coef, 'dice_loss': dice_loss}):
            model = tf.keras.models.load_model(model_path)
        ImageOperationserations = ImageOperations()
        HPR = PatternRecognition()        
        BG_thread = threading.Thread(target = HPR.background_removal, args = (images_path, output_folder, model, progress_bar))                                               
        BG_thread.start()        
        
                

