from core.settings import MODEL_DIR
import cv2
import os
from django.conf import settings


face_detection_videocam = cv2.CascadeClassifier(os.path.join(
    MODEL_DIR, 'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()
        # Using OpenCV to detect faces in the frame
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
        frame_flip = cv2.flip(image, 1)  # mirror to get the real image
        ret, jpeg = cv2.imencode('.jpg', frame_flip)
        return jpeg.tobytes()
