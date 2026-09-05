import streamlit as st

st.title("Bootcamp Data Analytics for Oil & Gas")
st.sidebar.title("Parámetros")

modulos = st.sidebar.selectbox("seleccione un módulo", ["Introducción de variables", "Funciones"])

if modulos == "Introducción de variables":

pozo= "SPE-001"
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
