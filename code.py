import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st  



df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
