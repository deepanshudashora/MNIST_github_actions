from setuptools import setup, find_packages

setup(
    name="mnist_model",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'tqdm',
        'matplotlib',
        'numpy',
        'torchsummary'
    ],
) 