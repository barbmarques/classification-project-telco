### classification-project-telco
#### Project Summary:

Telco is concerned about its significant customer attrition rate and has asked Codeup's Data Science team to identify drivers of churn. To do this, we created a machine learning model which predicts future customer churn as accurately as possible. 

Data Source: Telco's database of 7043 customers, including 24 attributes.

#### Project Goals:
- Find drivers for customer churn at Telco
- Construct a ML classification model that accurately predicts customer churn. 

#### Using a Random Forest Model, we identified the following predictors of churn:
- lack of tech support
- month-to-month contracts
- non-enrollment in auto-pay
- fiber optic internet 
- not subscribing to streaming movies and/or tv

#### Our analysis revealed that number of factors are contributing to churn:
- Customer does not receive technical support
- Customer does not participate in auto-pay
- Customer does not subscribe to streaming services
- Customer is on a month-to-month contract
- Customer has fiber optic internet

#### Our recommendations to reduce churn include:
- Offering reduced prices on tech support for internet customers.
- Offer packages for streaming movies and tv
- Encourage customers to participate in some form of automatic payment (bank draft or credit card).
- Incentivize 1- and 2-year contracts

To view the prediction and probability of churn for each Telco customer in our test data, download ```churn_probability.csv```. 

All files referenced in this presentation are available in the github repository for this project:   https://github.com/barbmarques/classification-project-telco.


#### Process/Data Science Pipeline:
Each step in the our process is recorded and staged on a Trello board at: https://trello.com/b/vOXbVcbl


#### Instructions for Reproducing Our Findings:

1.  Download the following files from https://github.com/barbmarques/classification-project-telco to your working directory:  
 - explore.py
 - prepare.py
 - acquire.py
 - logistic_regression_util.py
 - Final_Notebook.ipynb
 - churn_probability.csv
 

2.  You will also need you a copy of your personal env file in your working directory:
 - This should contain your access information (host, user, password) to access Codeup's database in MySQL

3. Run the Jupyter notebook, cell by cell, allowing time for visualizations to generate.

4. To access the prediction and probability of churn for each Telco customer in our test data in a csv format, download ```churn_probability.csv```. 


#### Data Dictionary of Variables Used in Our Analysis

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
not_streamer |Customer subscribes to streaming tv and/or movies | int 64 |
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



