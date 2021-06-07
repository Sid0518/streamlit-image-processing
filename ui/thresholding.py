import cv2
import streamlit as st

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
CALCULATION_METHOD_MAP = {
  "Otsu": cv2.THRESH_OTSU,
  "Triangle": cv2.THRESH_TRIANGLE
}
def threshold_calculation_menu(container):
  container.write(
    """
      <style>
        .css-17alyy9 > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) {
          flex-direction: row;
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
  force_gray, calculation_method
):
  if threshold:
    if force_gray:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(image, threshold, 255, method)
  else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(gray, 0, 255, method + calculation_method)

  return result


def show_image(image):
  c1, c2 = st.beta_columns([2, 3])
  
  method_id = thresholding_menu(c1)
  method = METHOD_MAP[method_id]

  threshold_provided = c2.checkbox("Set threshold value manually")
  if threshold_provided:
    threshold = c2.slider('Set threshold value', 0, 255, 127)
    force_gray = c2.checkbox("Convert to grayscale before thresholding")
    calculation_method = None
  else:
    threshold = None
    force_gray = None
    method_id = threshold_calculation_menu(c2)
    calculation_method = CALCULATION_METHOD_MAP[method_id]

  if image is not None:
    c1, c2 = st.beta_columns(2)
    c1.header("Original")
    c1.image(image)
    
    result = get_result(
      image, method, threshold,
      force_gray, calculation_method
    )
    c2.header("Result")
    c2.image(result)