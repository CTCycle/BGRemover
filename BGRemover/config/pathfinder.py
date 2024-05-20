from os.path import join, dirname, abspath 

PROJECT_DIR = dirname(dirname(abspath(__file__)))
DEFAULT_IMG_DIR = join(PROJECT_DIR, 'pictures')
MODEL_DIR = join(PROJECT_DIR, 'utils', 'model')
