import streamlit as st
import pandas as pd

from funciones_calculos import (calcular_liquido, calcular_bsw, calcular_gor, proyectar_produccion)
from funciones_datos import (filtrar_pozo, resumen_dataframe, exportar_excel)
from clases_pozo import Pozo
from clases_campo import Campo

st.title("Bootcamp Data Analytics for Oil & Gas")
st.sidebar.title("Parámetros")

modulos = st.sidebar.selectbox("seleccione un módulo", ["Introducción de variables", "Funciones", "POO","Importación de librerías"])

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

  class PozoLocal:
    def __init__(self,nombre, campo, petroleo, agua):
      self.nombre = nombre
      self.campo = campo
      self.petroleo = petroleo
      self.agua = agua
  
    def mostrar_informacion(self):
      st.write("Pozo:", self.nombre)
      st.write("Campo:", self.campo)
      st.write("Petroleo:", self.petroleo, "BOPD")
      st.write("Agua:", self.agua, "BWPD")
       
    def produccion_total(self):
      return self.petroleo + self.agua
  
    def proyectar_produccion(self, dias=30):
      return (self.petroleo + self.agua)*dias
    
  nombre_pozo = st.text_input("Ingrese el nombre del pozo", value="PZ-Local")
  campo_pozo = st.text_input("Ingrese el campo al que pertenece el pozo", value="SPE")
  petroleo = st.number_input("Ingrese la producción de petroleo", min_value = 0, max_value = 5000, value = 1000)
  agua = st.number_input("Ingrese la producción de agua", min_value = 0, max_value = 5000, value = 200)
    
  pozo = PozoLocal(nombre_pozo, campo_pozo, petroleo, agua)
  pozo.mostrar_informacion()

  st.write("producción total: ", pozo.produccion_total(), "BFPD")

  dias_proy = st.number_input("Ingrese los dias a proyectar", min_value = 0, max_value = 365, value = 30, key="dias_poo")
  st.write("Producción proyectada:", pozo.proyectar_produccion(dias_proy))

elif modulos == "Importación de librerías":
  st.title("Aplicación Modular con funciones y Clases")
  
  # --- SECCIÓN 1: USO DE FUNCIONES ---
  st.header("1. Uso de Funciones")

  petroleo = st.number_input("Producción de petróleo", min_value=0.0, value=800.0, key="oil_lib")
  agua = st.number_input("Producción de agua", min_value=0.0, value=200.0, key="water_lib")
  dias = st.number_input("Días", min_value=1, value=30, key="days_lib")
    
  # Inicializar estados de cálculo si no existen
  if "calc_liquido" not in st.session_state:
      st.session_state.calc_liquido = None
      st.session_state.calc_bsw = None
      st.session_state.calc_proy = None

  if st.button("Calcular", key="btn_calcular"):
    st.session_state.calc_liquido = calcular_liquido(petroleo, agua)
    st.session_state.calc_bsw = calcular_bsw(petroleo, agua)
    st.session_state.calc_proy = proyectar_produccion(petroleo, dias)
  
  if st.session_state.calc_liquido is not None:
    st.write("Producción líquida:", st.session_state.calc_liquido)
    st.write("BSW:", round(st.session_state.calc_bsw, 2), "%")
    st.write("Producción proyectada:", st.session_state.calc_proy)

  # --- SECCIÓN 2: CREAR UN OBJETO POZO ---
  st.header("2. Crear un objeto Pozo")
    
  nombre = st.text_input("Nombre del pozo", value="PZ-001", key="name_pozo_lib")
  campo = st.text_input("Campo", value="SPE", key="campo_pozo_lib")
  gas = st.number_input("Producción de gas", min_value=0.0, value=450.0, key="gas_lib")
    
  if "obj_pozo" not in st.session_state:
      st.session_state.obj_pozo = None

  if st.button("Crear objeto", key="btn_crear_obj"):
    st.session_state.obj_pozo = Pozo(nombre, campo, petroleo, agua, gas)

  if st.session_state.obj_pozo is not None:
    pozo_activo = st.session_state.obj_pozo
    st.write("Objeto creado:")
    st.write(pozo_activo.mostrar_informacion())
    st.write("Producción líquida:", pozo_activo.produccion_liquida())
    st.write("BSW:", round(pozo_activo.bsw(), 2))
    st.write("GOR:", round(pozo_activo.gor(), 2))
    
  # --- SECCIÓN 3: COMPOSICIÓN DE CLASES ---
  st.header("3. Composición de clases")
    
  pozo_1 = Pozo("PZ-001", "SPE", 800, 200, 450)
  pozo_2 = Pozo("PZ-002", "SPE", 650, 250, 380)
  
  campo_auc = Campo("SPE")
  campo_auc.agregar_pozo(pozo_1)
  campo_auc.agregar_pozo(pozo_2)
  
  st.write("Cantidad de pozos:", campo_auc.cantidad_pozos())
  st.write("Producción total de petróleo:", campo_auc.produccion_petroleo_total())
  st.dataframe(pd.DataFrame(campo_auc.listar_pozos()))
    
  # --- SECCIÓN 4: FUNCIONES APLICADAS A DATOS ---
  st.header("4. Funciones aplicadas a datos")
    
  datos = pd.DataFrame({
      "pozo": ["PZ-001", "PZ-001", "PZ-002", "PZ-002"],
      "petroleo": [800, 790, 650, 640]
  })
  
  st.dataframe(datos)
  pozo_seleccionado = st.selectbox("Seleccione un pozo", datos["pozo"].unique(), key="sb_pozo_datos")
  
  resultado = filtrar_pozo(datos, pozo_seleccionado)
  st.write("Datos filtrados:")
  st.dataframe(resultado)
  
  st.write("Resumen:", resumen_dataframe(datos))
