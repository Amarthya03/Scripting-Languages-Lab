# a)Load the Titanic data set into one of the data structures (NumPy or Pandas).
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# b)Display header rows and description of the loaded data set.
iris = pd.read_csv('iris.csv')
print(iris.head())

# c) Remove unnecessary features (E.g. drop unwanted columns) from the data set.
# d) Manipulate data by replacing empty column values with a default value.

# e) Data Visualization for:
# (i) How many flowers of each species exists for each value of sepal width
ax = sb.countplot(x='Class', data=iris, hue='Sepal_Width', palette='Set1'). \
    set(xlabel="", ylabel="", Title="")
plt.show()

# (ii) How many flowers are there whose petal width is <1, between 1 to 2 and >2
interval = [0, 1, 2, 3]
categories = ['Less than 1', 'Between 1 & 2', 'Greater than 2']
iris['Petal_cats'] = pd.cut(iris.Petal_Width, interval, labels=categories)
ax = sb.countplot(x='Petal_cats', data=iris, palette='Set2').\
    set(xlabel='Petal Width', ylabel='Number of flowers', Title='Flowers v Petal Width')
plt.show()

# (iii) Tally the Iris-Versicolour and Iris-Virginica species according to the value of Sepal Width
