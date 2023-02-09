import pandas as pd 
import requests
import math
import env
import os


pd.options.display.max_columns = None
pd.options.display.max_rows = None


def get_people_data(url):
    
    # creating an empty list of people
    people_data = []
    
    # while url is not none this code will keep repeating
    while url:
        
        # make API requests
        response = requests.get(url)
        
        # creates a .json object from our response
        people = response.json()
        
        ## Add the current page's planet information to the `planet_data` list
        people_data.extend(people['results'])
        
        # # Get the next URL from the response
        url = people['next']
        
        #return dataframe
    return people_data


def get_planets_data(url):
    planet_data = []
    while url:
        response = requests.get(url)
        planets = response.json()
        planet_data.extend(planets['results'])
        url = planets['next']
    return planet_data



#----------------------------------------------
 
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_store_data(get_connection):
    filename = "store.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else :
    # read the SQL query into a dataframe
        df = pd.read_sql('''select s.item_id,sale_id,sale_date, s.store_id, sale_amount,item_brand,item_name,item_price, store_zipcode, store_state from sales as s
                            join items using (item_id)
                            join stores on (stores.store_id)
                            

                         '''
                         , get_connection('tsa_item_demand'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename,index = False)

    # Return the dataframe to the calling code
        return df  
