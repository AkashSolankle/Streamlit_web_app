import streamlit as st
import pandas as pd
import numpy as np




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

chart_data = df.DataFrame(
    np.random.randn(200, 3),
    columns=['PROVINCE', 'PRECIPITATION', 'CODE'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'PROVINCE', 'type': 'quantitative'},
        'y': {'field': 'PRECIPITATION', 'type': 'quantitative'},
        'size': {'field': 'CODE', 'type': 'quantitative'},
        'color': {'field': 'CODE', 'type': 'quantitative'},
    },
})
