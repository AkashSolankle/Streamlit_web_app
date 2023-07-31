import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import scipy



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
df = conn.query('SELECT * from KORIA_WEATHER_REPORT;', ttl=600)

# Print results.
  #for row in df.itertuples():
  #    st.write(f"{row.NAME}:{row.PET}:")
#Charts
#st.line_chart(df)
#st.area_chart(df)


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
