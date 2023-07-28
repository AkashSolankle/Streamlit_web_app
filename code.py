import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowpark')

st.title('First :blue[Streamlit] web app emojis :sunglasses:')
# Perform query.
df = conn.query('SELECT BIRTH_YEAR,PROVINCE from SOURTH_KORIA_COVID;', ttl=600)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.NAME}:{row.PET}:")

st.line_chart(df)
st.area_chart(df)
