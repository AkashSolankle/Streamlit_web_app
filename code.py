import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st  



#read csv file
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"
#summary of data
# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()
