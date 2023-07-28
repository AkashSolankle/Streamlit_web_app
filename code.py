import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowpark')

# Perform query.
df = conn.query('SELECT PROVINCE from SOURTH_KORIA_COVID;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(row)
