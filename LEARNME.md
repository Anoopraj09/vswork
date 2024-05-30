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
fig.write_html('annual_sales_performance.html')
```
