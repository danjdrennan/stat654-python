# Getting Started With Python for Data Analysis

The repo includes a tutorial for using Python for simple data analyses using the Scipy suite of libraries.
We'll also look at the statsmodels library for regression and classification modeling.
Below you'll find support for downloading and installing Python alongside a developer environment.
Datasets are cited here and when used in the repository.
Finally, at the end I give instructions for installing a python environment which is fairly comprehensive
for doing statistical analyses using Python.
There are instructions for installing that environment using the conda package manager if you'd like an
easy environment to get started with.

## Quickstart

Longterm, you'll want to set up a proper local environment for any programming language you're working with frequently.
In the short term, it is easier to use [Google Colab](https://colab.research.google.com/) for Python or
[RStudio cloud](https://rstudio.cloud/) for R.
Both are free, cloud-based solutions with ready-made environments for most work.

## Downloading and setting up Python

Many of the libraries in the Scipy stack require compiled C code to run.
For the best experience using these, users are recommended to download the
[Anaconda distribution](https://www.anaconda.com/products/individual) and its `conda` package manager.
This is a fairly large distribution, and experienced users may prefer to download the
[miniconda distribution](https://docs.conda.io/en/latest/miniconda.html) instead.
Both sites have pretty good documentation for downloading and installing the software,
but additional tutorials via YouTube are shared below:

* [Python Tutorial: Anaconda - Installation and Using Conda](https://youtu.be/YJC6ldI3hWk)

* [Anaconda Beginners Guide for Linux and Windows - Python Working Environments Tutorial](https://youtu.be/MUZtVEDKXsk)

## Developer Environments

As R is a language and RStudio is a developer environment for using R,
Python is a language that is best used in some form of a developer environment.
I personally recommend using [Microsoft Visual Studio Code](https://code.visualstudio.com/) as your Python environment,
although [Pycharm](https://www.jetbrains.com/pycharm/) is a popular alternative.
Finally, RStudio can be used to interpret Python.

**Disclaimer**:
I have no experience setting up the latter two environments.
YouTube has great instructions for getting started with either one.

## Datasets

Datasets are sourced from the UCI Machine Learning Repository.
The [Auto MPG](https://archive-beta.ics.uci.edu/ml/datasets/auto+mpg) dataset will be used for regression.
The [Iris](https://archive-beta.ics.uci.edu/ml/datasets/iris) dataset will be used for classification.
