# Shark Attack Project - Team 1

### Presentation

[Link to Google slideshow](https://docs.google.com/presentation/d/1eZ5r_cNE_Yd3IT_d6c1fR7CATcM_BcEJu_etBod41iE/edit#slide=id.g2e9c3044cba_0_27)

-------

## Introduction
The original data was retrieved from the Global Shark Attack File, a repository that provides current and historical data on shark/human interactions. Based on a short overview of the database and its variables, formulated the following hypothesis:

1- **Geographic Hypothesis**: The United States has a higher number of shark attacks compared to other countries.

2- **Seasonal Hypothesis** : In the United States, most shark attacks occur during the summer season.

3- **Species Hypothesis**: In the United States, the White Shark is responsible for the most attacks and is considered the most dangerous type.



## Collect the Data

First of all, we need to import the pandas and numpy library in order to use the functions and methods in Python. We also need to import matplotlib.pyplot library in order to create visualization in Python, such as plots and charts. 

We need then to call the dataset which we get from this website: 
https://www.sharkattackfile.net/incidentlog.htm

The data is in an Excel file, therefore, we need to use one of functions in the pandas library to read the Excel file by using read_excel method. The data then will be read in Python as a DataFrame.
In order to use the data from the original DataFrame without changing anything, we need to use .copy() method. This method will create a copy of the original DataFrame. Thus, the data cleaning and manipulation that we will do for the analysis will not influence the original DataFrame. 



## Data Analysis Process 

1-Data Import
2-Data Selection/Cleaning
3-Data Standardization
4-Data Filtering/Transformation




## Visualizations

Geographic Hypothesis: The United States has a higher number of shark attacks compared to other countries.
Pie Chart enabled the visualization of shares of different countries in the total number of incidents, displayed in percentages.

![Incidents per country](/charts/incidents_per_country.png?raw=true "Incidents per country")

Bar/Count Plots allowed us to visualize the frequency of shark attacks over different variables

#Seasonal Hypothesis
![Attacks per season](/charts/attacks_per_season.png?raw=true "Incidents per season")

Species Hypothesis
![Attacks per species](/charts/attacks_per_species.png?raw=true "Incidents per species")


## Conclusions

The analysis on the shark attack data has proved our hypotheses that the US has more shark attacks than other countries and the attacks happen the most in summer. Furthermore, it is proven that White shark is the most dangerous species in the US.
