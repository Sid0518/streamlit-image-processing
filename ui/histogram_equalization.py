import cv2
import streamlit as st

from .utils import display_LR, display_LR_video, get_video_feed


def show_image(image):
  if image is not None:
    st.header("Original")
    st.image(image)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.equalizeHist(gray)
    display_LR(gray, result, h1= "Grayscale")


def show_video(video):
  if video is not None:
    st.header("Original")
    p = st.empty()
    p1, p2 = display_LR_video(h1= "Grayscale")

    while True:
      video_feed = get_video_feed(video)
      for frame in video_feed:
        p.image(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = cv2.equalizeHist(gray)
        p1.image(gray)
        p2.image(result)