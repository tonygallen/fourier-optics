#!/bin/bash

conda deactivate
conda activate optics
cd ../docs
pip install -r doc_requirements.txt
make clean
make html
cd ../dev_scripts
