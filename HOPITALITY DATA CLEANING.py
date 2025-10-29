# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 12:37:25 2025

@author: Dhruv Kaushik
"""
import pandas as pd
import numpy as np

# --- LOADING THE CSV FILE --- #

df = pd.read_csv(r"C:\Users\DELL\Desktop\data sets\HOSPITALITY\hotel_bookings.csv")
print(df)

# --- Removing Duplicates if any ---#

df.drop_duplicates()

# --- Filling of missing values with replacing nan with zero --- #

df["agent"] = np.where(df["agent"].isnull(),0, df["agent"])
df["company"] = np.where(df["company"].isnull(), 0 , df["company"])

# --- fixing datatype ---- #

numric_cols = ['lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights', 
                'adults', 'children', 'babies', 'adr']
for col in numric_cols:
    pd.to_numeric(df[col],errors= 'coerce')
    
# --- converting all arvival data into single date column --- #

df["arrival_date"] = pd.to_datetime(df["arrival_date_year"].astype(str)+ '-' +
   df["arrival_date_month"]+ '-' + df["arrival_date_day_of_month"].astype(str),errors='coerce')

# --- Small cahnges for performing dax function --- #
df["booking status"] = np.where(df["is_canceled"] ==1 ,'Canceled','Not Canceled')

# Create Columns Total Nights and Total Guest to perform dax
df['Total Nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
df['Total Guests'] = df['adults'] + df['children'] + df['babies']

# Create the Booking Value (Estimated Revenue) column
df['Booking Value (INR)'] = df['adr'] *( df['Total Nights'] + df['Total Guests'])

# --- saving Cleaned Data Set --- #
df.to_csv( r"C:\Users\DELL\Desktop\data sets\HOSPITALITY\Cleaned Hotel_booking.csv" , index = False)
print("Saved your Cleaned file to Folder HOSPITALITY!!")




























