import numpy as np
import streamlit as st
from .utils import get_video_feed

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

  
def show_video(video):
  if video is not None:
    st.header("Original")
    p = st.empty()
    
    c1, c2, c3 = st.beta_columns(3)
    c1.header("Red")
    p1 = c1.empty()
    c2.header("Green")
    p2 = c2.empty()
    c3.header("Blue")
    p3 = c3.empty()

    while True:
      video_feed = get_video_feed(video)
      
      for frame in video_feed:
        p.image(frame)
        p1.image(_red(frame))
        p2.image(_green(frame))
        p3.image(_blue(frame))