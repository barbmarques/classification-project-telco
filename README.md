### classification-project-telco
This repository will store the exploratory notebook and deliverables for the Telco Classification Project.

### Project Summary:

Telco customers are leaving for newer companies. Especially phone customers. Find a driver of the churn. A copy of the report will go to executives. Include enough documentation in your final notebook that someone could work through it without you.

Database of 7043 customers, 24 features

### Goals:

- Find drivers for customer churn at Telco
- Construct a ML classification model that accurately predicts customer churn.


### Data Dictionary

|Variable | Definition | Data Type | Value Counts |
|
|churn|This is our target **variable** Indicates that a customer has cancelled servicer| object |


---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|payment\_type\_id | Indicates how a customer pays their bill each month | int64 |
|contract\_type\_id| Indicates which contract type a customer has | int64 |
|internet\_service\_type_id| Indicates what type of internet service a customer has | int64 |
|customer\_id|Alpha-numeric ID that identifies each customer| object |
gender|Gender of the customer| object |
senior_citizen|Indicates if the customer is 65 or older| int64 |
partner|If a customer is married| object | 
dependents|Indicates if a customer lives with dependents| object |
tenure|The length of a customers relationship with Telco™ measured in months|  int64 |
phone_service|If a customer has phone service| object |
multiple_lines|If a customer has multiple phone lines| object |
online_security|Indicates if a customer has online security add-on| object |
online_backup|Indicates if a customer has online backups add-on| object |
device_protection|Indicates if a customer has a protection plan for Telco™ devices| object |
tech_support|Indicates whether a customer has technical support add-on| object |
streaming_tv|Indicates if a customer uses internet to stream tv| object |
streaming_movies|Indicates if a customer uses internet to stream movies| object |
paperless_billing|Indicates if a customer is enrolled in paperless billing| object |
monthly_charges|The amount a customer pays each month for services with Telco™| object |
total_charges|The total amount a customer has paid for Telco™ services| object |
|internet\_service\_type|Indicates the type of internet service a customer has| object |
|contract_type|The type of contract a customer has| object |
|payment_type|How a customer pays their bill each month| object |




### Process/Pipeline:
https://trello.com/b/vOXbVcbl

- Create git repository
- Create Readme file
    - commit and push
- Create a column for tenure in years
- Create acquire.py
    - write sequel query to join tables and acquire data
    - create get_telco_data function
    - commit and push
- import pandas, acquire and use it to acquire in a pandas dataframe
    - import env.py
    - run get_telco_data function  
- review data summary information and begin to compile a data dictionary of data types
- create data dictionary of all features
- plot distributions of individual variables
- Documented takeaways for data prep
- create prepare.py to clean, tidy and split data into train, validate, test


