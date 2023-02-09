import pandas as pd
import numpy as np
from vega_datasets import data
import matplotlib.pyplot as plt 
import seaborn as sns

from datetime import timedelta, datetime


import acquire as ac


import warnings
warnings.filterwarnings("ignore")




# functions for store data ---------


def convert_to_datetime(df):
    df.sale_date = pd.to_datetime(df.sale_date,infer_datetime_format= True)    
    
    return df

def add_feats(df):
    
    df = df.set_index('sale_date')
    
    df['month']= df.index.strftime('%b')
    
    df['dow']= df.index.strftime('%a')
    
    df['sales_total'] = (df.sale_amount * df.item_price)
    
    return df
    
    
# functions for german data ---------

def clean_german(df):
    
    df.Date = pd.to_datetime(df.Date, infer_datetime_format=True)

    df = df.set_index('Date')
    
    # creating features
    df['month'] = df.index.strftime('%m')
    df['year'] = df.index.strftime('%y')
    
    # fill nulls
    df.fillna(0, inplace=True)
    
    return df