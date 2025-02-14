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
from charts import line_chart
from streamlit_autorefresh import st_autorefresh


connection_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"

engine = create_engine(connection_string)

count = st_autorefresh(interval=1000*10, limit=100)

def load_data(query):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df


def layout():
    df = load_data("SELECT * FROM bitcoin;")

    st.markdown("# Bitcoin data")

    st.markdown("## Latest data")

    st.markdown("Latest data directly from postgres database in a docker container")

    st.dataframe(df.tail())

    st.markdown("## Bitcoin latest price in USD")

    # plotting code
    price_chart = line_chart(
        df["timestamp"],
        df["price_usd"],
        title="price USD for bitcoin",
        xlabel="time",
        ylabel="USD",
    )

    st.pyplot(price_chart)


if __name__ == "__main__":
    layout()
