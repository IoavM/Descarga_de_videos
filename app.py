import streamlit as st
import requests

def download_video(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Error al descargar el video. Verifica la URL.")
        return None

st.title('Descargador de Videos desde GitHub')

url = st.text_input('Ingresa la URL del video en GitHub:')
if url:
    if st.button('Descargar Video'):
        video_data = download_video(url)
        if video_data:
            st.video(video_data, format='video/mp4')
            st.download_button(
                label="Descargar Video",
                data=video_data,
                file_name="video.mp4",
                mime="video/mp4"
            )
