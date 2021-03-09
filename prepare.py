import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def clean_telco(df):
    
    '''
    This function cleans data obtained from Codeup's Telco database by: 
        converting data types of categorical and continuous variables to ints/floats,
        removing duplicate rows and columns, combining columns, creating new features 
    '''
    
    #remove any duplicate rows
    df.drop_duplicates(inplace=True)
    
    # fill nans in total_charges - these eleven customers have tenure of 0, so it is
    # reasonable to replace nan with 0
    df.assign(total_charges=df.total_charges.fillna(0))
    
    # convert total_charges to float
    df.total_charges=pd.to_numeric(df.total_charges, errors='coerce').astype('float64')
    
    # remove duplicate or unnecessary information (already encoded in _id columns of the same names): 
    # Drop gender (exploration shows it's nearly evenly split and therefore not likely a driver of churn)
    df.drop(columns=['gender','internet_service_type', 'contract_type', 'payment_type'], inplace=True)
    
    # rename tenure to monthly tenure & create a column to represent tenure in years
    df=df.rename(columns={'tenure':'tenure_months'})
    df['tenure_years']=round(df.tenure_months / 12, 2)

    # Encode booleans
    # Create one variable 'phone_services' combining phone service and multiple lines
    # 0 = no phone service, 1 = one line, 2 = multiple lines 
    # delete original phone_service and multiple_lines variables
    df['phone_services']=df.multiple_lines.replace({'No phone service': 0, 'No': 1, 'Yes': 2})
    df.drop(columns=['phone_service', 'multiple_lines'], inplace=True)    
    
    # Creating dataframe of dummy variables for streaming_tv and streaming_movies
    df_dummies=pd.get_dummies(df[['streaming_tv', 'streaming_movies']], drop_first=False)

    # Adding dummies to our original dataframe
    df=pd.concat([df, df_dummies], axis=1)

    # Drop original streaming_tv, and streaming_movies columns
    dummycols=['streaming_tv', 'streaming_movies']
    df=df.drop(columns = dummycols, axis = 1)
    
    # combine two columns streaming_tv and streaming_movies
    df['not_streamer']=(((df['streaming_tv_Yes'] == 1) & (df['streaming_movies_Yes'] == 1)) | ((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1))) 
    
    # drop original columns that were combined
    df.drop(columns=['streaming_tv_No','streaming_tv_Yes','streaming_tv_No internet service','streaming_movies_No','streaming_movies_Yes','streaming_movies_No internet service'], inplace = True)
    
    # Manually encode yes/no data to 0 = no, 1 - yes
    df['has_churned'] = df['churn'].replace({'No' : 0, 'Yes' : 1})
    df['partner'] = df['partner'].replace({'No' : 0, 'Yes' : 1})
    df['dependents'] = df['dependents'].replace({'No' : 0, 'Yes' : 1})
    df['paperless_billing'] = df['paperless_billing'].replace({'No': 0, 'Yes': 1})
    df.drop(columns = ['churn'], inplace = True)
    
    # Create new columns for partner/dependents combinations & drop original columns
    df['is_single_no_dep'] = (df['partner'] == 0) & (df['dependents'] == 0)
    df['has_partner_no_dep'] = (df['partner'] == 1) & (df['dependents'] == 0)
    df['is_single_with_dep'] = (df['partner'] == 0) & (df['dependents'] == 1)
    df['family'] = (df['partner'] == 1) & (df['dependents'] == 1)
    df.drop(columns=['partner', 'dependents'], inplace = True)   
            
    # Create new columns for contract types 
    df['month_to_month'] = (df['contract_type_id'] == 1)
    df['one_year'] = (df['contract_type_id'] == 2) 
    df['two_year'] = (df['contract_type_id'] == 3) 
    df.drop(columns=['contract_type_id'], inplace=True)   
                   
   # Create new columns for payment types 
    df['e_Check'] = (df['payment_type_id'] == 1)
    df['sends_check'] = (df['payment_type_id'] == 2) 
    df['has_auto_pay'] = (df['payment_type_id'] == 3) | (df['payment_type_id'] == 4)
    df.drop(columns=['payment_type_id'], inplace = True)   
    
    # Create new columns for internet service types 
    df['dsl'] = (df['internet_service_type_id'] == 1)
    df['fiber'] = (df['internet_service_type_id'] == 2) 
    df['no_internet'] = (df['internet_service_type_id'] == 3) 
    df.drop(columns=['internet_service_type_id'], inplace = True)  
                                  
    # Manually encode yes/no/no service data to 0 = no (includes those with no service), 1 - yes
    df['no_tech_support'] = df.tech_support.replace({'No': 1, 'Yes': 0, 'No internet service': 0})
    df['no_online_security'] = df.online_security.replace({'No': 1, 'Yes': 0, 'No internet service': 0})
    df['no_online_backup'] = df.online_backup.replace({'No': 1, 'Yes': 0, 'No internet service': 0})
    df['no_device_protection'] = df.device_protection.replace({'No': 1, 'Yes': 0, 'No internet service': 0})
    
    # drop original columns that were encoded in the negative above
    df.drop(columns=['tech_support','online_security','online_backup','device_protection'], inplace = True)
    
    # Change bool columns to False: 0, True: 1
    u = df.select_dtypes(bool)
    df[u.columns] = u.astype(int)     

    return df



def train_validate_test_split(df, seed=123):
    
    '''
    This function splits the telco data into train, 
    validate and test data sets to use in classification
    modeling
    
    This split is stratified on 'has_churned'
    '''
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.has_churned
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.has_churned,
    )
    return train, validate, test

