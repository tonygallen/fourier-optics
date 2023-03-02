#!/bin/bash

conda deactivate
conda activate optics
cd ../docs
pip install -r doc_requirements.txt
make html
cd ../dev_scripts
