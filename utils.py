import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') # We can suppress the warnings

def show_outliers(df):
    for i, column in enumerate(df.columns, 1):
        plt.subplot(4,4,i)
        g = sns.boxplot(df[column])
        g.set(xticklabels=[])
        plt.tight_layout()
        
def show_distribution(df):
    for i, column in enumerate(df.columns, 1):
        plt.subplot(4,4,i)
        g = sns.distplot(df[column]);
        g.set(yticklabels=[])
        g.set(xticklabels=[])
        plt.tight_layout()
    return g
        


__all__ = ['np', 'plt', 'pd', 'sns','show_outliers', 'show_distribution']
