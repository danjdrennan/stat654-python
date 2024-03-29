# STAT654: Statistical Computing with R and Python

**Instructor: Professor Sharmistha Guha**

**TA: Dan Drennan**

**Texas A&M University, College Station, Texas, USA**

**Term: Spring 2022**
## Intro

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
The major difference is that Anaconda comes with a GUI application for package
and environment management. The miniconda (and main anaconda distribution) comes
only with a command line interface. Both sites have good documentation for downloading
and installing the package manager but additional tutorials via YouTube are shared below:

* [Python Tutorial: Anaconda - Installation and Using Conda](https://youtu.be/YJC6ldI3hWk)

* [Anaconda Beginners Guide for Linux and Windows - Python Working Environments Tutorial](https://youtu.be/MUZtVEDKXsk)

### Conda environments

If you're looking for a complete Python environment (collection of libraries/packages) to get started,
you may be interested in creating an environment from the `stats.yml` file in this repository.
Steps to install this environment:

1. Install the conda package manager

2. Download this repository locally

3. Open a conda terminal

4. In the terminal, execute

```bash
$ conda env create -f stats.yml
```

More details on conda environments can be found at
[docs.conda.io/mange-environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

## Developer Environments

As R is a language and RStudio is a developer environment for using R,
Python is a language that is best used in some form of a developer environment.
I personally recommend using [Microsoft Visual Studio
Code](https://code.visualstudio.com/) as your Python IDE,
although [Pycharm](https://www.jetbrains.com/pycharm/) is a popular alternative.
RStudio can also be used to interpret Python.

**Disclaimer**:
I have no experience setting up the latter two environments.
YouTube has great instructions for getting started with either one.

## Datasets

Datasets are sourced from the UCI Machine Learning Repository.
The [Auto MPG](https://archive-beta.ics.uci.edu/ml/datasets/auto+mpg) dataset will be used for regression.
The [Iris](https://archive-beta.ics.uci.edu/ml/datasets/iris) dataset will be used for classification.
References for the respective datasets are below:

1. Auto MPG. (1993). UCI Machine Learning Repository.

2. Fisher, R.A.. (1988). Iris. UCI Machine Learning Repository.
