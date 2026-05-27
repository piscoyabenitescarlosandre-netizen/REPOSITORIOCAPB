import streamlit as st

st.title ("PROYECTO 1 – APLICACIÓN EN STREAMLIT")

st.sidebar.title("Selecciona")

st.write("Elaborado por: Carlos Piscoya Benites")
st.write("Módulo 1 – Python Fundamentals")


Selecciona = st.sidebar.selectbox("Menú", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if Selecciona == "Home":
    st.write("Bienvenido a Home")
st.image("PYTHON.png")

elif Selecciona == "Ejercicio 1":
    st.write("Bienvenido al ejercicio 1")

elif Selecciona == "Ejercicio 2":
    st.write("Bienvenido al ejercicio 2")

elif Selecciona == "Ejercicio 3":
    st.write("Bienvenido al ejercicio 3")

else:
    st.write("Bienvenido al ejercicio 4")
    
