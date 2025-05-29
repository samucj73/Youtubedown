import streamlit as st
from pytube import YouTube
import os

st.set_page_config(page_title="YouTube Downloader", layout="centered")
st.title("📥 YouTube Downloader")

url = st.text_input("Cole a URL do vídeo do YouTube")

if st.button("Baixar vídeo"):
    if url:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            st.info(f"🔻 Baixando: {yt.title}...")
            output_path = stream.download()
            st.success("✅ Download concluído!")
            with open(output_path, "rb") as f:
                st.download_button(
                    label="📁 Baixar arquivo .mp4",
                    data=f,
                    file_name=os.path.basename(output_path),
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"❌ Erro ao baixar: {e}")
    else:
        st.warning("⚠️ Insira uma URL válida.")
