# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:37:25 2024

@author: alexj
"""

#Purpose: Extract temperature, humidity data from weather database into CSV file
#Name: Alexander Jason Start
#Date: 04 Feb 2024
#   Run BuildWeatherDB.py to build weather database before running this program

import sqlite3

#convert Celsius temperature to Fahrenheit
def convertCtoF(tempC):
    return (tempC*9.0/5.0) + 32.0

#file names for database and output file
dbFile = "weather.db"
output_file_name='formatdata2.csv' #add 2 to file name for 2nd data set

#connect to and query weather database and 
conn = sqlite3.connect(dbFile)
#create cursor to execute SQL commands
cur = conn.cursor()
selectCmd = """ SELECT temperature, relativeHumidity FROM observations
                ORDER BY timestamp; """
cur.execute(selectCmd)
allRows = cur.fetchall()
#limit the number of rows output to half
rowCount = len(allRows)//2 # double slash does integer division
rows = allRows[rowCount:] #use [rowCount:] instead of [:rowCount] for 2nd data set

#write data to output file
with open(output_file_name,"w+") as outf:
    outf.write('Celsius,Fahrenheit,Humidity')
    outf.write('\n')
    for row in rows:
        tempC = row[0]
        if tempC is None:       #handle missing temperature value
            continue
        else:            
            tempF = convertCtoF(tempC)
            outf.write(str(tempC)+',')
            outf.write(str(tempF)+',')
        humidity = row[1]
        if humidity is None:   #handle missing humidity value
            outf.write('\n')
        else:
            outf.write(str(humidity)+'\n') #print data to file separated by commas
