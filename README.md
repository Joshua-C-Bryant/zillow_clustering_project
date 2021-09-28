<!-- Add banner here -->

# Zillow Clustering Project

<!-- Add buttons here -->

<!-- Describe your project in brief -->
Our goal for this project was to find drivers of logerror in Zillow's Zestimate to better predict housing prices. To do this, we were to use Machine Learning models with clustering and regression algorhithms. 

# Executive Summary

<!-- Add a demo for your project -->

- I was not able to make use of clusters for my model
- My top features used ended up being: bedroomcnt, buildingqualitytypeid, and longitude based on a mix of features chosen by RFE and heatmap correlation
- My top model was LinearRegression (OLS)
    - Train and Validate beat the mean baseline
    - However, Test was slightly above
    - Could be because of overfitting due to my hyperparameters
- Conclusion: While my model was able to beat my baseline on Train and Validate, it was not able to beat it on test data
    - With more time: I would like to dig into clustering more and spend more time with different combinations
    - While my model ultimately did not beat the baseline in my test, I do think these features should be looked into more and with more time, could be engineered better to predict unseen data


<!-- After you have written about your project, it is a good idea to have a demo/preview(**video/gif/screenshots** are good options) of your project so that people can know what to expect in your project. You could also add the demo in the previous section with the product description.

Here is a random GIF as a placeholder.

![Random GIF](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif) -->

# Table of Contents


- [Project Title](#Zillow-Clustering-Project)
- [Executive Summary](#demo-preview)
- [Project Description and Goals](#table-of-contents)
- [Initial Hypothesis](#contribute)
- [Deliverables](#installation)
- [Data Dictionary](#usage)
- [Project Planning](#development)
- [Instructions for Reproducing](#license)

# Initial Hypothesis
[(Back to top)](#table-of-contents)

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

<!-- Adding the license to README is a good practice so that people can easily refer to it.

Make sure you have added a LICENSE file in your project folder. **Shortcut:** Click add new file in your root of your repo in GitHub > Set file name to LICENSE > GitHub shows LICENSE templates > Choose the one that best suits your project!

I personally add the name of the license and provide a link to it like below. -->

