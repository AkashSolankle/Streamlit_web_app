import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pydeck as pdk
import scipy
import altair as alt
import matplotlib.pyplot as plt
from streamlit_extras.switch_page_button import switch_page
from snowflake.snowpark.context import get_active_session


session = get_active_session()
st.set_page_config(page_title='Covid App', page_icon=':mask:')
# Initialize connection.
conn = st.experimental_connection('snowpark')
#status elements
#st.snow()
#st.balloons()
#Title
st.title('First :blue[Streamlit] web app :sunglasses:')
st.text("")
st.text("")

st.sidebar.success('Welcome to Home Page :tada:')
#Code block
  #code = '''st.title('First :blue[Streamlit] web app :sunglasses:')'''
  #st.code(code, language='python')

#with st.chat_message("user"):
#    st.write("Hello 👋")
# Perform query.
df = conn.query('SELECT top 1000 * from KORIA_WEATHER_REPORT;', ttl=600)
#st.dataframe(df)
with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.data_editor(df, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        #Note the quote_identifiers argument for case insensitivity
        session.write_pandas(edited, "KORIA_WEATHER_REPORT", overwrite=True, quote_identifiers=False)
        st.success("Table updated")
        time.sleep(5)
    except:
        st.warning("Error updating table")
    #display success message for 5 seconds and update the table to reflect what is in Snowflake
    st.experimental_rerun()
#st.line_chart(df)
st.text("")
st.text("")
st.text("")
st.area_chart(df, x='PROVINCE', y='CODE')
st.line_chart(df, x='PROVINCE', y='CODE')
c = alt.Chart(df).mark_circle().encode(
    x='PROVINCE', y='CODE', size='c', color='c', tooltip=['PROVINCE', 'CODE', 'c'])
st.altair_chart(c, use_container_width=True)
