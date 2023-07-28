import streamlit as st
from snowflake.connector import connect
from snowflake.connector.connection import SnowflakeConnection
import toml


@st.cache_resource()
def get_connector() -> SnowflakeConnection:
    """Create a connector to SnowFlake using credentials filled in Streamlit secrets"""
    connector = connect(**st.secrets["snowflake"], client_session_keep_alive=True)
    return connector
