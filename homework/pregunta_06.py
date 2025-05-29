"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from homework.read_data import tbl1

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    df = tbl1()

    # Obtener los valores únicos de la columna 'c4', convertirlos a mayúsculas y ordenarlos alfabéticamente
    valores_unicos = sorted(df['c4'].unique())
    valores_unicos = [valor.upper() for valor in valores_unicos if isinstance(valor, str)]

    return valores_unicos