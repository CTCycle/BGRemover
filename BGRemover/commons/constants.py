from os.path import join, dirname, abspath 

# [PATHS]
###############################################################################
PROJECT_DIR = dirname(dirname(abspath(__file__)))
DEFAULT_IMG_DIR = join(PROJECT_DIR, 'pictures')
MODEL_PATH = join(PROJECT_DIR, 'commons', 'model', 'model.h5')
LOGS_PATH = join(PROJECT_DIR, 'resources', 'logs')

