import streamlit as st
from snowflake.connector import connect
from snowflake.connector.connection import SnowflakeConnection
import toml


@st.experimental_singleton()
def get_connector() -> SnowflakeConnection:
    """Create a connector to SnowFlake using credentials filled in Streamlit secrets"""
    connector = connect(**st.secrets["snowflake"], client_session_keep_alive=True)
    return connector

# Time to live: the maximum number of seconds to keep an entry in the cache
TTL = 24 * 60 * 60

# Using `experimental_memo()` to memoize function executions
@st.experimental_memo(ttl=TTL)
def get_databases(_connector) -> pd.DataFrame:
    """Get all databases available in Snowflake"""
    return pd.read_sql("SHOW DATABASES;", _connector)


