# 📌 Función 1: Calcular descuento
def calcular_descuento(precio, porcentaje):
    return precio - (precio * porcentaje / 100)


# 📌 Función 2: Calcular interés simple
def calcular_interes(monto, tasa, tiempo):
    return monto * tasa * tiempo


# 📌 Función 3: Área de un círculo
def area_circulo(radio):
    return 3.1416 * (radio ** 2)


# 📌 Función 4: Sueldo neto con descuento
def sueldo_neto(sueldo, descuento):
    return sueldo - (sueldo * descuento / 100)


# 📌 Función 5: Total de compra
def total_compra(precio, cantidad):
    return precio * cantidad