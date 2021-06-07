import cv2
import streamlit as st

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
        div.element-container:nth-child(5) > div:nth-child(1) > div:nth-child(2) {
          flex-direction: row;
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
  transform = point_transform_menu(st)

  if image is not None:
    c1, c2 = st.beta_columns(2)
    c1.header("Original")
    c1.image(image)

    result = get_result(image, transform)
    c2.header("Result")
    c2.image(result)

def show_video(video, video_type):
  transform = point_transform_menu(st)