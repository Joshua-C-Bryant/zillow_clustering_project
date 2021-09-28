# Zillow Clustering Project

Our goal for this project was to find drivers of logerror in Zillow's Zestimate to better predict housing prices. To do this, we were to use Machine Learning models with clustering and regression algorhithms. 

# Executive Summary


- I was not able to make use of clusters for my model
- My top features used ended up being: bedroomcnt, buildingqualitytypeid, and longitude based on a mix of features chosen by RFE and heatmap correlation
- My top model was LinearRegression (OLS)
    - Train and Validate beat the mean baseline
    - However, Test was slightly above
    - Could be because of overfitting due to my hyperparameters
- Conclusion: While my model was able to beat my baseline on Train and Validate, it was not able to beat it on test data
    - With more time: I would like to dig into clustering more and spend more time with different combinations
    - While my model ultimately did not beat the baseline in my test, I do think these features should be looked into more and with more time, could be engineered better to predict unseen data


# Table of Contents


- [Project Title](#Zillow-Clustering-Project)
- [Executive Summary](#Executive-Summary)
- [Initial Hypothesis](#Initial-Hypothesis)
- [Deliverables](#Deliverables)
- [Data Dictionary](#Data-Dictionary)
- [Project Planning](#Project-Planning)
- [Instructions for Reproducing](#Instructions-for-Reproducing)

# Initial Hypothesis
[(Back to top)](#table-of-contents)
- Hypothesis 1: Is logerror significantly different for properties in LA Country vs Orange County vs Ventura County?
- Hypothesis 2: Is logerror significantly different for properties in Orange County vs the rest of the population of homes?
- Hypothesis 3: Is there a correlation between square feet and logerror?
- Hypothesis 4: Is there a correlation between logerror and yearbuilt?
- Hypothesis 5: Is there a correlation between longitude and logerror?
- Hypothesis 6: Is there a correlation between buildingqualitytypeid and logerror?


<!-- This is where you can let people know how they can **contribute** to your project. Some of the ways are given below.

Also this shows how you can add subsections within a section. -->

# Deliverables
[(Back to top)](#table-of-contents)

[Trello Board](https://trello.com/b/4KbEEgOS)


# Data Dictionary
[(Back to top)](#table-of-contents)

| Feature                    | Datatype                | Definition   |
|:---------------------------|:------------------------|:-------------|
| parcelid                   | 69523 non-null: int64   |individual id for unique properties|
| bathroomcnt                | 69523 non-null: float64 |# of bathrooms a property has|
| bedroomcnt                 | 69523 non-null: float64 |# of bedrooms a property has|
| buildingqualitytypeid      | 69523 non-null: float64 |quality of the building on a scale from 1 to 12|
| calculatedfinishedsquarefeet|69523 non-null: float64 |calculated square footage of home|
| fips                       | 69523 non-null: float64 |county code|
| latitude                   | 69523 non-null: float64 |where the porperty is located in refrence to latitude|
| longitude                  | 69523 non-null: float64 |where the porperty is located in refrence to  longitude|
| lotsizesquarefeet          | 69523 non-null: float64 |the square footage of the land the propety resides on|
| regionidcity               | 69523 non-null: object  |unique identifier for cities the property is in|
| regionidzip                | 69523 non-null: object  |uniques identifier for the zip code the propert resides in|
| year_built                 | 69523 non-null: float64 |year the property was built|
| structuretaxvaluedollarcnt | 69523 non-null: float64 |the estimated tax value of the property itself|
| tax_value                  | 69523 non-null: float64 |the estimated tax value of the property|
| landtaxvaluedollarcnt      | 69523 non-null: float64 |the estimated tax value of the land the property is on|
| tax_amount                 | 69523 non-null: float64 |How much the owner of the property must pay this year|
| logerror                   | 69523 non-null: float64 |The target of this project (error produced in predictions)|
| transactiondate            | 69523 non-null: object  |Date property was sold|
| propertylandusedesc        | 69523 non-null: object  |What the property is listed as ex.(Single family)|
| county                     | 69523 non-null: object  |The county the resident resides in|


# Project Planning
[(Back to top)](#table-of-contents)

- Acquire Data from Zillow set in Codeup Database
    - Target homes were Single Family Residential
- Prepare Data
    - checking for duplicates, nulls, dropping unnecessary columns
    - feature engineering
    - scale the data
    - removed outliers using IQR
        - I mainly removed outliers based on the size of the home
        - I did not consider tax value outliers as needing to be dropped
- Explore the data
    - hypothesis testing
    - visualizations
- Clustering
    - created 3 clusters
        - longitude and square footage
        - building quality and year built
        - taxvalue and bedroom count
- Modeling
    - created 4 models to predict logerror
    - LinearRegression (OLS)
    - LassoLars
    - Tweedie Regressor
    - Polynomial Regression
- Evaluation
    - I used my LinearRegression (OLS) model
        - baseline RMSE on validate: 0.16099	
        - RMSE for OLS using LinearRegression
        - Training/In-Sample:  0.16087 
        - Validation/Out-of-Sample:  0.16091 
        - Test/Out-of-Sample:  0.16861



# Instructions for Reproducing
[(Back to top)](#table-of-contents)

You will need this repository and access to Codeup's Zillow data set to be able to recreate this project.
All functions are available in my prepare.py and explore.py scripts

