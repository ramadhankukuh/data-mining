import os
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(72018)

# Data Boston dibaca dari file pickle di folder data/, karena
# sklearn.datasets.load_boston sudah dihapus pada scikit-learn versi baru.
_BOSTON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "boston_housing_clean.pickle")


def to_2d(array):
    return array.reshape(array.shape[0], -1)


def boston_dataframe(description=False):
    with open(_BOSTON_PATH, "rb") as f:
        boston = pickle.load(f)

    df = boston["dataframe"].copy()

    if description:
        return df, boston["description"]
    return df


def plot_exponential_data():
    data = np.exp(np.random.normal(size=1000))
    plt.hist(data)
    plt.show()
    return data


def plot_square_normal_data():
    data = np.square(np.random.normal(loc=5, size=1000))
    plt.hist(data)
    plt.show()
    return data
