import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE, SelectKBest, f_regression
from sklearn.linear_model import LinearRegression, TweedieRegressor, LassoLars

def zillow_split(df, target):
    '''
    This function take in the zillow dataframe and performs a train, validate, test split
    Returns train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test as partitions
    and prints out the shape of train, validate, test
    '''
    #create train_validate and test datasets
    train, test = train_test_split(df, train_size = 0.8, random_state = 123)
    #create train and validate datasets
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123)

    #Split into X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]

    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]

    X_test = test.drop(columns=[target])
    y_test = test[target]
   
    return X_train, X_validate, X_test, y_train, y_validate, y_test

def min_max_scaler(X_train, X_validate, X_test, numeric_cols):
    """
    this function takes in 3 dataframes with the same columns,
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler.
    it returns 3 dataframes with the same column names and scaled values.
    """
    # create the scaler object and fit it to X_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).
    scaler = MinMaxScaler(copy=True).fit(X_train[numeric_cols])
    # scale X_train, X_validate, X_test using the mins and maxes stored in the scaler derived from X_train.
    X_train_scaled_array = scaler.transform(X_train[numeric_cols])
    X_validate_scaled_array = scaler.transform(X_validate[numeric_cols])
    X_test_scaled_array = scaler.transform(X_test[numeric_cols])
    # convert arrays to dataframes
    X_train_scaled = pd.DataFrame(X_train_scaled_array, columns=numeric_cols).set_index(
        [X_train.index.values]
    )
    X_validate_scaled = pd.DataFrame(
        X_validate_scaled_array, columns=numeric_cols
    ).set_index([X_validate.index.values])
    X_test_scaled = pd.DataFrame(X_test_scaled_array, columns=numeric_cols).set_index(
        [X_test.index.values]
    )
    # Overwriting columns in our input dataframes for simplicity
    for i in numeric_cols:
        X_train[i] = X_train_scaled[i]
        X_validate[i] = X_validate_scaled[i]
        X_test[i] = X_test_scaled[i]
    return X_train, X_validate, X_test

def rfe(X, y, n):
    '''
    This function takes an X, Y and n (number of features)
    and outputs the regressive feature engineering to show most valuable features
    '''
    lm = LinearRegression()
    rfe = RFE(lm, n)
    rfe.fit(X, y)
    
    n_features = X.columns[rfe.support_]
    
    return n_features

def select_kbest(X,y,k): 
    '''
    This function takes an X, Y and n (number of features)
    and outputs the most valuable features by using SelectKBest
    '''
    f_selector = SelectKBest(f_regression, k)
    f_selector.fit(X, y)
    k_features = X.columns[f_selector.get_support()]

    return k_features

def simple_mm_scale(df, X_train):
    '''
    This function uses minmax_scale(df, X_train)
    Takes in the dataframe and applies a minmax scaler to it. 
    Outputs a scaled dataframe.  
    '''
    scaler = MinMaxScaler().fit(X_train)
    x_scaled = scaler.transform(data_set)
    x_scaled = pd.DataFrame(x_scaled)
    x_scaled.columns = data_set.columns
    return x_scaled

    scaler = MinMaxScaler(copy=True).fit(X_train[numeric_cols])

    # scale X_train, X_validate, X_test using MinMax Scaler from X_train.
    X_train_scaled_array = scaler.transform(X_train[numeric_cols])
    X_validate_scaled_array = scaler.transform(X_validate[numeric_cols])
    X_test_scaled_array = scaler.transform(X_test[numeric_cols])