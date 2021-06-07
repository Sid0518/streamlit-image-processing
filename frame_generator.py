import cv2

def generate_frames(video):
  source = cv2.VideoCapture(video)
  if source is None:
    raise IOError("Unable to start video feed")

  while True:
    ret, frame = source.read()
    if frame is None:
      break

    cv2.waitKey(1)