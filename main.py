import cv2
import numpy as np
from PIL import Image
import streamlit as st

#---------------------------------------------------------------#
  # Setup temporary directory for video upload
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

tmpdir = os.path.join(ROOT_DIR, "temp")
if not os.path.isdir(tmpdir):
  os.mkdir(tmpdir)
  
for tmpfile in os.listdir(os.path.join(os.getcwd(), "temp")):
  os.unlink(os.path.join(tmpdir, tmpfile))
  
import tempfile
tempfile.tempdir = tmpdir
#---------------------------------------------------------------#

import sidebar_menus
import ui.point_transform
import ui.rgb_channels
import ui.histogram_equalization
import ui.thresholding
import ui.edge_detection
import ui.morphology

MODULE_MAP = {
  "Point transform": ui.point_transform,
  "RGB channels": ui.rgb_channels,
  "Histogram equalization": ui.histogram_equalization,
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
    f = st.file_uploader("Upload an image", type= ["mp4"])
    if f is not None:
      tfile = tempfile.NamedTemporaryFile(delete= False)
      tfile.write(f.read())
      tfile.close()
      video = tfile.name

  elif video_type == "Webcam":
    video = cv2.CAP_DSHOW
#----------------------------------------------------------------------------------#

# Show the radio buttons to select from the various image processing methods
effect_type = sidebar_menus.effects()
header.header(effect_type)

effect_module = MODULE_MAP.get(effect_type, None)
if effect_module is not None:
  if input_type == "Image":
    effect_module.show_image(image)
  elif input_type == "Video":
    effect_module.show_video(video)