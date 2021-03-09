import pandas as pd
import env

# Define helper function to create connection url
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    This function uses information from env to create
    a url to connect and access the Codeup database.'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Employs a helper function and sql query to obtain telco data
def get_telco_data():
    '''
    This function reads data from Codeup's Telco database and 
    returns a dataframe containing all fields
    '''
    telco_sql = "SELECT * \
                 FROM customers \
                 JOIN internet_service_types USING (internet_service_type_id) \
                 JOIN contract_types USING (contract_type_id) \
                 JOIN payment_types USING(payment_type_id)"    
    return pd.read_sql(telco_sql, get_connection('telco_churn'))
