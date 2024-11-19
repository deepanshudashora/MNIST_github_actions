# MNIST Model

![Build Status](https://github.com/{username}/{repository-name}/workflows/Python%20application/badge.svg)

This repository contains a PyTorch implementation of a CNN model for MNIST digit classification.

## Features
- Custom CNN architecture
- Data augmentation
- Training and testing utilities
- Performance visualization
- Per-class accuracy analysis

## Tests
The model includes several automated tests:
- Parameter count verification (<10k parameters)
- Output shape validation
- Training speed assessment
- Model stability checks
- Loss computation verification

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python train.py`
4. Run tests: `pytest tests/` 