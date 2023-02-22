# datasets.py
#
# Description: This file contains methods that read, process, and clean input data.



import numpy as np
import pandas as pd



def load_truck_data(start : int = 2015, end : int = 2022, trace : bool = False, *args, **kwargs):
    r"""
    Load the refrigerated truck volume data set from the start year to the end year. The data set
    comes from the Agricultural Marketing Service of the USDA which can be accessed here:
    https://agtransport.usda.gov/Truck/Refrigerated-Truck-Volumes/rfpn-7etz.
    
    Parameters
    ----------
    start : int, default value is 2015
        The starting year to begin loading the truck data.
    end : int, default value is 2022
        The ending year (inclusive) to stop loading the truck data.
    trace : bool, default value is False
        Boolean value whether to trace the output.
    *args, **kwargs
        Additional keywords accepted into the load_file() method.
        
    Returns
    -------
    truck_df : pandas.DataFrame
        The output data frame for the refrigerated truck volumes.
    """
    
    lst = []
    for year in range(start, end+1):
        filename = f'data\Refrigerated_Truck_Volumes_{year}.csv'
        temp_df = pd.read_csv(filename, *args, **kwargs)
        lst.append(temp_df)
        
        if trace:
            print(f"The file '{filename}' contains {temp_df.shape[0]} rows and {temp_df.shape[1]} columns.")
    
    # concatenate all data frames together
    full_df = pd.concat(lst, axis=0, ignore_index=True)
    
    if trace:
        print(f"The full data frame contains {full_df.shape[0]} rows and {full_df.shape[1]} columns.")
    
    truck_df = _clean_truck_columns(full_df, trace=trace)
    
    return truck_df



def _clean_truck_columns(truck_df, cols_to_keep : list = None, trace : bool = False):
    r"""
    Clean the columns and values of the refrigerated truck volume data frame.

    Parameters
    ----------
    truck_df : pandas.DataFrame
        The refrigerated truck volume data frame.
    cols_to_keep : list, default value is None
        The columns to keep in the output data frame.
    trace : bool, default value is False
        Boolean value whether to trace the output.
        
    Returns
    -------
    clean_truck_df : pandas.DataFrame
        The cleaned up data frame.
    """
    
    # Some rows for truck volume may be assigned to different commodity marketing 
    #   seasons (e.g., a shipment on 1/1/2015 may be assigned to 2014, 2015, or both)
    #   indicated by the `Season` column. If both, then there will be 2 rows of data.
    # For our analysis, we disregard this fact because we are more interested in the 
    #   `date` of the shipment.
    # Therefore, we first group the data, then aggregate by summation of the `10,000 LBS` 
    #   column and finally we drop the `Season` column.
    groupby_cols = truck_df.columns.drop(['Season','10,000 LBS']).tolist()
    clean_truck_df = truck_df.groupby(by=groupby_cols)[['10,000 LBS']].sum().reset_index()

    # The column descriptions are taken from the data set page.
    if cols_to_keep is None:
        cols_to_keep = [
            'date',      # reporting date
            'Month',     
            'Year',      
            'Mode',      # all origins are domestic, mode is either truck or import, both of
                         #   which are truck movements
            'Region',    # broader region assigned to `Origin` by USDA's Transporation
                         #   Services Division 
            'Origin',    # broader region assigned to `District` by Market News Speciualty Crops
            'District',  # Origin Specialty Crops district
            'Commodity', # commodity (either fruit or vegetable)
            '10,000 LBS' # integer value for truck volume in 10,000 lbs
        ]
    clean_truck_df = clean_truck_df[cols_to_keep]

    # Note that the `10,000 LBS` column is encoded as an integer value. We can infer that truck movements 
    #   with volumes below the 10,000 lbs threshold will have a value of 0. Since, this is weekly aggregated 
    #   truck volumes there isn't use in keeping rows with 0 values for the `10,000 LBS` column.
    clean_truck_df = clean_truck_df[clean_truck_df['10,000 LBS'] != 0]

    # We want to fix the `date` column to be a datetime type.
    clean_truck_df.loc[:,'date'] = pd.to_datetime(clean_truck_df['date'], format='%m/%d/%Y')

    if trace:
        print(f"The cleaned data frame contains {clean_truck_df.shape[0]} rows and {clean_truck_df.shape[1]} columns.")

    return clean_truck_df



def aggregate_truck_df(truck_df, rule : str = '1M', trace : bool = False):
    r"""
    Aggregate the refrigerated truck volume data frame based on a datetime frequency conversion
    similar to the `resample()` method of a pandas.DataFrame. Additional handling is necessary
    with the use of the `pandas.Grouper` object. The idea comes from the Stack Overflow page:
    https://stackoverflow.com/questions/32012012/pandas-resample-timeseries-with-groupby.

    Parameters
    ----------
    truck_df : pandas.DataFrame
        The refrigerated truck volume data frame.
    rule : str, default value is '1M'
        The rule for the specified frequency (e.g., '1M' indicates every month) of the datetime column.
    trace : bool, default value is False

    Returns
    -------
    aggregated_truck_df : pandas.DataFrame
        The aggregated data frame based on a datetime frequency.
    """

    # Perform a split-apply-combine strategy for aggregating data on a monthly basis.

    # Some of the columns to group by. We remove `date` and `10,000 LBS` because
    #   `date` will be covered by a pandas.Grouper object and 
    #   `10,000 LBS` is the column whose value we wish to combine.
    groupby_cols = truck_df.columns.drop(['date', '10,000 LBS']).tolist()

    # First, sort rows by the date and set as the index.
    # Then, we choose to aggregate on a monthly basis.
    grouper = truck_df.sort_values('date').set_index('date').groupby(
        [pd.Grouper(freq='1M')] + groupby_cols 
    )

    # The combine strategy is the summation function.
    aggregated_truck_df = grouper['10,000 LBS'].sum().reset_index()

    return aggregated_truck_df



def load_fruit_data(trace : bool = False):
    r"""
    Load the fruit prices data set. The data set comes from the Economic Research Service department
    of the USDA which can be accessed here: 
    https://www.ers.usda.gov/data-products/fruit-and-tree-nuts-data/selected-weekly-fruit-movement-and-price/

    Parameters
    ----------
    trace : bool, default value is False
        Boolean value whether to trace the output.
    
    Returns
    -------
    fruit_df : pandas.DataFrame
        The output fruit prices data frame.
    """

    # get all sheet names of excel file
    sheets = pd.ExcelFile('data/selected-weekly-fruit-movement-and-price.xlsx').sheet_names

    # get list of all commodities
    fruit_df = pd.read_excel('data/selected-weekly-fruit-movement-and-price.xlsx',sheet_name=sheets[0])
    fruit_df = fruit_df.iloc[6:28,0]

    # get price of each week from each sheet
    for sheet in sheets:
        week = pd.read_excel('data/selected-weekly-fruit-movement-and-price.xlsx',sheet_name=sheet)
        week = week.iloc[6:28,17]
        week = pd.to_numeric(week, errors='coerce')
        fruit_df = pd.concat([fruit_df, week], axis=1)

    # reassign proper column names
    col = ['Commodity']
    for sheet in sheets:
        dt = sheet[-6:]
        p_date = '20'+dt[-2:]+'-'+dt[:2]+'-'+dt[2:4]
        col.append(p_date)

    fruit_df.columns = col

    return fruit_df


