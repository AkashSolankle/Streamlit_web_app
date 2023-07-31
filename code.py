import streamlit as st



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

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Code",
            "type": "quantitative",
        },
        "y": {
            "field": "Province",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        df, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        df, chart, theme=None, use_container_width=True
    )
