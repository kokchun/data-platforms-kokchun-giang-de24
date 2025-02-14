import streamlit as st
from constants import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)
from sqlalchemy import create_engine
import pandas as pd 


connection_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"

engine = create_engine(connection_string)

query = "SELECT * FROM bitcoin;"

with engine.connect() as conn: 
    df = pd.read_sql(query, conn)


st.markdown("# Bitcoin data")

st.markdown("## Latest data")

st.dataframe(df.tail())