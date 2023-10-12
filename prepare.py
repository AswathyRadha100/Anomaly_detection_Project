# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# Import numpy for numerical operations
import numpy as np

# Import Pandas for data manipulation 
import pandas as pd

# Import Matplotlib for data visualization
import matplotlib.pyplot as plt

# Import seaborn for data visualization
import seaborn as sns

# -

def summarize(df) -> None:
    '''
    Summarize will take in a pandas DataFrame
    and print summary statistics:
    info
    shape
    outliers
    description
    missing data stats
    
    Args:
    df (DataFrame): The DataFrame to be summarized.
    k (float): The threshold for identifying outliers.
    
    return: None (prints to console)
    '''
    # print info on the df
    print('Shape of Data: ')
    print(df.shape)
    print('======================\n======================')
    print('Info: ')
    print(df.info())
    print('======================\n======================')
    
    
    # Calculate missing values and percentages
    missing_values = df.isnull()
    missing_count = missing_values.sum()
    missing_percentage = (missing_count / len(df)) * 100
    
    print('Missing Data Stats:')
    print('Missing Data Count by Column:')
    print(missing_count)
    print('Missing Data Percentage by Column:')
    print(missing_percentage)


# +

def prepare_logs_cohort(df):
    '''
    Preprocesses a DataFrame containing logs and cohorts data:
    
    1. Combines 'date' and 'time' into a new 'datetime' column.
    2. Drops the 'date', 'time', 'id', and 'deleted_at' columns.
    3. Sets the 'datetime' column as the index and sorts the DataFrame.

    Parameters:
    df (DataFrame): The input DataFrame containing logs and cohorts data.

    Returns:
    DataFrame: The preprocessed DataFrame with the specified transformations.
    '''
    # Combine 'date' and 'time' into a new 'datetime' column
    df['datetime'] = pd.to_datetime(df.index + ' ' + df['time'])
    
    # Drop specified columns, handling potential column name variations
    columns_to_drop = ['date', 'time', 'id', 'deleted_at']
    for column in columns_to_drop:
        if column in df.columns:
            df = df.drop(column, axis=1)
    
    # Set 'datetime' as the index and sort the DataFrame by the index
    df = df.set_index('datetime').sort_index()

    return df


# -

def sort_and_reset_index(df, column_name):
    """
    Sort a DataFrame by a specified column and reset the index.

    Args:
    df (pd.DataFrame): The DataFrame to be sorted.
    column_name (str): The name of the column to sort by.

    Returns:
    pd.DataFrame: The sorted DataFrame with the index reset.
    """
    # Sort the DataFrame by the specified column
    df_sorted = df.sort_values(by=column_name)

    # Reset the index to reflect the new order
    df_sorted.reset_index(drop=True, inplace=True)

    return df_sorted








