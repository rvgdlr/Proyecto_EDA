import pandas as pd

def comas (df, col):
    df[col] = df[col].str.replace(',', '.')
    df[col] = df[col].astype('float64')


def enteros(df, col):
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].astype('Int64') 