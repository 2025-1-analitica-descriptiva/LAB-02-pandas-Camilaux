import pandas as pd

def tbl0():
    """
    Carga el archivo `tbl0.tsv` y devuelve un DataFrame de pandas.
    """
    return pd.read_csv('files/input/tbl0.tsv', sep='\t')

def tbl1():
    """
    Carga el archivo `tbl1.tsv` y devuelve un DataFrame de pandas.
    """
    return pd.read_csv('files/input/tbl1.tsv', sep='\t')

def tbl2():
    """
    Carga el archivo `tbl2.tsv` y devuelve un DataFrame de pandas.
    """
    return pd.read_csv('files/input/tbl2.tsv', sep='\t')