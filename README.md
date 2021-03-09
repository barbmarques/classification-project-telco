### classification-project-telco
### Project Summary:

Telco customers are leaving for newer companies. Find a driver of the churn. A copy of the report will go to executives. Include enough documentation in your final notebook that someone could work through it without you.

Data Source: Telco database of 7043 customers, 24 features

### Goals:

- Find drivers for customer churn at Telco
- Construct a machine learning classification model that accurately predicts customer churn.


### Data Dictionary

|Variable | Definition | Data Type | Value Counts |
|
|churn|This is our target **variable** Indicates that a customer has cancelled servicer| object |


---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|**Target variable:** has_churned | Indicates whether customer has cancelled all services. | int64 |
|customer_id| Unique identifier for each customer | object |
|senior_citizen| Indicates whether customer's age is 65 or older | int64 |
|tenure_months|Length of customer's relationship with Telco in months | int64 |
paperless_billing|Indicates whether customer has selected paperless billing | int64 |
monthly_charges|The amount customer pays for services each month| float64 |
total_charges|The total amount customer has paid for Telco services throughout tenure| float64 | 
tenure_years|Lenth of customer's relationship with Telco in years| float64 |
phone_services|Indicates whether customer has a single phone line, multiple lines, or no phone service|  int64 |
gender_Female|Customer is female| uint8 |
gender_Male|Customer is male| uint8 |
streamer |Customer subscribes to streaming tv and/or movies | int 64 |
is_single_no_dep |Customer has no partner, no dependents | int64 |
has_partner_no_dep|Customer has partner, but no dependents| int64 |
is_single_with_dep|Customer has dependents, but no partner| int64 |
family|Customer has partner and dependents| int64 |
month_to_month|Customer has a month-to-month contract| int64 |
one-year|Customer has a one-year contract| int64 |
two-year|Customer has a two-year contract| int64 |
e-Check|Customer pays with electronic check| int64 |
sends_check|Customers pays by check through the mail| int64 |
has_auto_pay|Customer payment is auto-drafted or automatically charged to credit card |int64 |
dsl|Customer has dsl internet service| int64 |
fiber|Customer has fiber optic internet service| int64 |
no_internet|Customer has no internet service| int64 |
no_tech_support|Customer does not subscribe to tech support| int64 |
no_online_security|Customer does not subscribe to online security | int64 |
no_online_backup|Customer does not subscribe to online backup | int64 |
no_device_protection|Customer does not subscribe to device protection| int64 |



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


