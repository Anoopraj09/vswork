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

import pandas as pd
import plotly.express as px

# Load the data
url = 'https://raw.githubusercontent.com/your-username/sales-performance/main/sales_data.csv'
data = pd.read_csv(url)

Create the line chart
fig = px.line(data, x='Year', y='Sales', title='Annual Sales Performance Over Time')

Save the figure to an HTML file
fig.write_html('annual_sales_performance.html')

