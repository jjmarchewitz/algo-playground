#!/bin/sh
cd docs/
rm -r generated/
mkdir generated/
rm -r source/
mkdir source/
python3 generate_source_rst.py
make html