import cv2
import streamlit as st

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

def show_image(image):
  c1, c2 = st.beta_columns([2, 3])
  method = morphology_menu(c1)
  
  shape_id = se_menu(c2)
  shape = SHAPE_MAP[shape_id]
  k_size = c2.slider("Structuring element size", 3, 99, 25, step= 2)

  if method == "Hit-and-Miss":
    force_gray = True
  else:
    force_gray = c2.checkbox("Convert to grayscale before thresholding")
    
  if image is not None:
    kernel = cv2.getStructuringElement(shape, (k_size, k_size))

    c1, c2 = st.beta_columns(2)
    c1.header("Original")
    c1.image(image)

    if force_gray:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = None
    if method == "Erosion":
      result = cv2.erode(image, kernel)

    elif method == "Dilation":
      result = cv2.dilate(image, kernel)

    elif method == "Opening":
      result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    elif method == "Closing":
      result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    elif method == "Gradient":
      result = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

    elif method == "Black Hat":
      result = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

    elif method == "Top Hat":
      result = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

    elif method == "Hit-and-Miss":
      result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel)

    c2.header("Result")
    if result is not None:
      c2.image(result)
    else:
      c2.title("Unimplemented")