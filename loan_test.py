# Load the libraries
import pandas as pd
import pytest


# Load the data
df = pd.read_csv("train.csv")

# Test to check the column names and their sequence are same as expected
def test_NoColumns():
    assert (list(df.columns)) == ['Loan_ID','Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area','Loan_Status']

# Test to check if the Gender has only Male or Female
def test_Gender():
    assert df['Gender'].unique().tolist() == ['Male', 'Female']

#Test for checking if the Married columns has only two values either Yes or No
def test_Married():
    assert df['Married'].unique().tolist() == ['Yes','No']


# Test for checking if Applicant Income is less than zero
def test_ApplicantIncome():
    assert df[df['ApplicantIncome'] < 0].shape[0]  == 0


#Test for checking if the Married columns has only two values either Male or Female
def test_PropertyArea():
    assert df['Property_Area'].unique().tolist() == ['Rural','Urban','Semiurban']


# Test for checking if Loan Amount is more than 500
def test_LoanAmount():
    assert df[df['LoanAmount'] > 600].shape[0]  == 0