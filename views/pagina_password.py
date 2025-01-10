import streamlit as st

from scripts.password import password


def visual_convertidor():

    st.write("# Generador de contraseñas")
    valor = st.slider("Ingrese la cantidad de caracteres", 0 ,100 , 6, step=1)
    st.success(password(valor))