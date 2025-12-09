import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("qatarcars.csv")

st.title("Qatar Cars -- TidyTuesday 12/9")

x = st.sidebar.selectbox(
    "Select an X variable:",
    df.columns
)

y = st.sidebar.selectbox(
    "Select a Y variable:",
    df.columns
)

fig = px.scatter(df, x, y, color="enginetype", hover_data = ["make", "model", "economy", "price", "mass", "type"])
fig.update_traces(marker_size=10)
st.plotly_chart(fig)

st.sidebar.markdown("""
                    |variable      |description                                                 |
|:-----------|:-----------------------------------------------------------|
|origin      |The country associated with the car brand.                  |
|make        |The brand of the car, such as Toyota or Land Rover.         |
|model       |The specific type of car, such as Land Cruiser or Defender. |
|length      |Length of the car (in meters).                              |
|width       |Width of the car (in meters).                               |
|height      |Height of the car (in meters).                              |
|seating     |Number of seats in the car.                                 |
|trunk       |Capacity or volume of the trunk (in liters).                |
|economy     |Fuel economy of the car (in liters per 100 km).             |
|horsepower  |Car horsepower.                                             |
|price       |Price of the car in 2025 Qatari riyals.                     |
|mass        |Mass of the car (in kg).                                    |
|performance |Time to accelerate from 0 to 100 km/h (in seconds).         |
|type        |The type of the car, such as coupe, sedan, or SUV.          |
|enginetype  |The type of engine: electric, hybrid, or petrol.            |
                    """)
