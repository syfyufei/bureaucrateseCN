from setuptools import setup, find_packages
import os

# 获取README内容
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="bureaucratese",
    version="0.1.0",
    packages=find_packages(include=['bureaucratese', 'bureaucratese.*']),
    install_requires=[
        'pandas>=1.0.0',
        'jieba>=0.42.1',
        'torch>=1.7.0',
        'transformers>=4.0.0',
        'numpy>=1.19.0',
        'tqdm>=4.45.0'
    ],
    author="Adrian",
    author_email="",
    description="A Python package for analyzing the density of Chinese official discourse in text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrian/bureaucratese",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        'bureaucratese': ['data/*.csv', 'models/bert-base-chinese/*', 'preprocessed/*']
    },
)