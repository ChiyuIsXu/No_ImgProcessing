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

# normalize the image
image_normalized = img_gray / 255.0

# Sidebar
with st.sidebar:
    st.title("GrayScale")
    # # 对数变换
    st.header("Log Transformation")
    c1 = st.slider(
        label="constant 1",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.1,
        format="%.1f",
    )  # 通常取 1，或者根据需要调整
    log_transformed = c1 * np.log(1 + image_normalized)
    # 反归一化到 [0, 255] 范围
    log_transformed = np.uint8(log_transformed * 255)
    st.divider()

    # # 幂次变换
    st.header("Power-Law Transformation")
    c2 = st.slider(
        label="constant 2",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.1,
        format="%.1f",
    )  # 通常取 1，或者根据需要调整
    gamma = st.slider(
        label="gamma",
        min_value=0.0,
        max_value=5.0,
        value=1.0,
        step=0.1,
        format="%.1f",
    )
    # 应用幂律变换
    power_law_transformed = c2 * (image_normalized**gamma)

    # 反归一化到 [0, 255] 范围
    power_law_transformed = np.uint8(power_law_transformed * 255)


st.title("GrayScale")

st.write(f"Current Page: {current_page}")

# 显示图像
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1), plt.title("Gray Image")
plt.imshow(img_gray, cmap="gray")


plt.subplot(1, 3, 2), plt.title("Log Transformed Image")
plt.imshow(log_transformed, cmap="gray")

plt.subplot(1, 3, 3), plt.title("Power-Law Transformed Image")
plt.imshow(power_law_transformed, cmap="gray")

st.pyplot(plt)

st.divider()

tab1, tab2 = st.tabs(["Log Transformation", "Power-Law Transformation"])
with tab1:
    st.write("## Log Transformation")
    st.markdown(
        r"""
        对数变换是一种图像处理技术，用于调整图像的亮度分布，使得图像中的细节更加突出。</br>
        这种技术通常用于增强图像的对比度，特别是在处理具有较大亮度范围的图像时。</br>
        $Transformed Pixel = Scaling Factor \cdot \log(1 + Original Pixel)$
        """,
        unsafe_allow_html=True,
    )
    # 使用 Streamlit 布局容器调整宽度
    col, _, _ = st.columns([1, 1, 1])
    with col:
        ScalingFactor = c1
        OriginalPixel = np.linspace(0, 1, 100)
        TransformedPixel = ScalingFactor * np.log1p(OriginalPixel)
        plt.figure(figsize=(5, 5))
        plt.plot(
            OriginalPixel, TransformedPixel, label=f"Scaling Factor = {ScalingFactor}"
        )
        plt.plot(OriginalPixel, OriginalPixel)
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("Original Pixel Value")
        plt.ylabel("Transformed Pixel Value")
        plt.title("Logarithmic Transformation of Pixel Values")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)

with tab2:
    st.write("## Power-Law Transformation")
    st.markdown(
        r"""
        幂次变换是一种图像处理技术，用于调整图像的亮度分布，使得图像中的细节更加突出。</br>
        这种技术通常用于增强图像的对比度，特别是在处理具有较大亮度范围的图像时。</br>
        $Transformed Pixel = Scaling Factor \cdot (Original Pixel)^{\gamma}$</br>

        幂律变换的效果:</br>
        当 $\gamma>1$：变换将增强图像的高亮区域，压缩暗部的细节。这种变换可以增加图像的对比度，使得亮度较高的区域更加明显。</br>
        当 $\gamma<1$：变换将增强图像的暗部细节，压缩高亮区域。这种变换可以减少图像的对比度，使得暗部的细节更加突出。
        """,
        unsafe_allow_html=True,
    )
    # 使用 Streamlit 布局容器调整宽度
    col, _, _ = st.columns([1, 1, 1])
    with col:
        ScalingFactor = c2
        gamma = gamma
        OriginalPixel = np.linspace(0, 1, 100)
        plt.figure(figsize=(5, 5))
        plt.plot(
            OriginalPixel,
            ScalingFactor * OriginalPixel**gamma,
            label=f"Scaling Factor = {ScalingFactor}, Gamma = {gamma}",
        )
        plt.plot(OriginalPixel, OriginalPixel)
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("Original Pixel Value")
        plt.ylabel("Transformed Pixel Value")
        plt.title("Power-Law Transformation of Pixel Values")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
