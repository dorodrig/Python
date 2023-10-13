#Lectura de archivos Excel con contraseña en Python
import xlwings as xw

# Ruta del archivo Excel
excel_file_path = r'C:\Users\David.Rodriguez\Desktop\Fasecolda\USUARIOS Y MENUS\Estadisticas 2017-2.xlsx'

# Contraseña para el archivo Excel (puedes cambiar esto a tu contraseña)
password = '79739564'

try:
    # Abre el archivo Excel con contraseña
    workbook = xw.Book(excel_file_path, password=password)

    # Obtiene los nombres de las hojas
    sheet_names = [sheet.name for sheet in workbook.sheets]

    # Itera a través de los nombres de las hojas e imprímelos
    for sheet_name in sheet_names:
        print(sheet_name)

    # Cierra el archivo Excel
    workbook.close()

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
