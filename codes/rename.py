#load library
import pandas as pd

#load data
airbnb = pd.read_csv('data/Newyork_airbnb/AB_NYC_2019.csv')

#check columns
airbnb.columns

#check top observations
airbnb.head()

#rename columns
airbnb = airbnb.rename(columns={'name':'room_name','neighbourhood':'area'})

#check columns name modification
airbnb.columns  
airbnb.head()

#apply changes directly without saving
airbnb.rename(columns={'name':'room_name','neighbourhood':'area'}, inplace=True)
airbnb.columns

# rename using axis parameter
airbnb.rename(str.upper, axis='columns')

#rename index
airbnb.rename(index={0:'first',1:'second'})