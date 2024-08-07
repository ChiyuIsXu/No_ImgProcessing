# -*- encoding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def rgb_to_hsb(red, green, blue):
    red_prime = red / 255.0
    green_prime = green / 255.0
    blue_prime = blue / 255.0

    max_value = max(red_prime, green_prime, blue_prime)
    min_value = min(red_prime, green_prime, blue_prime)
    Chroma = max_value - min_value

    Brightness = max_value

    if max_value == 0:
        Saturation = 0
    else:
        Saturation = Chroma / max_value

    if Chroma == 0:
        Hue = 0
    else:
        if max_value == red_prime:
            Hue = 60 * ((green_prime - blue_prime) / Chroma % 6)
        elif max_value == green_prime:
            Hue = 60 * ((blue_prime - red_prime) / Chroma + 2)
        elif max_value == blue_prime:
            Hue = 60 * ((red_prime - green_prime) / Chroma + 4)

    Hue = Hue % 360

    return Hue, Saturation, Brightness


def hsb_to_rgb(hue, saturation, brightness):

    hue = hue % 360
    saturation = max(0, min(saturation, 1))
    brightness = max(0, min(brightness, 1))

    Chroma = brightness * saturation
    hue_prime = hue / 60
    X = Chroma * (1 - abs(hue_prime % 2 - 1))
    m = brightness - Chroma

    if 0 <= hue_prime < 1:
        r, g, b = Chroma, X, 0
    elif 1 <= hue_prime < 2:
        r, g, b = X, Chroma, 0
    elif 2 <= hue_prime < 3:
        r, g, b = 0, Chroma, X
    elif 3 <= hue_prime < 4:
        r, g, b = 0, X, Chroma
    elif 4 <= hue_prime < 5:
        r, g, b = X, 0, Chroma
    elif 5 <= hue_prime < 6:
        r, g, b = Chroma, 0, X

    r = (r + m) * 255
    g = (g + m) * 255
    b = (b + m) * 255

    return int(round(r)), int(round(g)), int(round(b))


def plot_rgb_histogram(red, green, blue):
    # 创建直方图数据
    colors = [red, green, blue]
    color_labels = ["Red", "Green", "Blue"]

    # 绘制直方图
    plt.figure(figsize=(8, 8))
    plt.bar(color_labels, colors, color=["red", "green", "blue"])
    plt.ylim(0, 255)
    plt.xlabel("Color Channels")
    plt.ylabel("Intensity")
    plt.title("RGB Color Histogram")

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # 显示直方图
    st.pyplot(plt)


def main():

    st.set_page_config(
        page_title="Color Mode",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            "Get Help": "https://www.extremelycoolapp.com/help",
        },
    )

    st.title("RGB 和 HSB 颜色转换器")
    st.divider()

    # 分列
    col1, col2 = st.columns([4, 4])
    with col1:
        col1_1, col1_2 = st.columns([1, 4])
        with col1_1:
            red = st.slider("Red (0-255)", 0, 255, 255)
            green = st.slider("Green (0-255)", 0, 255, 0)
            blue = st.slider("Blue (0-255)", 0, 255, 0)
            color_rgb = (red, green, blue)

            hue, saturation, brightness = rgb_to_hsb(red, green, blue)

            st.write(
                f"""
                Hue = {hue:.2f}°\
                \n\
                    Saturation = {(saturation*100):.2f}\
                \n\
                    Brightness = {(brightness*100):.2f}
                """
            )
            st.image(
                np.zeros((100, 100, 3), dtype=np.uint8) + np.array(color_rgb),
                use_column_width=True,
            )

        with col1_2:
            plot_rgb_histogram(red, green, blue)

    with col2:
        col2_1, col2_2 = st.columns([1, 4])
        with col2_1:

            hue = st.slider("Hue (0-360)", 0, 360, 0)
            saturation = st.slider("Saturation (0-1)", 0.0, 1.0, 1.0)
            brightness = st.slider("Brightness (0-1)", 0.0, 1.0, 1.0)

            color_rgb = hsb_to_rgb(hue, saturation, brightness)
            st.write(
                f"""
                Red = {color_rgb[0]}\
                \n\
                    Green = {color_rgb[1]}\
                \n\
                    Blue = {color_rgb[2]}
                """
            )
            st.image(
                np.zeros((100, 100, 3), dtype=np.uint8) + np.array(color_rgb),
                use_column_width=True,
            )
        with col2_2:
            plot_rgb_histogram(color_rgb[0], color_rgb[1], color_rgb[2])
    st.latex(
        r"""
            H = \begin{cases}
            60^\circ \times \left( \frac{G - B}{\Delta} \right) + 360^\circ & \text{if } R = \text{max}(R, G, B) \\
            60^\circ \times \left( \frac{B - R}{\Delta} \right) + 120^\circ & \text{if } G = \text{max}(R, G, B) \\
            60^\circ \times \left( \frac{R - G}{\Delta} \right) + 240^\circ & \text{if } B = \text{max}(R, G, B)
            \end{cases}
        """
    )


if __name__ == "__main__":
    main()
