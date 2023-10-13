#Este codigo me permite entrar a un csv y divirlos en varios csv segun el valor de una columna
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('BD_Digitados V3.csv', delimiter=';')  # Indica el delimitador correcto (;) en tu archivo CSV

# Obtener valores únicos de la columna 'Lote' (asegúrate de que coincida con el nombre de columna en tu archivo)
lotes_unicos = df['Lote'].unique()

# Dividir el DataFrame en varios DataFrames según el valor de 'Lote' y guardarlos en archivos CSV
for lote in lotes_unicos:
    lote_df = df[df['Lote'] == lote]
    # Utilizar el valor del lote como nombre del archivo de salida
    nombre_archivo = f'Digitacion-4-{lote}.csv'
    lote_df.to_csv(nombre_archivo, index=False, sep=';')  # Indica el delimitador (;) en la salida también
