import cv2
import streamlit as st

from .utils import display_LR, display_LR_video, get_video_feed

#-------------------------------------------------------------#
  # Thresholding methods
METHOD_MAP = {
  "Binary": cv2.THRESH_BINARY, 
  "Binary Inverse": cv2.THRESH_BINARY_INV, 
  "Truncate": cv2.THRESH_TRUNC,
  "Zero": cv2.THRESH_TOZERO, 
  "Zero Inverse": cv2.THRESH_TOZERO_INV
}
def thresholding_menu(container):
  options = [
    "Binary", "Binary Inverse", 
    "Truncate",
    "Zero", "Zero Inverse"
  ]
  option = container.radio("Threshold method", options)
  return option
#-------------------------------------------------------------#

#-----------------------------------------------------------------------#
  # Automatic threshold calculation methods
CALC_MAP = {
  "Otsu": cv2.THRESH_OTSU,
  "Triangle": cv2.THRESH_TRIANGLE
}
def threshold_calc_menu(container):
  container.write(
    """
      <style>
        .css-17alyy9 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) {
          flex-direction: row;
          justify-content: space-around;
        }
      </style>
    """, 
    unsafe_allow_html=True
  )

  options = [
    "Otsu",
    "Triangle"
  ]
  option = container.radio("Threshold calculation method", options)
  return option
#-----------------------------------------------------------------------#


def get_result(
  image, method, threshold, 
  force_gray, calc_method
):
  if threshold:
    if force_gray:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(image, threshold, 255, method)
  else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(gray, 0, 255, method + calc_method)

  return result


def show_options():
  c1, c2 = st.beta_columns([2, 3])
  
  method_id = thresholding_menu(c1)
  method = METHOD_MAP[method_id]

  threshold_provided = c2.checkbox("Set threshold value manually")
  if threshold_provided:
    threshold = c2.slider('Set threshold value', 0, 255, 127)
    force_gray = c2.checkbox("Convert to grayscale before thresholding")
    calc_method = None
  else:
    threshold = None
    force_gray = False
    method_id = threshold_calc_menu(c2)
    calc_method = CALC_MAP[method_id]

  return method, threshold, force_gray, calc_method


def show_image(image):
  if image is not None:
    method, threshold, force_gray, calc_method = show_options()
    result = get_result(
      image, method, threshold,
      force_gray, calc_method
    )
    display_LR(image, result)


def show_video(video):
  if video is not None:
    method, threshold, force_gray, calc_method = show_options()
    p1, p2 = display_LR_video()

    while True:
      video_feed = get_video_feed(video)
      for frame in video_feed:
        result = get_result(
          frame, method, threshold,
          force_gray, calc_method
        )
        p1.image(frame)
        p2.image(result)