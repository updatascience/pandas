#load libraries 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline  

#load data
airbnb = pd.read_csv('data/Newyork_airbnb/AB_NYC_2019.csv')
# check top observations
airbnb.head()

#box plot
airbnb['neighbourhood_group'].value_counts().plot(kind='bar')

#add title and change picture size
airbnb['neighbourhood_group'].value_counts().plot(kind='bar', title = 'Airbnb neighbourhood rooms in NY', figsize = (14,6))

# Add label for x-axis & y-axis
vis1 = airbnb['neighbourhood_group'].value_counts().plot(kind='bar', title = 'Airbnb neighbourhood rooms in NY', figsize = (14,6))
vis1.set_xlabel('Neighbourhood')
vis1.set_ylabel('Number of rooms')

# Add title and label for x-axis & y-axis
vis1 = airbnb['neighbourhood_group'].value_counts().plot(kind='bar', title = 'Airbnb neighbourhood rooms in NY', figsize = (14,6))
vis1.set_xlabel('Neighbourhood')
vis1.set_ylabel('Number of rooms')
vis1.tick_params(axis='x', rotation=45)

#scatter plot
plt.scatter(airbnb['neighbourhood_group'],airbnb['price'])
plt.show()

# Add title and label for x-axis & y-axis
plt.scatter(airbnb['neighbourhood_group'],airbnb['price'])
plt.title('Room price in neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('Price')
plt.show()

#change color
plt.scatter(airbnb['neighbourhood_group'],airbnb['price'],color ='green')
plt.title('Room price in neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('Price')
plt.show()

# Scatterplot Matrix
pd.plotting.scatter_matrix(airbnb[['price','availability_365','minimum_nights','number_of_reviews']],figsize=(10,10))