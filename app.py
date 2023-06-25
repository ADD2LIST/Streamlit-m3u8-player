import streamlit as st

video_url = st.text_input("Enter the M3U8 URL")

if video_url:
    st.video(video_url)
  
