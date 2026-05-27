import streamlit as st

st.title ("PROYECTO 1 – APLICACIÓN EN STREAMLIT")

st.sidebar.title("Selecciona")

st.write("Elaborado por: Carlos Piscoya Benites")
st.write("Módulo 1 – Python Fundamentals")


menu = st.sidebar.selectbox("Menú", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if Selecciona == "Home":
    st.write("Bienvenido a Home")
    st.image("PYTHON.png") 

elif menu == "Ejercicio 1":

    st.markdown("## 💰 Ejercicio 1 – Flujo de caja con listas")
    st.markdown("Registra ingresos y gastos y calcula el estado financiero.")

    # Inicializar lista en memoria
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Inputs
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=1.0)

    # Botón
    if st.button("Agregar movimiento"):
        if concepto != "" and valor > 0:
            movimiento = {
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            }
            st.session_state.movimientos.append(movimiento)
            st.success("Movimiento agregado correctamente")
        else:
            st.error("Completa todos los campos correctamente")

    # Mostrar tabla
    if st.session_state.movimientos:
        st.markdown("### 📋 Movimientos registrados")
        st.dataframe(st.session_state.movimientos)

        # Cálculos
        ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
        gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")
        saldo = ingresos - gastos

        st.markdown("### 📊 Resumen")

        st.metric("Total Ingresos", ingresos)
        st.metric("Total Gastos", gastos)
        st.metric("Saldo Final", saldo)

        # Estado
        if saldo > 0:
            st.success("Flujo de caja a favor ✅")
        elif saldo < 0:
            st.error("Flujo de caja en contra ❌")
        else:
            st.warning("Flujo de caja equilibrado ⚖️")

elif Selecciona == "Ejercicio 2":
    st.write("Bienvenido al ejercicio 2")

elif Selecciona == "Ejercicio 3":
    st.write("Bienvenido al ejercicio 3")

else:
    st.write("Bienvenido al ejercicio 4")
    
