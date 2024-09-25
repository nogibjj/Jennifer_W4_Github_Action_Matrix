"""
    library file
"""

import pandas as pd

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"


def load_dataset():
    df = pd.read_csv(dataset)
    return df


def grab_mean(df, col):
    return df[col].mean()


# def create_histogram(df, col):

# def grab_median
# def grab STD
# def grab max
