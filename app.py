import streamlit as st
from pytube import YouTube

st.set_page_config(page_title="YouTube Downloader", layout="centered")
st.title("📥 YouTube Downloader")

url = st.text_input("Cole aqui a URL do vídeo do YouTube")

if st.button("Baixar vídeo"):
    if url:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            st.write(f"🔻 Baixando: {yt.title}")
            stream.download()
            st.success("✅ Download concluído!")
        except Exception as e:
            st.error(f"❌ Erro: {e}")
    else:
        st.warning("⚠️ Insira uma URL válida.")
