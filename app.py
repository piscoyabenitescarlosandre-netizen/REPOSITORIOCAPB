import streamlit as st

st.title ("PROYECTO 1 – APLICACIÓN EN STREAMLIT")

st.sidebar.title("Selecciona")

st.write("Elaborado por: Carlos Piscoya Benites")
st.write("Módulo 1 – Python Fundamentals")


Selecciona = st.sidebar.selectbox("Menú", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
