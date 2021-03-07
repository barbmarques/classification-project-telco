### classification-project-telco
This repository will store the exploratory notebook and deliverables for the Telco Classification Project.

### Project Summary:

Telco customers are leaving for newer companies. Especially phone customers. Find a driver of the churn. A copy of the report will go to executives. Include enough documentation in your final notebook that someone could work through it without you.

Database of 7043 customers, 24 features

### Goals:

- Find drivers for customer churn at Telco
- Construct a ML classification model that accurately predicts customer churn.

###Insert Data Dictionary Here



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


