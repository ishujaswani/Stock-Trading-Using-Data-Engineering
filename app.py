from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, input_file_name, substring_index
import os
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.subplots as sp
import os

# set the working directory
os.chdir('/Users/ishujaswani/Downloads/Columbia_Courses/spring_23/Managing_Data/Flask_app')


app = Flask(__name__,
            template_folder='templates',
            static_url_path='/static') 

spark = SparkSession \
    .builder \
    .appName("Traders App") \
    .config("spark.cores.max", "4") \
    .config('spark.executor.memory', '8G') \
    .config('spark.driver.maxResultSize', '8g') \
    .config('spark.kryoserializer.buffer.max', '512m') \
    .config("spark.driver.cores", "4") \
    .getOrCreate()

sc = spark.sparkContext

# Read all CSV files in a folder and add a column for the file name (ticker)
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Users/ishujaswani/Downloads/archive/Data/StockHistory/*") \
    .withColumn("ticker", substring_index(split(input_file_name(), "History/")[1], ".csv", 1)) # assuming the ticker is everything between "History/" and ".csv"

for c in df.columns:
    new_name = c.replace(".", "_")
    df = df.withColumnRenamed(c, new_name)
# Define a list of columns to be cast as integers
cols_to_cast = [col for col in df.columns if col not in ['Date', 'ticker']]

# Use a for loop to cast the columns to integers
for col in cols_to_cast:
    df = df.withColumn(col, df[col].cast('integer'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input and filter DataFrame
        ticker = request.form['ticker']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        filtered_df = df.filter((df.ticker == ticker) & (df.Date >= start_date) & (df.Date <= end_date))

        # Convert filtered PySpark DataFrame to Pandas DataFrame
        pd_filtered_df = filtered_df.toPandas()

        # Create the Plotly figure
        fig = sp.make_subplots(rows=2, cols=1, specs=[[{"secondary_y": True}], [{}]])

        fig.add_trace(go.Scatter(x=pd_filtered_df['Date'], y=pd_filtered_df['Close'], name='Closing Prices'), row=1, col=1, secondary_y=False)
        fig.add_trace(go.Bar(x=pd_filtered_df['Date'], y=pd_filtered_df['Volume'], name='Volume', opacity=0.5), row=1, col=1, secondary_y=True)

        if 'true' in request.form.getlist('rsi_14'):
            fig.add_trace(go.Scatter(x=pd_filtered_df['Date'], y=pd_filtered_df['RSI_14'], name='RSI_14'), row=2, col=1)

        if 'true' in request.form.getlist('stochd_14_3_3'):
            fig.add_trace(go.Scatter(x=pd_filtered_df['Date'], y=pd_filtered_df['STOCHd_14_3_3'], name='STOCHd_14_3_3'), row=2, col=1)

        if 'true' in request.form.getlist('stochk_14_3_3'):
            fig.add_trace(go.Scatter(x=pd_filtered_df['Date'], y=pd_filtered_df['STOCHk_14_3_3'], name='STOCHk_14_3_3'), row=2, col=1)

        if 'true' in request.form.getlist('macd_12_26_9'):
            fig.add_trace(go.Scatter(x=pd_filtered_df['Date'], y=pd_filtered_df['MACD_12_26_9'], name='MACD_12_26_9'), row=2, col=1)

        if 'true' in request.form.getlist('macdh_12_26_9'):
            fig.add_trace(go.Scatter(x=pd_filtered_df['Date'], y=pd_filtered_df['MACD_12_26_9'], name='MACD_12_26_9'), row=2, col=1)

        fig.update_layout(title=f'{ticker} Stock Visualization',
                          xaxis_title='Date',
                          yaxis_title='Price',
                          width=1200,  # Adjust the chart width
                          height=600)  # Adjust the chart height

        # Disabling grid of the secondary y-axis
        fig.layout.yaxis2.showgrid = False

        # Return the HTML page with the chart
        return fig.to_html(include_plotlyjs='cdn')

    # Render the form if the request is not a POST request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False,port=5000)


#why are we using these technologies 

#- more focus on data engg
#- why pyspark 

#different senarios
#data questions - quality and governance (kaggle) (open source) (checks)
#- we can do quality checks. cheaper!

#- 
