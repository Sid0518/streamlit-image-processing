import cv2
import streamlit as st

def display_LR(original, result, h1= "Original", h2= "Result"):
  c1, c2 = st.beta_columns(2)
  
  c1.header(h1)
  if original is not None:
    c1.image(original)
  else:
    c1.subheader("No image to show")

  c2.header(h2)
  if result is not None:
    c2.image(result)
  else:
    c2.subheader("No result to show")

def display_LR_video(h1= "Original", h2= "Result"):
  c1, c2 = st.beta_columns(2)
  
  c1.header(h1)
  c2.header(h2)
  
  p1 = c1.empty()
  p2 = c2.empty()
  return p1, p2

def get_video_feed(video):
  source = cv2.VideoCapture(video)
  if source is None:
    raise IOError("Unable to start video feed")

  while True:
    ret, frame = source.read()
    if frame is None:
      break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    yield frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break