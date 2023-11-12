from PIL import Image
import streamlit as st
from models import predict
import time

st.title("Gender Prediction")

fup = st.file_uploader("Upload a face image", type = "jpg", accept_multiple_files=False)

col1, col2 = st.columns([3, 1])

with col1:
    if fup is not None:
        img = Image.open(fup)
        st.image(img, caption = 'Uploaded Image', use_column_width = True)

with col2:
    if fup is not None:
        time.sleep(0.5)
        st.write("Prediction:")
        with st.spinner('Wait a seconds ...'):
            prediction = predict(fup)
            st.success(prediction)
        
