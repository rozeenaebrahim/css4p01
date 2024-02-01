# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


df=pd.read_csv('C:/Users/rebrahim/css2024_week1_project1/movie_dataset.csv')


#Q0 Cleaning up data
print(df.info())
print(df.describe())

"""
sort out column names
"""
df.rename(columns={"Runtime (Minutes)": "Runtime_Minutes"}, inplace=True)
df.rename(columns={"Revenue (Millions)": "Revenue_Millions"}, inplace=True)

"""
sort out nan values
"""
Revenue_mean = df["Revenue_Millions"].mean()
df["Revenue_Millions"].fillna(Revenue_mean, inplace = True) 

Metascore_mean = df["Metascore"].mean()
df["Metascore"].fillna(Metascore_mean, inplace = True) 

#Q1 What is the highest rated movie in the dataset?

max_rating_value=df['Rating'].max()
print("Q1: Highest rated movie is:")
print(df[df['Rating'] == max_rating_value]["Title"])

#Q2 What is the average revenue of all movies in the dataset? 
Revenue_mean = df["Revenue_Millions"].mean()
print("Q2: Average revenue of all movies:")
print(Revenue_mean)

#Q3 What is the average revenue of movies from 2015 to 2017 in the dataset?
df1 = df[df["Year"] >= 2015] #Filter for 2015 and above (data only goes up to 2016)
revenue_average_2015_plus=df1["Revenue_Millions"].mean()
print("Q3: Average revenue between 2015 and 2017:")
print(revenue_average_2015_plus)

#Q4 How many movies were released in the year 2016?
print("Q4: The number of movies released in the year 2016:")
print(df["Year"].value_counts()[2016])

#Q5. How many movies were directed by Christopher Nolan?
print("Q5: The number of movies directed by Chris Nolan:")
print(df["Director"].value_counts()["Christopher Nolan"])

#Q6. How many movies in the dataset have a rating of at least 8.0?
print("The number of movies with a rating of at least 8.0")
print(len(df[df["Rating"] >= 8.0]))

#Q7 What is the median rating of movies directed by Christopher Nolan?
print("Q6 Median rating of Christopher Nolan movies:")
print(df[df['Director'] == "Christopher Nolan"]["Rating"].median())

#???? Q8 Find the year with the highest average rating?
print("I selected the year with the largest rating from the list below to show the year with the highest average rating")
print(df.groupby('Year')['Rating'].mean())

#Q9 What is the percentage increase in number of movies made between 2006 and 2016?
number_of_movies_2016=df["Year"].value_counts()[2016]
number_of_movies_2006=df["Year"].value_counts()[2006]
percentage_increase=((number_of_movies_2016-number_of_movies_2006)/(number_of_movies_2006))*100
print("Q9 Percentage increase in number of movies made between 2006 and 2016:")
print(percentage_increase)

#Q10 Find the most common actor in all the movies?
df2=df['Actors'].str.replace(' ', '')
df3 = pd.DataFrame([sub.split(",") for sub in df2])
df4 = pd.concat([df3[0], df3[1],df3[2], df3[3]],ignore_index=True).to_frame()
df5 = df4.groupby(0).size()
print("Q10 The most common actor in all the movies")
print(df5.idxmax(0, skipna=True))

#Q11 How many unique genres are there in the dataset?
df6=df['Genre'].str.replace(' ', '')
df7 = pd.DataFrame([sub.split(",") for sub in df6])
df8 = pd.concat([df7[0], df7[1],df7[2]],ignore_index=True).to_frame()
df9=df8.groupby(0).size()
print("Q11 The number of unique genres in the dataset:")
print(len(df9))
