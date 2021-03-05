import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_telco_data():
    return pd.read_sql(telco_sql, get_connection('telco_churn'))


telco_sql = "SELECT * FROM customers JOIN internet_service_types ON(customers.internet_service_type_id=internet_service_types.internet_service_type_id) JOIN contract_types ON(customers.contract_type_id=contract_types.contract_type_id) JOIN payment_types ON(customers.payment_type_id=payment_types.payment_type_id)"

