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

if menu == "Ejercicio 1":

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor")

    if st.button("Agregar"):
        st.session_state.movimientos.append((concepto, tipo, valor))

    st.write(st.session_state.movimientos)

    ingresos = sum(v for c,t,v in st.session_state.movimientos if t=="Ingreso")
    gastos = sum(v for c,t,v in st.session_state.movimientos if t=="Gasto")

    st.write("Ingresos:", ingresos)
    st.write("Gastos:", gastos)
    st.write("Saldo:", ingresos - gastos)
