import streamlit as st
import pandas as pd

from funciones_calculos import (calcular_liquido, calcular_bsw, calcular_gor, proyectar_produccion)
from funciones_datos import (filtrar_pozo, resumen_dataframe, exportar_excel)
from clase_pozo import Pozo
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

  class PozoLocal: # Cambiado temporalmente de nombre para no chocar con la importación global si fuera necesario

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
      total_produccion = self.petroleo + self.agua
      return total_produccion
  
    def proyectar_produccion(self, dias=30):
      produccion_proyectada = (self.petroleo + self.agua)*dias
      return produccion_proyectada
    
  nombre_pozo = st.text_input("Ingrese el nombre del pozo")
  campo_pozo = st.text_input("Ingrese el campo al que pertenece el pozo")
  petroleo = st.number_input("Ingrese la producción de petroleo", min_value = 0, max_value = 5000, value = 1000)
  agua = st.number_input("Ingrese la producción de agua", min_value = 0, max_value = 5000, value = 200)
    
  pozo = PozoLocal(nombre_pozo, campo_pozo, petroleo, agua)
    
  pozo.mostrar_informacion()

  st.write("producción total: ",pozo.produccion_total(), "BFPD")

  dias = st.number_input("Ingrese los dias a proyectar", min_value = 0, max_value = 365, value = 30)
  st.write(pozo.proyectar_produccion())

elif modulos == "Importación de librerías":
  st.title("Aplicación Modular con funciones y Clases")
  st.header("1. Uso de Funciones")

  petroleo = st.number_input(
      "Producción de petróleo",
      min_value=0.0,
      value=800.0
  )
    
  agua = st.number_input(
      "Producción de agua",
      min_value=0.0,
      value=200.0
  )
    
  dias = st.number_input(
      "Días",
      min_value=1,
      value=30
  )
    
  if st.button("Calcular"):
    liquido = calcular_liquido(
        petroleo,
        agua
    )
  
    bsw = calcular_bsw(
        petroleo,
        agua
    )
  
    proyeccion = proyectar_produccion(
        petroleo,
        dias
    )
  
    st.write("Producción líquida:", liquido)
    st.write("BSW:", round(bsw, 2), "%")
    st.write("Producción proyectada:", proyeccion)


  st.header("2. Crear un objeto Pozo")
    
  nombre = st.text_input(
      "Nombre del pozo",
      value="PZ-001"
  )
  
  campo = st.text_input(
      "Campo",
      value="SPE"
  )
  
  gas = st.number_input(
      "Producción de gas",
      min_value=0.0,
      value=450.0
  )
    
  if st.button("Crear objeto"):
    pozo = Pozo(
        nombre,
        campo,
        petroleo,
        agua,
        gas
    )

    st.write("Objeto creado:")
    st.write(pozo.mostrar_informacion())

    st.write(
        "Producción líquida:",
        pozo.produccion_liquida()
    )

    st.write(
        "BSW:",
        round(pozo.bsw(), 2)
    )

    st.write(
        "GOR:",
        round(pozo.gor(), 2)
    )
    
    
  st.header("3. Composición de clases")
    
  pozo_1 = Pozo(
      "PZ-001",
      "SPE",
      800,
      200,
      450
  )
  
  pozo_2 = Pozo(
      "PZ-002",
      "SPE",
      650,
      250,
      380
  )
  
  campo_auc = Campo("SPE")
  
  campo_auc.agregar_pozo(pozo_1)
  campo_auc.agregar_pozo(pozo_2)
  
  st.write(
      "Cantidad de pozos:",
      campo_auc.cantidad_pozos()
  )
  
  st.write(
      "Producción total de petróleo:",
      campo_auc.produccion_petroleo_total()
  )
  
  st.dataframe(
      pd.DataFrame(
          campo_auc.listar_pozos()
      )
  )
    
    
  st.header("4. Funciones aplicadas a datos")
    
  datos = pd.DataFrame({
      "pozo": [
          "PZ-001",
          "PZ-001",
          "PZ-002",
          "PZ-002"
      ],
      "petroleo": [
          800,
          790,
          650,
          640
      ]
  })
  
  st.dataframe(datos)
  
  pozo_seleccionado = st.selectbox(
      "Seleccione un pozo",
      datos["pozo"].unique()
  )
  
  resultado = filtrar_pozo(
      datos,
      pozo_seleccionado
  )
  
  st.write("Datos filtrados:")
  st.dataframe(resultado)
  
  st.write(
      "Resumen:",
      resumen_dataframe(datos)
  )
