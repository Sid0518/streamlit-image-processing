import cv2
import numpy as np
import streamlit as st
import time

from .utils import display_LR, display_LR_video, get_video_feed

class Sobel:
  x = np.array((
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1],
  ), dtype = 'int')

  y = np.array((
    [ 1,  2,  1],
    [ 0,  0,  0],
    [-1, -2, -1],
  ), dtype = 'int')

class Laplacian:
  hv = np.array((
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
  ), dtype = 'int')

  hvd = np.array((
    [1,  1, 1],
    [1, -8, 1],
    [1,  1, 1]
  ), dtype = 'int')

class Prewitt:
  x = np.array((
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
  ), dtype = 'int')

  y = np.array((
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1],
  ), dtype = 'int')

class Scharr:
  x = np.array((
    [ 3, 0,  -3],
    [10, 0, -10],
    [ 3, 0,  -3],
  ), dtype = 'int')

  y = np.array((
    [ 3,  10,  3],
    [ 0,   0,  0],
    [-3, -10, -3],
  ), dtype = 'int')

def edge_detectors(container):
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
    unsafe_allow_html= True
  )
  options = [
    "Sobel", "Prewitt", "Scharr",
    "Laplacian", "Canny"
  ]
  option = container.radio("Edge detection method", options)
  return option

def detect_edges(image, kernel):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
  grad_x = cv2.filter2D(gray, -1, kernel.x)
  grad_y = cv2.filter2D(gray, -1, kernel.y)

  grad = np.abs(grad_x) + np.abs(grad_y)
  grad = np.clip(grad, 0, 255).astype(np.uint8)
  return grad

def laplacian(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  grad = cv2.Laplacian(gray, cv2.CV_16S, ksize= 5)

  grad = np.clip(grad, 0, 255).astype(np.uint8)
  return grad

def get_result(image, method, low= None, high= None):
  result = None
  if method == "Sobel":
    result = detect_edges(image, Sobel)
  elif method == "Prewitt":
    result = detect_edges(image, Prewitt)
  elif method == "Scharr":
    result = detect_edges(image, Scharr)
  elif method == "Laplacian":
    result = laplacian(image)
  elif method == "Canny":
    result = cv2.Canny(image, low, high)

  return result


def show_options():
  method = edge_detectors(st)

  low, high = None, None
  if method == "Canny":
    low, high = st.slider('Set threshold range', 0, 255, (75, 165))

  return method, low, high

def show_image(image):
  if image is not None:
    method, low, high = show_options()
    result = get_result(image, method, low, high)
    display_LR(image, result)


def show_video(video):
  if video is not None:
    method, low, high = show_options()
    
    p1, p2 = display_LR_video()
    while True:
      video_feed = get_video_feed(video)
      for frame in video_feed:
        result = get_result(frame, method, low, high)
        p1.image(frame)
        p2.image(result)