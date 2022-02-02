from typing import Union

import numpy as np
import matplotlib.pyplot as plt

def plot(x: np.ndarray, y: np.ndarray, labels:dict=None, fname:str=None, **kwargs)->None:
    """
    Helper function for plotting data using plt.plot function.
    The plotter standardizes grids and figure sizes, and reduces overhead.

    Inputs:
    -------
    x: numpy.ndarray or list-like
        Data to plot on the horizontal axis

    y: numpy.ndarray or list-like
        Data to plot on the vertical axis

    labels: dict
        A dictionary of plot labels, including
        - title
        - x_label
        - y_label
        Note: Any format other than
        {
            'title': 'Some time',
            'x_label': 'Some x label (with units), 
            'y_label': 'Some y label (with units)'
        }
        will not be used. Any one of these (or all of them) can be optionally skipped,
        but this is the format to pass labels into this plotter.

    fname: str
        A filename to save the plot. The filename should include an extension.
    """
    plt.figure(figsize=(16, 9))
    
    # If labels are present, use them
    # Assume labels are correctly passed as a dict with expected keys
    if labels:
        try:
            plt.title(labels['title'], fontsize=24)
        except Exception:
            pass
        try:
            plt.xlabel(labels['x_label'], fontsize=20)
        except Exception:
            pass
        try:
            plt.ylabel(labels['y_label'], fontsize=20)
        except Exception:
            pass
    
    plt.plot(x, y, *args, **kwargs)
    plt.grid(alpha=0.2)
    
    if fname:
        plt.savefig(fname, format=fname.split('.')[-1], dpi=300)
    