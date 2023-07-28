import streamlit as st
from snowflake.snowpark import Session
from secrets import SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, SNOWFLAKE_PASSWORD


session = Session(url=SNOWFLAKE_ACCOUNT, user=SNOWFLAKE_USER, password=SNOWFLAKE_PASSWORD)
df = session.sql("SELECT * FROM PETS.MYTABLE").to_pandas()
st.write(df)


st.title("Hi Anber! Welcome to Streamlit!")

st.write("My first DataFrame")

st.write(
pd.DataFrame({
    'A': [1, 5, 9, 7],
    'B': [3, 2, 4, 8]
  })
)
