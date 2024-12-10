# -*- coding: utf-8 -*-
"""PDS_OEP (2).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VtGvqqd7XKHHsynPsWHk9eRnFgr71IRE
"""

#Importing neccessary lib...

import numpy as np
import pandas as pd

# Loading the dataset

loan_train = pd.read_csv('loan-train.csv')
loan_test = pd.read_csv('loan-test.csv')

# Displaying the train DataSet

loan_train

"""# Preprocessing the Data Set"""

# Displaying total No of Rows

print("Number of rows: ",len(loan_train))

# Displaying total No of Columns

print("Number of columns: ",len(loan_train.columns))

# Displaying Shape of the DataSet

print("Shape: ",loan_train.shape)

# Info of the dataset

loan_train.info()

conert_dict={
    'ApplicantIncome': np.float16,
    'CoapplicantIncome': np.float16 ,
    'LoanAmount' : np.float16 ,
    'Loan_Amount_Term' : np.float16 ,
    'Credit_History'  : np.float16
}
loan_train=loan_train.astype(conert_dict)
loan_train.info()

# Describing the DataSet

loan_train.describe()

# Now We will Explore Feature having Object Data Type

def explore_object(data,feature):

    if(data[feature].dtype == 'object'):

        print(data[feature].value_counts())
        print()

col=[col for col in loan_train.columns]
for col in col:
    explore_object(loan_train,col)

# list of how many null values are present per column

loan_train.isna().sum()

# Finding outliers in LoanAmount and Credit_History
# importing seaborn for data visualization

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(4,4))
sns.boxplot(data=loan_train,y='LoanAmount')
plt.title('Box Plot for LoanAmount')
plt.show()

loan_train.drop_duplicates(inplace=True)

"""# Exploratory Data Analysis"""

loan_train['LoanAmount'].describe()

# Finding lower and upper limits
q1,q3=loan_train['LoanAmount'].quantile(0.25),loan_train['LoanAmount'].quantile(0.75)
iqr=q3-q1
lower_limit,higher_limit=q1-(1.5*iqr),q3+(1.5*iqr)
lower_limit,higher_limit

# Now Removing Outliers

loan_train=loan_train[loan_train['LoanAmount']<higher_limit]
loan_train

# Finding outliers in LoanAmount and Credit_History
# importing seaborn for data visualization

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(4,4))
sns.boxplot(data=loan_train,y='LoanAmount')
plt.title('Box Plot for LoanAmount')
plt.show()

# Finding outliers in LoanAmount and Credit_History

plt.figure(figsize=(4,4))
sns.boxplot(data=loan_train,y='Credit_History')
plt.title('Box Plot for Credit_History')
plt.show()

loan_train['Credit_History'].describe()

mean_loan_amount = loan_train['LoanAmount'].mean()
mean_loan_amount

loan_train.loc[:,'LoanAmount']

# We need to fill null values of Numerical Data with mean and mode


mode_credit_history = loan_train.loc[:,'Credit_History'].mode()
loan_train.loc[:,'Credit_History'] = loan_train.loc[:,'Credit_History'].fillna(mode_credit_history.values[0]) #Mode

mode_credit_history = loan_test.loc[:,'Credit_History'].mode()
loan_test.loc[:,'Credit_History'] = loan_test.loc[:,'Credit_History'].fillna(mode_credit_history.values[0])   #Mode


mode_loan_term = loan_train.loc[:,'Loan_Amount_Term'].mode()
loan_train.loc[:,'Loan_Amount_Term'] = loan_train.loc[:,'Loan_Amount_Term'].fillna(mode_loan_term.values[0])   #Mode

mode_loan_term = loan_test.loc[:,'Loan_Amount_Term'].mode()
loan_test.loc[:,'Loan_Amount_Term'] = loan_test.loc[:,'Loan_Amount_Term'].fillna(mode_loan_term.values[0])   #Mode


mean_loan_amount = loan_train.loc[:,'LoanAmount'].mean()
loan_train.loc[:,'LoanAmount'] = loan_train.loc[:,'LoanAmount'].fillna(mean_loan_amount)   #Mean

mean_loan_amount = loan_test.loc[:,'LoanAmount'].mean()
loan_test.loc[:,'LoanAmount'] = loan_test.loc[:,'LoanAmount'].fillna(mean_loan_amount)   #Mean

# After Replacing

loan_train.isna().sum()

# We need to fill null values of Catagorical Data with mode

mode_gender = loan_train.loc[:,'Gender'].mode()
loan_train.loc[:,'Gender'] = loan_train.loc[:,'Gender'].fillna(mode_gender.values[0])   #Mode

mode_gender = loan_test.loc[:,'Gender'].mode()
loan_test.loc[:,'Gender'] = loan_test.loc[:,'Gender'].fillna(mode_gender.values[0])   #Mode



mode_married = loan_train.loc[:,'Married'].mode()
loan_train.loc[:,'Married'] = loan_train.loc[:,'Married'].fillna(mode_married.values[0])   #Mode

mode_married = loan_test.loc[:,'Married'].mode()
loan_test.loc[:,'Married'] = loan_test.loc[:,'Married'].fillna(mode_married.values[0])   #Mode



mode_dependents = loan_train.loc[:,'Dependents'].mode()
loan_train.loc[:,'Dependents'] = loan_train.loc[:,'Dependents'].fillna(mode_dependents.values[0])   #Mode

mode_dependents = loan_test.loc[:,'Dependents'].mode()
loan_test.loc[:,'Dependents'] = loan_test.loc[:,'Dependents'].fillna(mode_dependents.values[0])   #Mode



mode_self_employed = loan_train.loc[:,'Self_Employed'].mode()
loan_train.loc[:,'Self_Employed'] = loan_train.loc[:,'Self_Employed'].fillna(mode_self_employed.values[0])   #Mode

mode_self_employed = loan_test.loc[:,'Self_Employed'].mode()
loan_test.loc[:,'Self_Employed'] = loan_test.loc[:,'Self_Employed'].fillna(mode_self_employed.values[0])   #Mode

# After Replacing

loan_train.isna().sum()

# Converting categorical variable into numerical variables
# Importing LabelEncoder

# from sklearn.preprocessing import LabelEncoder
# feature_col = [col for col in loan_train.columns if loan_train.loc[:,col].dtype=='object']

# le = LabelEncoder()
# for col in feature_col:
#     loan_train.loc[:,col] = le.fit_transform(loan_train.loc[:,col])
#     if(col!='Loan_Status'):
#         loan_test.loc[:,col] = le.fit_transform(loan_test.loc[:,col])

loan_train.head()

# Removing Unnecessary Features

loan_train = loan_train.drop('Loan_ID',axis=1)
loan_train

"""# Data Visualizations"""

# Importing necessary libraries..
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('dark')

#Normalization of ApplicantIncome to remove skweness
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)


sns.histplot(loan_train['ApplicantIncome'],bins=15,kde=True)
plt.title("Applicant Income ")

plt.subplot(1, 2, 2)
plt.grid()
loan_train['ApplicantIncome']=np.log(loan_train['ApplicantIncome'])
sns.histplot(loan_train['ApplicantIncome'],bins=15,kde=True)
plt.title("Log Application Income ")

plt.show()

#Normalization of LoanAmount to remove skweness
plt.figure(figsize=(18, 6))
plt.subplot(1, 2, 1)


sns.histplot(loan_train['LoanAmount'],bins=15,kde=True)
plt.title("Loan Amount ")

plt.subplot(1, 2, 2)
plt.grid()
loan_train['LoanAmount']=np.log(loan_train['LoanAmount'])
sns.histplot(loan_train['LoanAmount'],bins=15,kde=True)
plt.title(" LoanAmount ")

plt.show()

#Normalization of CoapplicantIncome to remove skweness
plt.figure(figsize=(18, 6))
plt.subplot(1, 2, 1)


sns.histplot(loan_train['CoapplicantIncome'],bins=15,kde=True)
plt.title("CoapplicantIncome ")

plt.subplot(1, 2, 2)
plt.grid()
sns.histplot(np.log(loan_train['CoapplicantIncome']),bins=15,kde=True)
plt.title("Log CoapplicantIncome ")

plt.show()

numeric_col=[ col for col in loan_train.columns if loan_train[col].dtype != 'object']
new = loan_train.loc[:,numeric_col]
plt.figure(figsize=(4,4))
sns.heatmap(new.corr(), cmap='coolwarm', annot=True, fmt='.1f', linewidths=.1)
plt.show()

print('Covariance of the numeric Columns is:- ')
new.cov()

loan_train.boxplot(column= 'ApplicantIncome', by='Education')
plt.tight_layout()

"""# Split into Train and Test"""

X = loan_train.iloc[:,:-1]
y = loan_train['Loan_Status']

X = pd.get_dummies(X)
loan_train = pd.get_dummies(loan_train)
loan_test = pd.get_dummies(loan_test)

# Splitting the data set into train and test data

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

"""# Choose ML Model."""

X_train.columns

np.isfinite(X_train)

X_train.head()

X_train.info()

"""# Model-1"""

from sklearn.ensemble import RandomForestClassifier

model_1 = RandomForestClassifier(n_estimators=500)
model_1.fit(X_train,y_train)

model_1_prediction=model_1.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
print(classification_report(y_test, model_1_prediction))

cm = confusion_matrix(y_test, model_1_prediction)
print(cm)

print(accuracy_score(y_test, model_1_prediction))

model_2 = RandomForestClassifier(n_estimators=100)
model_2.fit(X_train,y_train)

model_2_prediction=model_2.predict(X_test)

print(classification_report(y_test, model_2_prediction))

cm = confusion_matrix(y_test, model_2_prediction)
print(cm)

print(accuracy_score(y_test, model_2_prediction))

model_3 = RandomForestClassifier(n_estimators=1000)
model_3.fit(X_train,y_train)

model_3_prediction=model_3.predict(X_test)

print(classification_report(y_test,model_3_prediction))

cm = confusion_matrix(y_test, model_3_prediction)
print(cm)

print(accuracy_score(y_test, model_3_prediction))

"""# Model-2"""

from sklearn import svm

model_4=svm.SVC(kernel='linear')
model_4.fit(X_train,y_train)

model_4_prediction=model_4.predict(X_test)
print(classification_report(y_test,model_4_prediction))

cm = confusion_matrix(y_test, model_4_prediction)
print(cm)

print(accuracy_score(y_test, model_4_prediction))

model_5=svm.SVC(kernel='rbf')
model_5.fit(X_train,y_train)

model_5_prediction=model_5.predict(X_test)
print(classification_report(y_test,model_5_prediction))

cm = confusion_matrix(y_test, model_5_prediction)
print(cm)

print(accuracy_score(y_test, model_5_prediction))

model_6=svm.SVC(kernel='sigmoid')
model_6.fit(X_train,y_train)

model_6_prediction=model_6.predict(X_test)
print(classification_report(y_test,model_6_prediction))

cm = confusion_matrix(y_test, model_6_prediction)
print(cm)

print(accuracy_score(y_test, model_6_prediction))

"""# model-3"""

from sklearn.naive_bayes import GaussianNB
model_7=GaussianNB()
model_7.fit(X_train,y_train)

model_7_prediction=model_7.predict(X_test)
print(classification_report(y_test,model_7_prediction))

cm = confusion_matrix(y_test, model_7_prediction)
print(cm)

print(accuracy_score(y_test, model_7_prediction))

"""# model-4"""

import math
k=int(math.sqrt(len(X_train)))

from sklearn.neighbors import KNeighborsClassifier
model_8=KNeighborsClassifier(n_neighbors=k)
model_8.fit(X_train,y_train)

model_8_prediction=model_8.predict(X_test)
print(classification_report(y_test,model_8_prediction))

cm = confusion_matrix(y_test, model_8_prediction)
print(cm)

print(accuracy_score(y_test, model_8_prediction))

y=[0.801,0.792,0.801,0.828,0.684,0.684,0.315,0.693]
x=['model1','model2','model3','model4','model5','model6','model7','model8']
plt.plot(x,y)
plt.ylabel('Accuracy')
plt.xlabel('Model')
plt.show()

pre=[0.79,0.79,0.79,0.80,0.68,0.71,0.00,0.69]
plt.plot(pre,y)
plt.ylabel('Accuracy')
plt.xlabel('precision')
plt.show()

recall=[0.96,
0.95,
0.96 ,
1.00  ,
1.00,
0.92,
0.00,
0.99

]
plt.plot(recall,y)
plt.ylabel('Accuracy')
plt.xlabel('Recall')
plt.show()

f1_Y=[0.87,
0.86,
0.87,
0.89,
0.81,
0.80,
0.00,
0.82]
f1_N=[0.59,
0.58,
0.59 ,
0.63  ,
0.00,
0.26,
0.48,
0.11

]
plt.plot(f1_Y,y)
plt.ylabel('Accuracy')
plt.xlabel('F1-score')
plt.show()