import streamlit as st
import pandas as pd

from funciones_calculos import (
    calcular_liquido,
    calcular_bsw,
    proyectar_produccion
)

from funciones_datos import (
    filtrar_pozo,
    resumen_dataframe
)

from clases_pozo import Pozo
from clases_campo import Campo


st.title("Aplicación Modular con Funciones y Clases")

st.header("1. Uso de funciones")

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
    value="Auca"
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
    "Auca",
    800,
    200,
    450
)

pozo_2 = Pozo(
    "PZ-002",
    "Auca",
    650,
    250,
    380
)

campo_auc = Campo("Auca")

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

