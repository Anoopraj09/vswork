import os

import pandas as pd 
import mysql.connector 
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
username = os.getenv('USER')
password = os.getenv('PASSWORD')

connection = mysql.connector.connect(host=host,
                                     user=username,
                                     password=password,
                                     database='swiftmarket')

cursor = connection.cursor()

def queryToDataFrame(query):

    cursor. execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df

def showTables():
    query = """SHOW TABLES;"""
    cursor. execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df

def DescribeTable(tablename):
    query = f"""DESCRIBE {tablename};"""
    cursor. execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df

import pandas as pd
import plotly.express as px

# Create the sales data DataFrame
data = pd.DataFrame({
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Sales": [50000, 60000, 55000, 70000, 75000]
})

# Create the line chart
fig = px.line(data, x='Year', y='Sales', title='Annual Sales Performance Over Time')

# Show the figure
fig.show()

# Optionally, save the figure to an HTML file
fig.write_html('annual_sales_performance.html')

