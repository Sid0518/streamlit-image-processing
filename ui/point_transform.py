import cv2
import streamlit as st

from .utils import display_LR, display_LR_video, get_video_feed

def grayscale(image):
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def negative(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return 255 - gray

def BGR(image):
  return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

def point_transform_menu(container):
  container.write(
    """
      <style>
        div.element-container:nth-child(4) > div:nth-child(1) > div:nth-child(2),
        div.element-container:nth-child(5) > div:nth-child(1) > div:nth-child(2) {
          flex-direction: row;
          justify-content: space-around;
        }
      </style>
    """, 
    unsafe_allow_html=True
  )

  options = [
    "Grayscale", "Image negative", "BGR",
  ]
  option = container.radio("Transform", options)
  return option


def get_result(image, transform):
  if transform == "Grayscale":
    result = grayscale(image)
  elif transform == "Image negative":
    result = negative(image)
  elif transform == "BGR":
    result = BGR(image)

  return result


def show_image(image):
  if image is not None:
    transform = point_transform_menu(st)
    result = get_result(image, transform)
    display_LR(image, result)


def show_video(video):
  if video is not None:
    transform = point_transform_menu(st)
    p1, p2 = display_LR_video()

    while True:
      video_feed = get_video_feed(video)
      for frame in video_feed:
        result = get_result(frame, transform)
        p1.image(frame)
        p2.image(result)