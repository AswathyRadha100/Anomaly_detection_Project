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
# Import necessary libraries and modules
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations

# Import the 'os' library for operating system-related tasks
import os

# Import credentials from an 'env.py' file 
from env import host, user, password


# -

def get_db_url(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# +
####################### logs_cohort function  #########################


def get_logs_cohort():
    '''
    Returns a DataFrame of data from the "logs" and "cohorts" tables using a left join and saves it as a local CSV file.
    If the CSV file already exists, it loads the data from the file.
    
    '''
    filename = "logs_cohort.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        # Create the URL for the database connection  
        url = get_db_url('curriculum_logs')  
        # Define the SQL query 
        query = '''
                
                SELECT *
                FROM logs
                LEFT JOIN cohorts ON logs.cohort_id = cohorts.id
                ;

                '''

        df = pd.read_sql(query, url)
        df.to_csv('logs_cohort.csv', index=False)
        return df
# -




