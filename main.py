import pandas as pd
from pandasgui import show

# Ruta del archivo Excel
ruta = "excel.xlsx"
# Configurar Pandas para que muestre todas las columnas
pd.set_option('display.max_columns', None)

# Definir tus propios encabezados
mi_cabezera = ["Producto_id", "Promo", "Bono", "Bono_id"]

# Leer el archivo Excel e ignorar el encabezado original
pd
df = pd.read_excel(ruta, header=None, names=mi_cabezera)

show(df)

