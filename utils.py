import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') # We can suppress the warnings
from scipy import stats
import scipy as scipy

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

#Shapiro wilk test function
def shapiro_wilk(data):
    results = stats.shapiro(data)
    print(results)
    if results[1] > 0.05:
        #normality = 1
        print("Ho(Accepted): Sample is from a normal distribution.(P>0.05)")
    else:
        #normality = 0
        print("Ha(Rejected): Sample is not from a normal distribution")
        


__all__ = ['np', 'plt', 'pd', 'sns','show_outliers', 'show_distribution', 'shapiro_wilk', 'stats', 'scipy']
