import os
import sys

# # Ensure the path to the ARIMA model is correct
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import matplotlib.pyplot as plt

from model.arima import forecast_with_arima
from statsmodels.graphics.tsaplots import plot_predict
from fm.ai_module import invoke



# Streamlit app setup
st.set_page_config(layout='wide')



class Streamlit_main:
    def __init__(self):
        self.main()
        
        
    def plot(self, df, start, end):
        fig, ax = plt.subplots(figsize=(10, 8))
        fig = plot_predict(df, start=start, end=end, ax=ax)
        legend = ax.legend(loc="upper left")
        return fig, legend


    def main(self):
        st.title("Real-Time Demand Forecasting Analysis Prototype")
        load_dotenv()  # Load environment variables

        # MongoDB connection setup
        client = MongoClient(os.environ.get("MONGO_URI"))
        db = client[os.environ.get("MONGO_DB")]
        collection = db[os.environ.get("MONGO_COLLECTION")]
        data_logs = list(collection.find({}))

        # Streamlit UI components
        col1, col2 = st.columns(2)
        chat_input = col2.text_input("Chat Box")
        if chat_input:
            col2.markdown(f"You wrote: **{chat_input}**")

        df = pd.DataFrame(data_logs).drop(columns=['_id'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Set 'timestamp' as the index
        df.set_index('timestamp', inplace=True)
        st.write(df['sales'].dtype)

        # Aggregate sales data by day by city
        daily_sales = df.groupby(['city', pd.Grouper(freq='T')])['sales'].sum()
        st.write(daily_sales)
        
        loading_state = col1.empty()
        if col1.button("Fetch Latest Data"):
            loading_state.text("Loading data...")
            loading_state.empty()

        if not df.empty:
            col1.subheader("Latest Few Rows of Data")
            col1.write(df.tail())

            if col1.button("Process Data"):
                loading_state.text("Processing data...")
                col1.write(daily_sales.tail())

                forecasted_sales = {}
                if 'city' in daily_sales.index.names:
                    for city in daily_sales.index.get_level_values('city').unique():
                        city_sales = daily_sales.xs(city, level='city')
                        city_sales_df = city_sales.to_frame(name='sales')

                        try:
                            forecast_result = forecast_with_arima(city_sales_df, 'sales', (1, 1, 1), 1)
                            forecasted_sales[city] = forecast_result
                        except ValueError as e:
                            col1.error(f"Error in forecasting for {city}: {e}")

                        loading_state.empty()
                        col1.subheader("Actual Sales")
                        col1.line_chart(city_sales_df)
                        col1.write(f"mean: {city_sales.mean()}")

                        col1.subheader("Forecasted Sales")
                        plot = self.plot(forecast_result, city_sales.index[-1], city_sales.index[-1] + pd.Timedelta(minutes=5))
                        col1.write(plot)

                        # Invoke AI Module
                        prompt = f"give analysis for {city} for the next 5 minutes. the sales average is {city_sales.mean()} and the forecasted sales is {forecast_result}"
                        response = invoke(prompt)
                        col2.write(response)

if __name__ == "__main__":
    Streamlit_main()
