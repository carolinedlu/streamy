import streamlit as st

st.set_page_config(
        page_title="Covid19 Chest Scan Images Detector",
        page_icon="clean_hands_open_hearts_covid19footerimage2-removebg-preview.png",
        layout="centered",
        initial_sidebar_state="auto",

    )

from multiapp import MultiApp
from apps import home, data_stats, xrayandct # import your app modules here



app = MultiApp()

# Add all your application here
app.add_app("Xray", home.app)
app.add_app("CT", data_stats.app)
app.add_app("XrayAndCT", xrayandct.app)

# The main app
app.run()