# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:02:32 2020

@author: Rahul1582
"""


import pandas as pd

data_ex=pd.ExcelFile(r"C:\Users\Rahul1582\Desktop\Excel Automation\Book1.xlsx")

sheet=pd.read_excel(data_ex)

# print(sheet)

df=sheet

print(df.shape)

val = input(" Type the column name you want to filter:-") 

#print(val) 

print(df[df[val]==1])

sheet1=df[df[val]==1]

sheet1.to_excel(r"C:\Users\Rahul1582\Desktop\Excel Automation\filtered.xlsx")

print("File saved successfully")