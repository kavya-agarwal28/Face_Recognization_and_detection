import cv2
import face_recognition
from PIL import Image, ImageDraw
import numpy as np

webcam_video_stream = cv2.VideoCapture(0)

while True:
    ret,current_frame = webcam_video_stream.read()
    face_landmarks_list = face_recognition.face_landmarks(current_frame)
    pil_image = Image.fromarray(current_frame)
    d = ImageDraw.Draw(pil_image)
    for face_landmarks in face_landmarks_list:
        d.line(face_landmarks['chin'],fill=(255,255,255),width=2)
        d.line(face_landmarks['left_eyebrow'],fill=(255,255,255),width=2)
        d.line(face_landmarks['right_eyebrow'],fill=(255,255,255),width=2)
        d.line(face_landmarks['nose_bridge'],fill=(255,255,255),width=2)
        d.line(face_landmarks['nose_tip'],fill=(255,255,255),width=2)
        d.line(face_landmarks['left_eye'],fill=(255,255,255),width=2)
        d.line(face_landmarks['right_eye'],fill=(255,255,255),width=2)
        d.line(face_landmarks['top_lip'],fill=(255,255,255),width=2)
        d.line(face_landmarks['bottom_lip'],fill=(255,255,255),width=2)
    rgb_image = pil_image.convert('RGB')
    rgb_open_cv_image = np.array(rgb_image)
    bgr_open_cv_image = cv2.cvtColor(rgb_open_cv_image, cv2.COLOR_RGB2BGR)
    #bgr_open_cv_image = bgr_open_cv_image[:, :, ::-1].copy()
    
    cv2.imshow("Webcam Video",bgr_open_cv_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

webcam_video_stream.release()
cv2.destroyAllWindows()