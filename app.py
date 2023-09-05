from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2
from keras.models import load_model
import numpy as np
import streamlit as st

np.set_printoptions(suppress=True)
model = None

if model == None:
    model = load_model("keras_Model.h5", compile=False)
    

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
class_names = open("labels.txt", "r").readlines()
	
		
     
class 	VideoProcessor:
    
    def recv(self,frame):
        frm = frame.to_ndarray(format = 'bgr24')
        
        #frm = cv2.flip(frm,1)
        image = cv2.resize(frm, (224, 224), interpolation=cv2.INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        
        image = (image / 127.5) - 1
        
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        
        if index == 1:
            cv2.putText(frm,'NO MASK',org=(100, 40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1, color=(0,0,255), thickness=1, lineType=cv2.LINE_AA)
        else:
            cv2.putText(frm,'MASK',org=(100, 40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1, color=(0,255,0), thickness=1, lineType=cv2.LINE_AA)

        
        
        
        
        
        return av.VideoFrame.from_ndarray(frm,format = 'bgr24')

webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	)