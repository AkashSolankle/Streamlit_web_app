import streamlit as st
from snowflake.snowpark import Session
from .secrets import SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, SNOWFLAKE_PASSWORD


session = Session(url=st.secrets["SNOWFLAKE_ACCOUNT"], user=st.secrets["SNOWFLAKE_USER"], password=st.secrets["SNOWFLAKE_PASSWORD"])

df = session.sql("SELECT * FROM PETS.MYTABLE").to_pandas()
st.write(df)
