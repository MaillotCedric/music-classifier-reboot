import streamlit as st
import boite_outils as bo

uploaded_file = st.file_uploader("Choisir une musique")
if uploaded_file:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    with open(f"./Upload/{uploaded_file.name}", 'wb') as f: 
        f.write(bytes_data)
        st.write(f"Musique identifiée comme étant du **{bo.get_genre_musical()}**")
