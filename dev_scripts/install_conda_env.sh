#!/bin/bash
# Remove and create conda environment, install package locally

cd ..
conda deactivate
conda remove --name optics --all
conda create --name optics python=3.9
conda activate optics
pip install -r requirements.txt
pip install -e .
cd dev_scripts
