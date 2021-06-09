import cv2
import streamlit as st
from .utils import display_LR, display_LR_video, get_video_feed

def morphology_menu(container):
  options = [
    "Erosion", "Dilation",
    "Opening", "Closing",
    "Gradient",
    "Black Hat", "Top Hat",
    "Hit-and-Miss"
  ]
  method = container.radio("Morphology method", options)
  return method

SHAPE_MAP = {
  "Rectangle": cv2.MORPH_RECT,
  "Ellipse": cv2.MORPH_ELLIPSE,
  "Cross": cv2.MORPH_CROSS
}
def se_menu(container):
  container.write(
    """
      <style>
        .css-17alyy9 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) {
          flex-direction: row;
        }
      </style>
    """, 
    unsafe_allow_html=True
  )
  options = [
    "Rectangle", "Ellipse", "Cross" 
  ]
  se = container.radio("Structuring element", options)
  
  return se

MORPHOLOGY_MAP = {
  "Opening": cv2.MORPH_OPEN,
  "Closing": cv2.MORPH_CLOSE,
  "Gradient": cv2.MORPH_GRADIENT,
  "Black Hat": cv2.MORPH_BLACKHAT,
  "Top Hat": cv2.MORPH_TOPHAT,
  "Hit-and-Miss": cv2.MORPH_HITMISS,
}


def get_result(image, method, shape, k_size, force_gray):
  kernel = cv2.getStructuringElement(shape, (k_size, k_size))

  if force_gray:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  result = None
  if method == "Erosion":
    result = cv2.erode(image, kernel)
  elif method == "Dilation":
    result = cv2.dilate(image, kernel)
  else:
    op = MORPHOLOGY_MAP.get(method, None)
    if op is not None:
      result = cv2.morphologyEx(image, op, kernel)
  
  return result


def show_options():
  c1, c2 = st.beta_columns([2, 3])
  method = morphology_menu(c1)
  
  shape_id = se_menu(c2)
  shape = SHAPE_MAP[shape_id]
  k_size = c2.slider("Structuring element size", 3, 99, 25, step= 2)

  if method == "Hit-and-Miss":
    force_gray = True
  else:
    force_gray = c2.checkbox("Convert to grayscale before thresholding")

  return method, shape, k_size, force_gray


def show_image(image):
  if image is not None:
    method, shape, k_size, force_gray = show_options()
    result = get_result(
      image, method,
      shape, k_size,
      force_gray
    )
    display_LR(image, result)


def show_video(video):
  if video is not None:
    method, shape, k_size, force_gray = show_options()
    
    p1, p2 = display_LR_video()
    while True:
      video_feed = get_video_feed(video)
      for frame in video_feed:
        result = get_result(
          frame, method,
          shape, k_size,
          force_gray 
        )
        p1.image(frame)
        p2.image(result)