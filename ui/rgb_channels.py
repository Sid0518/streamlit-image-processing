import numpy as np
import streamlit as st

def _red(image):
  out = np.zeros_like(image)
  out[:, :, 0] = image[:, :, 0]
  return out

def _green(image):
  out = np.zeros_like(image)
  out[:, :, 1] = image[:, :, 1]
  return out

def _blue(image):
  out = np.zeros_like(image)
  out[:, :, 2] = image[:, :, 2]
  return out

def show_image(image):
  if image is not None:
    st.header("Original")
    st.image(image)
    
    c1, c2, c3 = st.beta_columns(3)
    c1.header("Red")
    c1.image(_red(image))
    c2.header("Green")
    c2.image(_green(image))
    c3.header("Blue")
    c3.image(_blue(image))