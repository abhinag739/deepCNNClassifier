import os
from pathlib import Path
from unittest import makeSuite
import logging



logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:  ')
project_name = "deepClassifier"

#the src folder containing the Pipeline files, the artifact folder will be outside this
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py__",                          
    f"src/{project_name}/components/__init__.py__", 
    f"src/{project_name}/utils/__init__.py__",
    f"src/{project_name}/config/__init__.py__",
    f"src/{project_name}/pipeline/__init__.py__",
    f"src/{project_name}/entity/__init__.py__",
    f"src/{project_name}/constants/__init__.py__",
    f"configs/config.yaml",
    f"dvc.yaml",   #data version control yaml file
    f"params.yaml", #parameters yaml file, containing all our parameters
    f"init_setup.sh", #shell script file, which will help us to create the environment
    f"requirements.txt",
    f"requirements_dev.txt",  #Development requirements, certain requirements which are only used for development phase
    f"setup.py",
    f"setup.cfg",
    f"pyproject.toml",
    f"tox.ini",  #used for testing of the project locally
    f"research/stage_01.ipynb"  #Jupyter notebook files for trial purposes
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  #creating an empty file
            logging.info(f"Created an empty file: {filepath}")

    else:
        logging.info(f"File {filepath} already exists")
