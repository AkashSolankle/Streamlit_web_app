import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowpark')
#status elements
st.snow()
st.balloons()
#Title
st.title('First :blue[Streamlit] web app :sunglasses:')

#Code block
code = '''st.title('First :blue[Streamlit] web app :sunglasses:')'''
st.code(code, language='python')

with st.chat_message("user"):
    st.write("Hello 👋")
# Perform query.
df = conn.query('SELECT * from MYTABLE;', ttl=600)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.NAME}:{row.PET}:")

st.line_chart(df)
st.area_chart(df)
