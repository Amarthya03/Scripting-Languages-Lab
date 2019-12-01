# a)Load the ‘Black Friday’ data set into one of the data structures (NumPy or Pandas).
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

black = pd.read_csv('blackfri.csv')

# b)Display header rows and description of the loaded data set.
print(black.head())

# c) Remove unnecessary features (E.g. drop unwanted columns) from the data set such as ‘User_ID’,
# ‘Product_ID ‘ ‘Stay_In_Current_City_Years’.
black.drop(['User_ID', 'Product_ID', 'Stay_In_Current_City_Years'], axis=1, inplace=True)
print(black.head())

# d) Manipulate data by replacing empty column values in ‘City_Category’ with a default value for the city.
black['City_Category'] = black['City_Category'].fillna("Unknown")

# e) Rename the attribute ‘City_Category’ to have ‘A’ to be ‘Metro Cities’, ‘B’ to be ‘Small Towns’,
# ‘C’ to be ‘Villages’.
black['City_Category'] = black['City_Category'].map({
    'A': 'Metro Cities',
    'B': 'Small Towns',
    'C': 'Villages'
})

# f) Rename the attribute ‘Product_Category_1’ to have ‘Baseball Caps’, ‘Product_Category_2’ to have
# ‘Wine Tumblers’ and ‘Product_Category_3’ to have ‘Pet Raincoats’

# g) Convert the attribute ‘Marital_Status’ to have ‘1:Married’ and ‘0:Un-Married’
black['Marital_Status'] = black['Marital_Status'].map({
    1: 'Married',
    0: 'Unmarried'
})

# h) Perform the following visualizations on the loaded data set:
#   i)   Tally of the Number of Male & Female persons who bought ‘Product_Category_1’ and ‘Product_Category_2’.
print(black.Pet_Raincoats)
#   ii)  Total Number of Male & Female persons belonging to each city category
ax = sb.countplot(x='Gender', data=black, hue='City_Category', palette='Set3')\
    .set(xlabel='Gender', ylabel='Number of persons', Title='Male and Female Persons belonging to each category')
plt.show()
