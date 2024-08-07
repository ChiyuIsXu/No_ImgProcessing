# -*- encoding: utf-8 -*-
import tomllib as tl
import streamlit as st
import seaborn as sns
import plotly.express as px

# Load the configuration file
with open("configuration.toml", "rb") as file:
    config = tl.load(file)

# Get the page configuration
page_config = config["page"]

# Set the page configuration
st.set_page_config(
    page_title=page_config["title"],
    page_icon=page_config["icon"],
    layout=page_config["layout"],
    initial_sidebar_state=page_config["initial_sidebar_state"],
    menu_items={
        "Get Help": page_config["menu_items"]["get_help"],
        "Report a bug": page_config["menu_items"]["report_a_bug"],
        "About": page_config["menu_items"]["about"],
    },
)
