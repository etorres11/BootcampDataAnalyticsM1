import pandas as pd

def cargar_csv(ruta):
    return pd.read_csv(ruta)

def filtrar_pozo(df, nombre_pozo):
    return df[df["pozo"] == nombre_pozo]

def resumen_dataframe(df):
    return {
        "filas": len(df),
        "columnas": len(df.columns),
        "pozos": df["pozo"].nunique() if "pozo" in df.columns else 0
    }

def exportar_excel(df, nombre_archivo="datos_exportados.xlsx"):
    df.to_excel(nombre_archivo, index=False)
    return nombre_archivo
