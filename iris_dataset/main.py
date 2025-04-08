"""
A simple Python script to read a CSV file using pandas and create a histogram 
for a specific column using matplotlib.

This script assumes that the CSV file and the column to be plotted exist.
"""

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def load_data():
    # Load iris dataset from sklearn
    iris = load_iris()

    # Convert dataset into pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Map target values to target names
    df['target'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    return df

def get_features(df):
    # Get list of all features
    features = df.columns.tolist()
    features.remove('target')
    return features

def plot_histogram(df, features):
    # Create a figure with multiple subplots
    fig, axs = plt.subplots(2, 2)

    # Create histograms for each feature
    for i, ax in enumerate(axs.flat):
        if i < len(features):
            for label in df['target'].unique():
                ax.hist(df[df['target'] == label][features[i]], label=label, alpha=0.7)
                ax.set_title(features[i])
                ax.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    df = load_data()
    print(df.head())
    df.describe()

    features = get_features(df)
    plot_histogram(df, features)

if __name__ == "__main__":
    main()
