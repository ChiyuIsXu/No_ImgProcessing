# -*- encoding: utf-8 -*-
import tomllib as tl
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px

# Initialize the App
if "current_page" not in st.session_state:
    st.session_state.current_page = None
current_page = st.session_state.get("current_page", None)

# Sidebar


# st.sidebar.title("Test")

st.title("Test")

st.write(f"Current Page: {current_page}")
