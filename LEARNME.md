<<<<<<< HEAD
import os

import pandas as pd
import numpy as pd
import mysql.connector 
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
username = os.getenv('USER')
password = os.getenv('PASWORD')

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

def shoeTables():
query = """SHOW TABLES;"""
cursor.execute(query)
rows = cursor.fetchall()
df = pd.DataFrame(data=rows,columns=cursor.column_names)
retrun df

def describeTable(tablename):
query = f"""describe {tablename};"""
cursor.execute(query)
rows = cursor.fetchall()
df = pd.DataFrame(data=rows,columns=cursor_names)
return df

=======
 # E-Commerce Sales Data Analysis

 ## Prepare the Sales Data:
* "Year" and "Sales"
  
|Year|Sales|
|----|------|
|2018 | 50000 |
|2019 | 60000 |
|2020 | 55000 |
|2021 | 70000 |
|2022 | 75000 |

The followung code does this....
```python
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

# Annual Sales Performence and Review
fig.write_html('annual_sales_performance.html')
```

![Image](https://cdn4.vectorstock.com/i/1000x1000/83/73/happy-new-year-sale-promotion-background-design-vector-22948373.jpg)
>>>>>>> 1ed44a7229cbedd83bb3765291cb629f7a385909
>>>>>>>
# Annual Sales Performence and Review
## Table of Contents
