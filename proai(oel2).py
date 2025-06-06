

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


#Load the dataset.
df = pd.read_csv('/CSVAI.csv')
df.head()
#Remove constant features using Variance Threshold.
from sklearn.feature_selection import VarianceThreshold
var_thres = VarianceThreshold(threshold=0)
var_thres.fit(df)
df.columns[var_thres.get_support()]

#Handle missing values:
# Replace missing numerical values with mean.
df.fillna(df.mean(), inplace=True)
# Replace missing categorical values with mode.
df.fillna(df.mode().iloc[0], inplace=True)
#Remove outliers from at least two numerical columns using the Z-score method
#(threshold = 3)
from scipy import stats
z = np.abs(stats.zscore(df))
threshold = 3
df = df[(z < 3).all(axis=1)]
#Generate the following plots using Seaborn or Matplotlib:
# Histogram of a numerical column.
plt.hist(df['column_name'])
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.show()
# Boxplot for visualizing outliers in a numerical column.
sns.boxplot(x=df['column_name'])
plt.show()
#- Countplot for a categorical feature
sns.countplot(x=df['column_name'])
plt.show()

from google.colab import drive
drive.mount('/content/drive')
