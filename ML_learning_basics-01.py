import pandas as pd
Data=pd.read_csv('car_data.csv')
#print(Data.head())

'''To take an unique data of specified column in the csv file'''
Unique_data=Data['Gender'].unique()
print(Unique_data)

'''To know the Number of the unique data of specified column in the csv file'''
Number_of_uniquedata=Data['Gender'].nunique()
print(Number_of_uniquedata)

'''To convert object into numbers of the specified column in the given csv file for system knowledge using map() function'''
#Data['Gender']=Data['Gender'].map({'Male':0,'Female':1})
#print(Data)

'''To convert automatically object into numbers of the specified column in the given csv file for system knowledge using LabelEncoder() function'''
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
#Data['Gender']=le.fit_transform(Data['Gender'])
#print(Data)

'''To find total count of catagoris in the specified column respectively using value_counts() function'''
Total_count_in_category_wise=Data['Gender'].value_counts()
print(Total_count_in_category_wise)

'''To find total count of categoris in the multiple column respectively using value_counts() function'''
# Total_count_in_categery_wise=Data[['Gender','Purchased']].value_counts()
# #print(Total_count_in_catagery_wise)

'''To find total count of specified column using count() function'''
Total_count_inthecolumn=Data[['User ID','Gender']].count()
print(Total_count_inthecolumn)

'''To automatically map the entire data of the column in the given csv file to another or new file'''
# Data['Gender']=le.fit_transform(Data['Gender'])
# Data.to_csv('Meena.csv')

'''To get dummy columns using get_dummies() function'''
# Data=pd.get_dummies(Data,columns=['Gender'])
# print(Data.head())
    
