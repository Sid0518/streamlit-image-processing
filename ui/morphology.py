import cv2
import streamlit as st

def morphology_menu(container):
  options = [
    "Erosion", "Dilation",
    "Opening", "Closing",
    "Hit-and-Miss"
  ]
  method = container.radio("Morphology method", options)
  return method

STRUCTURING_ELEMENT_MAP = {
  "Rectangle": cv2.MORPH_RECT,
  "Ellipse": cv2.MORPH_ELLIPSE,
  "Cross": cv2.MORPH_CROSS
}
def structuring_element_menu(container):
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
  
  se_id = structuring_element_menu(c2)
  structuring_element = STRUCTURING_ELEMENT_MAP[se_id]
  kernel_size = c2.slider("Structuring element size", 3, 99, step= 2)

  if image is not None:
    st.title("Unimplemented")

    # c1, c2 = st.beta_columns(2)
    # c1.header("Original")
    # c1.image(image)

    # c2.header("Result")
    # c2.image(image)