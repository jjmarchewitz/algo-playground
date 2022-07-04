#!/bin/sh
cd docs/
rm -r generated/
mkdir generated/
python3 generate_source_rst.py
make html