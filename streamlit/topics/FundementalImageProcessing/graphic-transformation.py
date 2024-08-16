# -*- encoding: utf-8 -*-
import tomllib as tl

import numpy as np
import pandas as pd

from PIL import Image
import cv2 as cv
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import config

# Initialize the App
if "current_page" not in st.session_state:
    st.session_state.current_page = None
current_page = st.session_state.get("current_page", None)

# 导入图像
img = cv.imread(config.TEST_IMAGE)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Sidebar
with st.sidebar:
    st.title("Graphic Transformation")

# # 平移
# # 旋转
# # 缩放

# # 翻转

# # 仿射变换
# # 透视变换

# Main Area
st.title("Graphic Transformation")