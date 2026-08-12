import streamlit as st
from supabase import create_client
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Live IoT Sensor Dashboard")
st.caption("Simulated device data streamed via HTTP into Supabase")

placeholder = st.empty()

while True:
    response = supabase.table("sensor_readings").select("*").order("timestamp", desc=True).limit(50).execute()
    data = response.data

    if data:
        df = pd.DataFrame(data)
        df = df.sort_values("timestamp")

        with placeholder.container():
            col1, col2 = st.columns(2)
            col1.metric("Latest Temperature (°C)", df.iloc[-1]["temperature"])
            col2.metric("Latest Humidity (%)", df.iloc[-1]["humidity"])

            st.subheader("Temperature over time")
            st.line_chart(df.set_index("timestamp")["temperature"])

            st.subheader("Humidity over time")
            st.line_chart(df.set_index("timestamp")["humidity"])

            st.subheader("Raw readings")
            st.dataframe(df[::-1], use_container_width=True)

    time.sleep(3)