### MAIN FORK CHANGES FOR M4R PROJECT

Bulk of project code is in **Notebooks**: 
* Input Data Pipeline
* Training
* Inference

Key modifications to ANTIPASTI
* Since the structures are AF3 models instead of experimental, they must be converted from file format mmCIF (AF3 output) to .pdb (ANTIPASTI input) which is done via PyMOL - these structures are assigned unique database IDs (instead of PDB IDs) for identification and tagged with _af to differentiate them from experimental structures, and Preprocessing has been adapted to accomodate.
* During train-test split checks, the antigen difference check bypassed as the dataset all share an antigen. The option for an AF3 confidence threshold is added, which helps filter the test set for entries that have a high model confidence.
* To support training on a variety of input maps in this project, we implement rectangular input support throughout ANTIPASTI's model, preprocessing, and utils.

# ANTIPASTI: interpretable prediction of antibody binding affinity exploiting Normal Modes and Deep Learning

[![Python 3.8 - 3.11](https://img.shields.io/badge/Python-3.8%20--%203.11-blue)](https://www.python.org/downloads/release/python-3113/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/license/mit/)
[![Tests](https://github.com/kevinmicha/ANTIPASTI/actions/workflows/tests.yml/badge.svg)](https://github.com/kevinmicha/ANTIPASTI/actions/workflows/tests.yml)
[![Docs](https://github.com/kevinmicha/ANTIPASTI/actions/workflows/documentation.yml/badge.svg)](https://kevinmicha.github.io/ANTIPASTI/index.html)
[![Coverage](https://codecov.io/gh/kevinmicha/ANTIPASTI/branch/main/graph/badge.svg?token=GJCV2H7L1J)](https://codecov.io/gh/kevinmicha/ANTIPASTI)
[![PyPI](https://img.shields.io/pypi/v/antipasti)](https://pypi.org/project/ANTIPASTI/)

ANTIPASTI (ANTIbody Predictor of Affinity from STructural Information) is a Python Deep Learning method that predicts the binding affinity of antibodies from their three-dimensional structure.

## Installation 

### Through PyPI

ANTIPASTI releases are distributed through the Python Package Index (PyPI). To install the latest version use `pip`:

```bash
pip install antipasti
```

### Through Anaconda
We provide an Anaconda environment that satisfies all the dependencies in `antipasti-env.yml`. 
```bash
git clone https://github.com/kevinmicha/ANTIPASTI
cd ANTIPASTI
conda env create -f antipasti-env.yml
conda activate antipasti-env
pip install .
```

Next, you can run the tests to make sure your installation is working correctly.

```bash
# While still in the ANTIPASTI directory:
pytest . 
```

### Manually handling the dependencies
If you want to use an existing environment, just omit the Anaconda commands above:
```bash
git clone https://github.com/kevinmicha/ANTIPASTI
cd ANTIPASTI
pip install .
```

or if you need to install it for your user only: 
```bash
python setup.py install --user 
```

## Requirements 

ANTIPASTI requires the following Python packages: 
* `adabelief-pytorch`
* `biopython`
* `matplotlib`
* `numpy`
* `opencv-python`
* `optuna`
* `pandas`
* `scikit-learn`
* `torch`
* `torchmetrics`
* `umap-learn`
    


## Example Notebooks and Documentation
The full documentation can be found [here](https://kevinmicha.github.io/ANTIPASTI/). 

Example notebooks are located in the [notebooks](https://github.com/kevinmicha/ANTIPASTI/tree/main/notebooks) folder:
* [[Tutorial] Training ANTIPASTI](https://github.com/kevinmicha/ANTIPASTI/blob/main/notebooks/%5BTutorial%5D%20Training%20ANTIPASTI.ipynb)
* [[Tutorial] Predicting affinity using ANTIPASTI](https://github.com/kevinmicha/ANTIPASTI/blob/main/notebooks/%5BTutorial%5D%20Predicting%20affinity%20using%20ANTIPASTI.ipynb)
* [[Tutorial] Explaining binding affinity with ANTIPASTI](https://github.com/kevinmicha/ANTIPASTI/blob/main/notebooks/%5BTutorial%5D%20Explaining%20binding%20affinity%20with%20ANTIPASTI.ipynb)
* [[Tutorial] Combining AlphaFold and ANTIPASTI](https://github.com/kevinmicha/ANTIPASTI/blob/main/notebooks/%5BTutorial%5D%20Combining%20AlphaFold%20and%20ANTIPASTI.ipynb)

You can download normal mode correlation maps computed at atomistic scale (instead of residue scale) [here](https://drive.google.com/drive/folders/1E8-GwQq9GHBE0A6r2t8dblAzP7qf0seQ?usp=sharing) and place them in `data/dccm_maps_full_ags_all_aa`.

## Attribution

If you use this code, please cite the [paper](https://kevinmicha.github.io/ANTIPASTI/citing.html) indicated in the documentation.
