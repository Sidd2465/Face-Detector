import streamlit as st
import cv2
import numpy as np
from detect_faces import detect_faces

st.title("👤 Face Detection Web App (Live Camera)")
st.markdown("Click 'Start Camera' to detect faces in real-time from your webcam.")

if 'camera_active' not in st.session_state:
    st.session_state['camera_active'] = False

start = st.button('Start Camera', key='start')
stop = st.button('Stop Camera', key='stop')
frame_window = st.empty()

if start:
    st.session_state['camera_active'] = True
if stop:
    st.session_state['camera_active'] = False

if st.session_state['camera_active']:
    cap = cv2.VideoCapture(0)
    while st.session_state['camera_active']:
        ret, frame = cap.read()
        if not ret:
            st.warning('Failed to grab frame from camera.')
            break
        result_img, face_count = detect_faces(frame)
        frame_window.image(result_img, channels="BGR", caption=f"Detected {face_count} face(s)")
        # Add a small delay to avoid high CPU usage
        if not st.session_state['camera_active']:
            break
    cap.release()
    cv2.destroyAllWindows()
