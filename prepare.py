import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def clean_telco(df):
    '''
    This function cleans data obtained from Codeup's Telco database by: 
    
    removing duplicate columns, 
    
    #### FILL IN WITH SPECIFIC CHANGES
    
    '''
    
    # fill nans in total_charges - these eleven customers have tenure of 0, so it is
    # reasonable to replace nan with 0
    df.assign(total_charges=df.total_charges.fillna(0))
    
    # convert total_charges to float
    df.total_charges = pd.to_numeric(df.total_charges, errors ='coerce').astype('float64')
    
    # remove duplicate or unnecessary information (already encoded in _id columns of the same names): 
    df.drop(columns=['internet_service_type', 'contract_type', 'payment_type'], inplace = True)
    
    # rename tenure to monthly tenure & create a column to represent tenure in years
    df = df.rename(columns = {'tenure':'tenure_months'})
    df['tenure_years'] = round(df.tenure_months / 12, 2)

    # Creating dataframe of dummy variables for gender: male = 1, female = 0, streaming_tv, and streaming_movies
    dummycols = ['gender', 'streaming_tv', 'streaming_movies']
    df_dummies = pd.get_dummies(dummycols, drop_first = False)

    # Adding dummies to our original dataframe
    df = pd.concat([df, df_dummies], axis = 1)

    # Drop original gender, streaming_tv, and streaming_movies columns
    df = df.drop(columns = dummycols, axis = 1)
    
    # Create one variable 'phone_services' combining phone service and multiple lines
    # 0 = no phone service, 1 = one line, 2 = multiple lines 
    # delete original phone_service and multiple_lines variables
    df['phone_services'] = df.multiple_lines.replace({'No phone service': 0, 'No': 1, 'Yes': 2})
    df.drop(columns=['phone_service', 'multiple_lines'], inplace = True)    
    
    # Manually encode yes/no data to 0 = no, 1 - yes
    df['churn'] = df['churn'].replace({'No' : 0, 'Yes' : 1})
    df['partner'] = df['partner'].replace({'No' : 0, 'Yes' : 1})
    df['dependents'] = df['dependents'].replace({'No' : 0, 'Yes' : 1})
    df['paperless_billing'] = df['paperless_billing'].replace({'No': 0, 'Yes': 1})
    
    # Create new columns for partner/dependents combinations
    df['single'] = (df['partner'] == 0) & (df['dependents'] == 0)
    df['partner_no_dep'] = (df['partner'] == 1) & (df['dependents'] == 0)
    df['single_with_dep'] = (df['partner'] == 0) & (df['dependents'] == 1)
    df['family'] = (df['partner'] == 1) & (df['dependents'] == 1)
            
   # Create new columns for contract types 
    df['month_to_month'] = (df['contract_type_id'] == 1)
    df['one_year'] = (df['contract_type_id'] == 2) 
    df['two_year'] = (df['contract_type_id'] == 3) 
    df.drop(columns=['contract_type_id'], inplace = True)   
                   
   # Create new columns for payment types 
    df['e_Check'] = (df['payment_type_id'] == 1)
    df['check'] = (df['payment_type_id'] == 2) 
    df['auto_pay'] = (df['payment_type_id'] == 3) | (df['payment_type_id'] == 4)
    df.drop(columns=['payment_type_id'], inplace = True)   
    
    # Create new columns for internet service types 
    df['dsl'] = (df['internet_service_type_id'] == 1)
    df['fiber'] = (df['internet_service_type_id'] == 2) 
    df['no_internet'] = (df['internet_service_type_id'] == 3) 
    df.drop(columns=['internet_service_type_id'], inplace = True)  
                           
        
    # Manually encode yes/no/no service data to 0 = no (includes those with no service), 1 - yes
    df['tech_support'] = df.tech_support.replace({'No': 0, 'Yes': 1, 'No internet service': 0})
    df['online_security'] = df.online_security.replace({'No': 0, 'Yes': 1, 'No internet service': 0})
    df['online_backup'] = df.online_backup.replace({'No': 0, 'Yes': 1, 'No internet service': 0})
    df['device_protection'] = df.device_protection.replace({'No': 0, 'Yes': 1, 'No internet service': 0})
    
    return df



def train_validate_test_split(df, seed=123):
    
    '''
    This function splits the telco data into train, 
    validate and test data sets to use in classification
    modeling
    
    This split is stratified on 'churn'
    '''
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.churn
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.churn,
    )
    return train, validate, test

