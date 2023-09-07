import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pydeck as pdk
import scipy
import altair as alt
import matplotlib.pyplot as plt
import time
from streamlit_extras.switch_page_button import switch_page
from snowflake.snowpark import Session


st.set_page_config(page_title='Experimental Connection', page_icon=':wave:')
# Initialize connection.
session = st.experimental_connection('snowpark').session
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
user = session.sql( 'select current_user()')
st.dataframe(user.style.highlight_max(axis=0))
#print(user.['CURRENT_USER()'].values[:1])
with st.chat_message("user"):
    st.write(user)
# Perform query.
df = session.table('TAGGING_SAMPLE')


#st.dataframe(df)
with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.data_editor(df, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        #Note the quote_identifiers argument for case insensitivity
        session.write_pandas(edited, "TAGGING_SAMPLE", overwrite=True, quote_identifiers=False)
        st.toast("Table updated")
        time.sleep(5)
    except:
        st.warning("Error updating table")
    #display success message for 5 seconds and update the table to reflect what is in Snowflake
    st.experimental_rerun()
#st.line_chart(df)
st.text("")
st.text("")
st.text("")


if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🔔')
