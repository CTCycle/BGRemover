@echo off
rem install packages in editable mode

call conda activate BGRemover && cd .. && pip install -e .
if errorlevel 1 (
    echo Failed to install the package in editable mode
    goto :eof
)
