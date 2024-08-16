# -*- encoding: utf-8 -*-
import time
import tomllib as tl
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px

# Load the configuration file
with open("configuration.toml", "rb") as file:
    config = tl.load(file)

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

# Set the theme
st.logo("static/logo_with_text.png")

# Initialize the App
if "current_page" not in st.session_state:
    st.session_state.current_page = None

# Topics for the App
# TODO：Add more topics
topics = [
    None,
    "Fundemental Image Processing",
    "Test",
]

# define the pages

# # Main page
df = pd.DataFrame(topics, columns=["Topics"]).dropna()


html = """
<style>
    .table{{width: 100%;margin-left: 0;margin-right: auto;border-collapse: collapse;}}
    .table th, .table td{{text-align: left;padding: 8px;}}
</style>
<div>{0}</div>
""".format(
    df.to_html(index=False, classes="table")
)


def choose_topic():
    _, col, _ = st.columns([1, 2, 1])

    with col:
        st.title(page_config["title"])
        # TODO: Add a description for the app
        st.write("This is a Algorithm Visualizer.")

        st.markdown(html, unsafe_allow_html=True)

        choice = st.selectbox("Choose a topic", topics)

        if st.button("Go to the topic"):
            st.session_state.current_page = choice
            if choice:
                st.rerun()
            else:
                st.write("Please select a topic")


def logout():
    st.session_state.current_page = None

    st.image("static/logo_with_text.png")
    progress_text = "Returning Home Page. Please wait."
    my_empty = """<style>.my_empty{height: 20vh;}</style><div class="my_empty"></div>"""
    st.markdown(my_empty, unsafe_allow_html=True)
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    st.rerun()


help_page = st.Page("pages/help.py", title="Help", icon=":material/help:")
logout_page = st.Page(logout, title="Exit", icon=":material/logout:")
setting_page = st.Page(
    "pages/settings.py", title="Settings", icon=":material/settings:"
)


# # Test page
test_page = st.Page(
    "topics/Test/test-page.py", title="Test Page", icon=":material/settings:"
)
test_page2 = st.Page(
    "topics/Test/test-page2.py", title="Test Page 2", icon=":material/settings:"
)

# TODO：Define more pages for each topic
# # Fundemental Image Processing page
grayscale_page = st.Page(
    "topics/FundementalImageProcessing/grayscale.py",
    title="Grayscale",
    icon=":material/settings:",
)
graphic_transformation_page = st.Page(
    "topics/FundementalImageProcessing/graphic-transformation.py",
    title="Graphic Transformation",
    icon=":material/settings:",
)

# page dictionary: pages for each topic
# TODO: Add created pages to the page dictionary
page_dict = {}
account_pages = [help_page, setting_page, logout_page]
test_pages = [test_page, test_page2]
fundemental_image_processing_pages = [grayscale_page, graphic_transformation_page]

# App navigation
current_page = st.session_state.get("current_page", None)
# TODO: Create navigation for each topic
if current_page == topics[1]:
    page_dict[topics[1]] = fundemental_image_processing_pages
    pg = st.navigation(page_dict | {"Assistance": account_pages})
elif current_page == topics[-1]:
    page_dict[topics[-1]] = test_pages
    pg = st.navigation(page_dict | {"Assistance": account_pages})
else:
    pg = st.navigation([st.Page(choose_topic)])

pg.run()
