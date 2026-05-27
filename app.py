import streamlit as st

st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")

st.sidebar.title("Selecciona")

st.write("Elaborado por: Carlos Piscoya Benites")
st.write("Módulo 1 – Python Fundamentals")

# SOLO UNA VARIABLE
menu = st.sidebar.selectbox(
    "Menú",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# HOME
if menu == "Home":
    st.write("Bienvenido a Home")
    st.image("PYTHON.png")

# EJERCICIO 1
elif menu == "Ejercicio 1":

    st.markdown("## 💰 Ejercicio 1 – Flujo de caja con listas")
    st.markdown("Registra ingresos y gastos y calcula el estado financiero.")

    # Inicializar lista
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

    # Mostrar datos
    if st.session_state.movimientos:
        st.markdown("### 📋 Movimientos registrados")
        st.dataframe(st.session_state.movimientos)

        ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
        gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")
        saldo = ingresos - gastos

        st.markdown("### 📊 Resumen")

        st.metric("Total Ingresos", ingresos)
        st.metric("Total Gastos", gastos)
        st.metric("Saldo Final", saldo)

        if saldo > 0:
            st.success("Flujo de caja a favor ✅")
        elif saldo < 0:
            st.error("Flujo de caja en contra ❌")
        else:
            st.warning("Flujo de caja equilibrado ⚖️")

# EJERCICIO 2
elif menu == "Ejercicio 2":

    import numpy as np
    import pandas as pd

    st.markdown("## 📦 Ejercicio 2 – Registro con NumPy y DataFrame")
    st.markdown("Registra productos y visualiza los datos en un DataFrame.")

    # Inicializar arrays en session_state
    if "nombres" not in st.session_state:
        st.session_state.nombres = []
        st.session_state.categorias = []
        st.session_state.precios = []
        st.session_state.cantidades = []
        st.session_state.totales = []

    # Inputs
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    total = precio * cantidad

    # Botón
    if st.button("Agregar registro"):
        if nombre != "" and precio > 0 and cantidad > 0:

            st.session_state.nombres.append(nombre)
            st.session_state.categorias.append(categoria)
            st.session_state.precios.append(precio)
            st.session_state.cantidades.append(cantidad)
            st.session_state.totales.append(total)

            st.success("Registro agregado correctamente")
        else:
            st.error("Completa todos los campos correctamente")

    # Mostrar DataFrame
    if st.session_state.nombres:

        # Convertir a arrays de NumPy
        nombres_np = np.array(st.session_state.nombres)
        categorias_np = np.array(st.session_state.categorias)
        precios_np = np.array(st.session_state.precios)
        cantidades_np = np.array(st.session_state.cantidades)
        totales_np = np.array(st.session_state.totales)

        # Crear DataFrame
        df = pd.DataFrame({
            "Producto": nombres_np,
            "Categoría": categorias_np,
            "Precio": precios_np,
            "Cantidad": cantidades_np,
            "Total": totales_np
        })

        st.markdown("### 📊 Registros")
        st.dataframe(df)

# EJERCICIO 3
elif menu == "Ejercicio 3":

    import pandas as pd
    from libreria_funciones_proyecto1 import 

    st.markdown("## ⚙️ Ejercicio 3 – Uso de funciones externas")
    st.markdown("Ejecuta funciones desde una librería externa y guarda resultados.")

    # Inicializar historial
    if "historial" not in st.session_state:
        st.session_state.historial = []

    # Selector de función (aunque uses una, igual lo piden)
    opcion = st.selectbox("Selecciona función", ["Calcular descuento"])

    # Inputs (depende de tu función)
    precio = st.number_input("Precio", min_value=0.0)
    porcentaje = st.number_input("Porcentaje de descuento", min_value=0.0)

    # Botón
    if st.button("Ejecutar función"):

        resultado = calcular_descuento(precio, porcentaje)

        st.write("Resultado:", resultado)

        # Guardar en historial
        registro = {
            "Función": opcion,
            "Precio": precio,
            "Porcentaje": porcentaje,
            "Resultado": resultado
        }

        st.session_state.historial.append(registro)

    # Mostrar historial
    if st.session_state.historial:
        df_historial = pd.DataFrame(st.session_state.historial)

        st.markdown("### 📊 Historial de resultados")
        st.dataframe(df_historial)

# EJERCICIO 4
elif menu == "Ejercicio 4":
    st.write("Bienvenido al ejercicio 4")
