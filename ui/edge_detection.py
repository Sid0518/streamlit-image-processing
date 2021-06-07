import cv2
import streamlit as st

def edge_detectors(container):
  options = [
    "Sobel", "Prewitt", "Scharr",
    "Laplacian", "Canny"
  ]
  option = container.radio("Edge detection method", options)
  return option

def show_image(image):
  method = edge_detectors(st)

  if image is not None:
    st.title("Unimplemented")
    
    # c1, c2 = st.beta_columns(2)
    # c1.header("Original")
    # c1.image(image)

    # c2.header("Result")
    # c2.image(image)