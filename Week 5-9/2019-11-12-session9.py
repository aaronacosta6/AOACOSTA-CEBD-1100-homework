#2019 November 12 – Session 9 + Assignment 9
# UNCOMMENT TO TOGGLE EACH PLOT

import pandas as pd
from matplotlib import pyplot as plt

# PLOT no. 1
""" df = pd.read_csv("/Users/Aaron/Dropbox/Concordia/Continuing Education/CEBD 1100 - Intro to Python and Data Analysis/Session 9/data-1.csv")

df[1] = (((df['var1'] - (-10))**2) + (df['var2'] - (-4.25))**2)
df[2] = (((df['var1'] - (-6.3))**2) + (df['var2'] - (-8.6))**2)
df[3] = (((df['var1'] - (-1.14))**2) + (df['var2'] - (4.23))**2)

df['class'] = df[[1,2,3]].idxmin(axis=1)

print(df.head())

plt.scatter(df['var1'], df['var2'], c = df['class'])
plt.show() """


#PLOT no. 2
""" df = pd.read_csv("/Users/Aaron/Dropbox/Concordia/Continuing Education/CEBD 1100 - Intro to Python and Data Analysis/Session 9/data-2.csv")

df[1] = (((df['var1'] - (21.39))**2) + (df['var2'] - (16.31))**2)
df[2] = (((df['var1'] - (20.93))**2) + (df['var2'] - (1.8))**2)
df[3] = (((df['var1'] - (28.06))**2) + (df['var2'] - (21.73))**2)

df['class'] = df[[1,2,3]].idxmin(axis=1)

plt.scatter(df['var1'], df['var2'], c = df['class'])
plt.show() """



# PLOT no. 3
df = pd.read_csv("/Users/Aaron/Dropbox/Concordia/Continuing Education/CEBD 1100 - Intro to Python and Data Analysis/Session 9/data-3.csv")

df[1] = (((df['var1'] - (95.34))**2) + (df['var2'] - (124.41))**2)
df[2] = (((df['var1'] - (136.22))**2) + (df['var2'] - (154.90))**2)
df[3] = (((df['var1'] - (185.33))**2) + (df['var2'] - (185.39))**2)

df['class'] = df[[1,2,3]].idxmin(axis=1)

plt.scatter(df['var1'], df['var2'], c = df['class'])
plt.show()