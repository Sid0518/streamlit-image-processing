import streamlit as st

def inputs():
  options = ["Image", "Video"]
  option = st.sidebar.selectbox("Input type", options)
  return option

def video_inputs():
  options = ["Upload", "Webcam"]
  option = st.sidebar.selectbox("Video input type", options)
  return option

def effects():
  options = [
    "Point transform",
    "RGB channels", 
    "Histogram equalization",
    "Thresholding", "Edge detection", 
    "Morphology"
  ]
  option = st.sidebar.radio("Effect", options)
  return option