# Shark Attack Project - Team 1

-------

## 1. Introduction

The objective of this project is to analyze the data from the shark attack dataset and to prove these hypotheses:

1. The US has more shark attacks than other countries.
2. Mork Shark attacks in the US happen during the summer season.
3. In the US, the White shark is the most dangerous species.


## 2. Collect the Data

First of all, we need to import the pandas and numpy library in order to use the functions and methods in Python. We also need to import matplotlib.pyplot library in order to create visualization in Python, such as plots and charts. 

We need then to call the dataset which we get from this website: 
https://www.sharkattackfile.net/incidentlog.htm

The data is in an Excel file, therefore, we need to use one of functions in the pandas library to read the Excel file by using read_excel method. The data then will be read in Python as a DataFrame.
In order to use the data from the original DataFrame without changing anything, we need to use .copy() method. This method will create a copy of the original DataFrame. Thus, the data cleaning and manipulation that we will do for the analysis will not influence the original DataFrame. 

### Data

The dataset used in this project is the Global Shark Attack File, which contains information about shark attacks from 1900 to 2016. The dataset has several columns, which consist of:

- Date - date when the injury recorded.
- Year - year of injury happened.
- Type - type of incidents.
- Country - country where the injury happened.
- State - state where the injury happened.
- Location - location where the injury happened. 
- Activity - activity that the victim did when the injury happened.
- Name - name of the victim.
- Sex - gender of the victim.
- Age - age of the victim.
- Injury - type of injury.
- Time - time when the injury happened.
- Species - species of the shark which attacked the victim.
- Source - source of information of the shark attack.
- Some unknowns - unknowns columns which exist from the data source.

...

## Visualizations

![Incidents per country](/charts/incidents_per_country.png?raw=true "Incidents per country")


## 4. Conclusions

The analysis on the shark attack data has proved our hypotheses that the US has more shark attacks than other countries and the attacks happen the most in summer. Furthermore, it is proven that White shark is the most dangerous species in the US.