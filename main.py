import streamlit as st
import numpy as np
from PIL import Image

import sidebar_menus

import ui.point_transform
import ui.rgb_channels
import ui.thresholding
import ui.edge_detection
import ui.morphology

MODULE_MAP = {
  "Point transform": ui.point_transform,
  "RGB channels": ui.rgb_channels,
  "Thresholding": ui.thresholding,
  "Edge detection": ui.edge_detection,
  "Morphology": ui.morphology
}

image, video = None, None

header = st.empty()
subheader = st.empty()
#---------------------------------------------------------------------------------#
  # Select the input type from the video
input_type = sidebar_menus.inputs()
if input_type == "Image":
  f = st.file_uploader("Upload an image", type= ["png", "jpg", "jpeg", "webp"])
  if f is not None:
    image = Image.open(f)
    image = np.array(image)

elif input_type == "Video":
  video_type = sidebar_menus.video_inputs()
  
  if video_type == "Upload":
    video = st.file_uploader("Upload an image", type= ["mp4"])
  elif video_type == "Webcam":
    video = None
  st.header(type(video))
#----------------------------------------------------------------------------------#

# Show the radio buttons to select from the various image processing methods
effect_type = sidebar_menus.effects()
header.header(effect_type)

effect_module = MODULE_MAP.get(effect_type, None)
if effect_module is not None:
  if input_type == "Image":
    effect_module.show_image(image)
  elif input_type == "Video":
    effect_module.show_video(video, video_type)