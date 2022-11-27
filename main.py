import streamlit as st
import database.database as db
import layout.header as header
import pandas as pd

if __name__ == "__main__":
    header.get_header("Connection to database")

    st.table(pd.DataFrame(
        db.get_users(),
        columns=('id', 'First name', 'Last name', 'age'))
    )