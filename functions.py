#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import seaborn as sns





#Load Data
def load_data(url):
    original_df = pd.read_excel(url)
    df = original_df.copy()
    return df

url = "https://www.sharkattackfile.net/spreadsheets/GSAF5.xls"
df = load_data(url)






#Get First Impression of Dataset
def get_first_impression(df, n=3):
    return df.head(n)

print(get_first_impression(df))





#shape function 
def get_shape(df):
    return df.shape

print(get_shape(df))






#Clean Column Names
def clean_column_names(df):
    df = df.rename(columns={"Species ": "Species"})
    return df

df = clean_column_names(df)
print(df.columns)





# Cleaning Data
def select_columns(df, columns):
    df = df[columns]
    return df

columns = ["Date", "Year", "Country", "Location", "Injury", "Species", "Activity"]
df = select_columns(df, columns)






#Drop Rows with All NaN Values
def drop_all_nan_rows(df):
    df = df.dropna(how='all')
    return df

df = drop_all_nan_rows(df)
print(get_shape(df))





#Drop Rows with NaN Year
def drop_nan_year(df):
    df = df.dropna(subset=['Year'])
    return df

df = drop_nan_year(df)
print(get_first_impression(df))





#correct Year Format
def correct_year_format(df):
    df['Year'] = df['Year'].astype(int)
    return df

df = correct_year_format(df)
print(get_first_impression(df))







#Filter Data for Last 10 Years
def filter_last_10_years(df):
    df = df[df['Year'] >= 2015]
    return df








df = filter_last_10_years(df)

#Incident Counts by Country
def incident_counts_by_country(df, top_n=5):
    return df['Country'].value_counts().head(top_n)

print(incident_counts_by_country(df))









#top countries with shark attacks piechart 
import matplotlib.pyplot as plt

def plot_top_countries_pie_chart(df):
    """
    Plots a pie chart of the top 4 countries with the most incidents and a fifth slice for the rest.
    
    Parameters:
        df (pd.DataFrame): The dataframe containing the data.
    """
    # Get the top 4 countries
    top_4 = df.Country.value_counts()[0:4]
    # Sum the incidents for the remaining countries
    others = df.Country.value_counts()[4:].sum()
    # Add 'Others' to the top 4 countries
    top_4['Others'] = others
    
    # Plot the pie chart
    top_4.plot.pie(autopct='%1.1f%%', startangle=90, title='Incidents per country', figsize=(10, 10), fontsize=15)
    plt.show()

# Example usage:
# Assuming `df` is already defined
plot_top_countries_pie_chart(df)







`#Filter Incidents in USA
def filter_incidents_usa(df):
    df_usa = df[df['Country'] == 'USA'].copy()
    return df_usa

df_usa = filter_incidents_usa(df)
print(get_first_impression(df_usa))






#Format Date Column
def format_date_column(df, date_column='Date'):
    """
    Formats the date column by removing unwanted characters, adding hyphens, converting to datetime, 
    and formatting to 'dd-mm-yy'.
    
    Parameters:
        df (pd.DataFrame): The dataframe containing the date column.
        date_column (str): The name of the date column to format. Default is 'Date'.
    
    Returns:
        pd.DataFrame: The dataframe with the formatted date column.
    """
    # Remove all whitespaces, commas, and hyphens from the date
    df[date_column] = df[date_column].apply(lambda x: re.sub(r'[-\s,]', '', str(x)))

    # Add a hyphen after the first four digits
    df[date_column] = df[date_column].apply(lambda x: re.sub(r'(\d{4})', r'\1-', str(x)))

    # Convert the month into a numerical value and format to 'dd-mm-yy'
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce').dt.strftime('%d-%m-%y')

    # Convert the 'Date' column back to datetime format
    df[date_column] = pd.to_datetime(df[date_column], format='%d-%m-%y', errors='coerce')
    
    # Reset the index of the dataframe
    df = df.reset_index(drop=True)
    
    return df

# Example usage:
# Assuming `df_usa` is already defined
df_usa = format_date_column(df_usa)
print(df_usa.head(3))








#Add Season Column
def add_season_column(df_usa):
    def get_season(Date):
        if pd.isna(Date):
            return 'Unknown'
        month = pd.to_datetime(Date).month
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Fall'
    
    df_usa['Season'] = df_usa['Date'].apply(get_season)
    return df_usa

df_usa = add_season_column(df_usa)
print(get_first_impression(df_usa))






#Group by Season and Year
def group_by_season_year(df_usa):
    grouped_season = df_usa.groupby(['Season', 'Year']).size().unstack(fill_value=0)
    grouped_season['Total sum'] = grouped_season.sum(axis=1)
    grouped_season = grouped_season.drop('Unknown')
    return grouped_season

grouped_season = group_by_season_year(df_usa)
print(grouped_season)






#Plot Incidents by Season
def plot_incidents_by_season(grouped_season):
    grouped_season[['Total sum']].plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.title('Shark Attacks in the USA by Season')
    plt.ylabel('Number of Attacks')
    plt.xlabel('Season')
    plt.xticks(rotation=0)
    plt.legend(loc='upper right')
    plt.show()

plot_incidents_by_season(grouped_season)





#Standardize Species Names
def standardize_species_names(df_usa):
    df_usa['Species'].fillna("Not Specified", inplace=True)
    species_replacements = {
        "white shark": "White Shark",
        "tiger shark": "Tiger Shark",
        "bull shark": "Bull Shark",
        "nurse shark": "Nurse Shark",
        "blacktip shark": "Blacktip Shark",
    }
    
    for key, value in species_replacements.items():
        df_usa['Species'] = df_usa['Species'].apply(lambda x: value if key in str(x).lower() else x)
    
    common_species = df_usa['Species'].value_counts().head(7).index
    df_usa['Species'] = df_usa['Species'].apply(lambda x: x if str(x) in common_species else "Others")
    
    return df_usa

df_usa = standardize_species_names(df_usa)







#Plot Shark Attacks by Species
def plot_shark_attacks_by_species(df_usa):
    fig = sns.countplot(y="Species", data=df_usa, order=df_usa["Species"].value_counts().index)
    fig.set_title('Shark Attacks by Species')
    plt.show()

plot_shark_attacks_by_species(df_usa)







#Final Data Check
def final_data_check(df_usa):
    print(df_usa.head())
    print(df_usa['Species'].value_counts().head(10))
    print(df_usa['Species'].isnull().sum())
    print(df_usa['Species'].value_counts())

final_data_check(df_usa)






# Conclusion
In this project, we performed data cleaning, exploration, and visualization to understand shark attack incidents.
We identified the most common species involved, analyzed the data by year and location, and created visualizations
to represent the findings.