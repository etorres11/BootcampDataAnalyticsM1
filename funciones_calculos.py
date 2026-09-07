def calcular_liquido(petroleo, agua):
    return petroleo + agua

def calcular_bsw(petroleo, agua):
    liquido = calcular_liquido(petroleo, agua)

    if liquido == 0:
        return 0

    return (agua / liquido) * 100

def calcular_gor(gas, petroleo):
    if petroleo == 0:
        return 0

    return (gas * 1000) / petroleo

def proyectar_produccion(produccion_diaria, dias):
    return produccion_diaria * dias