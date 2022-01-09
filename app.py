import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, xrayandct # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Xray", home.app)
app.add_app("CT", data_stats.app)
app.add_app("XrayAndCT", xrayandct.app)

# The main app
app.run()