# utils.py
#
# Description: This file contains utility methods that would otherwise clutter the 
#              Jupyter notebooks.



import numpy as np
import pandas as pd
import re

from datetime import datetime



def month_number_to_name(number):
    r"""
    Returns the name of the month (e.g., January) given the number for the month (e.g., 1 or 01).
    """
    
    return datetime.strptime(number, '%m').strftime('%B')



def map_to_state_code(state):
    r"""
    Returns the state abbreviation code (e.g., CA) given the state name (e.g., California).
    """

    state_code_mapping = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }

    if state in state_code_mapping:
        return state_code_mapping[state]
    else:
        return np.nan
    


def only_word(string):
    r"""
    Return only the words/characters of a string (e.g., 'Avocados 4' -> 'Avocados').
    """

    return re.sub('[^a-zA-Z]+', '', string)



def find_common_items(df1, df2, col): 
    r"""
    Find common values between two data frames based on the column given as an input.
    """

    df_1_col = df1[col].unique()
    common_commodities = []
    for i in df2[col]:
        if i in df_1_col:
            common_commodities.append(i)
    return common_commodities


 
def find_date(df, n):
    r"""
    Calculate the top n fast growth period based on the total COVID-19 cases.
    """
    diff_list = []
    for i in range(0, len(df['tot_cases'])-1):
        difference = (df['tot_cases'].iloc[i+1] - df['tot_cases'].iloc[i])
        diff_list.append((difference,df['date_updated'].iloc[i+1]))
        result = sorted(diff_list, reverse = True)
    return result[:n]


