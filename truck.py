# truck.py



# import data science packages
import numpy as np
import pandas as pd



def load_truck_data(start : int = 2015, end : int = 2022, trace : bool = False, *args, **kwargs):
    r"""
    Load the Refrigerated Truck Volume data set from the start year to the end year.
    
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
    output_df : pandas.DataFrame
        The output data set for the refrigerated truck volumes.
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
    
    output_df = _clean_truck_df(full_df, trace)
    
    return output_df



def _clean_truck_df(df, trace : bool = False):
    r"""
    
    Parameters
    ----------
    df : pandas.DataFrame
        The refrigerated truck volume data frame.
    trace : bool, default value is False
        Boolean value whether to trace the output.
        
    Returns
    -------
    clean_df : pandas.DataFrame
        The cleaned up data frame.
    """
    
    # Some rows for truck volume may be assigned to different commodity marketing 
    #   seasons (e.g., a shipment on 1/1/2015 may be assigned to 2014, 2015, or both)
    #   indicated by the `Season` column. If both, then there will be 2 rows of data.
    # For our analysis, we disregard this fact because we are more interested in the 
    #   `date` of the shipment.
    # Therefore, we first group the data, then aggregate by summation of the `10,000 LBS` 
    #   column and finally we drop the `Season` column.
    groupby_cols = df.columns.drop(['Season','10,000 LBS']).tolist()
    clean_df = df.groupby(by=groupby_cols)[['10,000 LBS']].sum().reset_index()

    # The column descriptions are taken from the data set page:
    # https://agtransport.usda.gov/Truck/Refrigerated-Truck-Volumes/rfpn-7etz
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
    clean_df = clean_df[cols_to_keep]
    
    # Note that the `10,000 LBS` column is encoded as an integer value. We can infer that 
    #   truck movements with volumes below the 10,000 lbs threshold will have a value of 0.
    #   Since, this is weekly aggregated truck volumes there isn't use in keeping rows
    #   with 0 values for the `10,000 LBS` column.
    clean_df = clean_df[clean_df['10,000 LBS'] != 0]
    
    if trace:
        print(f"The cleaned data frame contains {clean_df.shape[0]} rows and {clean_df.shape[1]} columns.")
    
    return clean_df



if __name__ == '__main__':
    truck_df = load_truck_data(
        start=2015, # starting year
        end=2022,   # ending year
        trace=True
    )

    print(truck_df.info(verbose=True))
