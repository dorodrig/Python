# Obtiene los nombres de las hojas de un archivo Excel sin contraseña
import openpyxl
# Ruta del archivo Excel
excel_file_path = r'C:\Users\David.Rodriguez\Desktop\Fasecolda\USUARIOS Y MENUS\Menú principal.xlsx'

# Abre el archivo Excel
workbook = openpyxl.load_workbook(excel_file_path)

# Obtiene los nombres de las hojas
sheet_names = workbook.sheetnames

# Itera a través de los nombres de las hojas e imprímelos
for sheet_name in sheet_names:
    print(sheet_name)

# Cierra el archivo Excel
workbook.close()