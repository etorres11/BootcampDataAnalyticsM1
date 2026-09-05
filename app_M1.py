import streamlit as st

st.title("Bootcamp Data Analytics for Oil & Gas")
st.sidebar.title("Parámetros")

modulos = st.sidebar.selectbox("seleccione un módulo", ["Introducción de variables", "Funciones"], "POO")

if modulos == "Introducción de variables":

  pozo = "SPE-001"
  petroleo_bpd = 1250
  agua_bpd = 350.50
  status = True
  liquido_total_bpd = petroleo_bpd + agua_bpd
  corte_agua_pct = (agua_bpd / liquido_total_bpd) * 100

  st.write(pozo)
  st.write(petroleo_bpd)
  st.write(agua_bpd)
  st.write(status)
  st.write(liquido_total_bpd)
  st.write(corte_agua_pct)

elif modulos == "Funciones":

  def calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales):
    """
    Calcula el caudal de petróleo mediante la ecuación de Vogel.

    Parámetros:
    caudal_maximo (float): Caudal máximo teórico del pozo, BPD.
    presion_yacimiento (float): Presión promedio del yacimiento, psi.
    presion_fondo (float): Presión de fondo fluyente, psi.
    decimales (int): Número de decimales del resultado.

    Retorna:
    float: Caudal estimado de petróleo, BPD.
    """

    relacion_presion = presion_fondo / presion_yacimiento

    caudal = caudal_maximo * (
        1 - 0.2 * relacion_presion - 0.8 * relacion_presion**2
    )

    return round(caudal, decimales)

  caudal_maximo = st.number_input("Ingrese el caudal máximo", min_value = 0, max_value = 5000, value = 1200)
  presion_yacimiento = st.number_input("Ingrese la presión el yacimiento", min_value = 0, max_value = 9000, value = 3000)
  presion_fondo = st.number_input("Ingrese la presión de fondo fluyente", min_value = 0, max_value = 9000, value = 1500)
  decimales = st.slider("Selecciones la cantidad de decimales para su resultado", min_value = 0, max_value = 4, value = 2)

  caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)

  st.write("El caudal es: ", caudal)

elif modulos == "POO":

  class Pozo:

    def __init__(self,nombre, campo, petroleo, agua):
      self.nombre = nombre
      self.campo = campo
      self.petroleo = petroleo
      self.agua = agua
  
    def mostrar_informacion(self):
      print("Pozo:", self.nombre)
      print("Campo:", self.campo)
      print("Petroleo:", self.petroleo, "BPD")
      print("Agua:", self.agua, "BPD")
  
    def produccion_total(self):
      total_produccion = self.petroleo + self.agua
      return total_produccion
  
    def proyectar_produccion(self, dias=30):
      produccion_proyectada = (self.petroleo + self.agua)*dias
      return produccion_proyectada
    
    nombre_pozo = st.text_input("Ingrese el nombre del pozo")
    campo_pozo = st.text_input("Ingrese el campo al que pertenece el pozo")
    petroleo = st.number_input("Ingrese la producción de petroleo", min_value = 0, max_value = 5000, value = 1000)
    agua = st.number_input("Ingrese la producción de agua", min_value = 0, max_value = 5000, value = 200)
    
    pozo = pozo(nombre_pozo, campo_pozo, petroleo, agua)
    
    st.write (pozo.mostrar_informacion())

st.write(pozo.produccion_total)

dias = st.number_input("Ingrese los dias a proyectar", min_value = 0, max_value = 365, value = 30)

st.write(pozo.proyectar_produccion())
