@echo off
rem Use this script to create a new environment called "BGRemover"

echo STEP 1: Creation of BGRemover environment
call conda create -n BGRemover python=3.10 -y
if errorlevel 1 (
    echo Failed to create the environment BGRemover
    goto :eof
)

rem If present, activate the environment
call conda activate BGRemover

rem Install additional packages with pip
echo STEP 2: Install python libraries and packages
call pip install numpy python-opencv tensorflow==2.10 gradio
if errorlevel 1 (
    echo Failed to install Python libraries.
    goto :eof
)

@echo off
rem install packages in editable mode
echo STEP 3: Install utils packages in editable mode
call cd .. && pip install -e .
if errorlevel 1 (
    echo Failed to install the package in editable mode
    goto :eof
)

rem Print the list of dependencies installed in the environment
echo List of installed dependencies
call conda list

set/p<nul =Press any key to exit... & pause>nul
