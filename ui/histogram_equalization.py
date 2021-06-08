import cv2
import streamlit as st

def show_image(image):
  if image is not None:
    st.header("Original")
    st.image(image)

    c1, c2 = st.beta_columns(2)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    c1.header("Grayscale")
    c1.image(gray)

    result = cv2.equalizeHist(gray)
    c2.header("Result")
    c2.image(result)