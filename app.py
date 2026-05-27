import streamlit as st

st.title ("PROYECTO 1 – APLICACIÓN EN STREAMLIT")

st.sidebar.title("Selecciona")

st.write("Elaborado por: Carlos Piscoya Benites")
st.write("Módulo 1 – Python Fundamentals")


Selecciona = st.sidebar.selectbox("Menú", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if menu == "Home":
    st.title("Mi Proyecto en Streamlit")
    st.write("Nombre: Carlos Piscoya")
    st.write("Módulo: Python Fundamentals")
    st.write("Descripción: Aplicación con ejercicios básicos")

elif menu == "Ejercicio 1":
     st.write("Ejercicio 1")

elif menu == "Ejercicio 2":
     st.write("Ejercicio 2")

elif menu == "Ejercicio 3":
     st.write("Ejercicio 3")

else :
     st.write("Ejercicio 4")
