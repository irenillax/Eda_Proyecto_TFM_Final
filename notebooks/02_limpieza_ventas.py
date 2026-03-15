from pathlib import Path
import pandas as pd

# ============================================
# 1. Rutas
# ============================================
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_DIR / "data" / "raw" / "online_retail.csv"
CLEAN_PATH = BASE_DIR / "data" / "processed" / "online_retail_clean.csv"

# ============================================
# 2. Cargar dataset bruto
# ============================================
df = pd.read_csv(RAW_PATH, encoding="latin1")

print("Dataset bruto cargado correctamente")
print(f"Filas iniciales: {df.shape[0]}")
print(f"Columnas iniciales: {df.shape[1]}")

# ============================================
# 3. Revisión inicial
# ============================================
print("\nNulos por columna antes de limpiar:")
print(df.isna().sum())

duplicados_antes = df.duplicated().sum()
print(f"\nDuplicados antes de limpiar: {duplicados_antes}")

# ============================================
# 4. Conversión de tipos
# ============================================
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# ============================================
# 5. Limpieza
# ============================================

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar filas con nulos en variables críticas
df = df.dropna(subset=[
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "Country"
])

# Mantener CustomerID aunque tenga nulos
# porque luego se usa para indicar presencia/ausencia de cliente

# Eliminar devoluciones y operaciones no válidas
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df = df[~df["InvoiceNo"].astype(str).str.startswith("C", na=False)]


# ============================================
# 6. Variables derivadas
# ============================================
df["LineTotal"] = df["Quantity"] * df["UnitPrice"]

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Quarter"] = df["InvoiceDate"].dt.quarter
df["Hour"] = df["InvoiceDate"].dt.hour
df["DayOfWeek"] = df["InvoiceDate"].dt.dayofweek
df["WeekOfYear"] = df["InvoiceDate"].dt.isocalendar().week.astype(int)

df["IsWeekend"] = df["DayOfWeek"].isin([5, 6]).astype(int)
df["HasCustomerID"] = df["CustomerID"].notna().astype(int)
df["IsReturn"] = 0

# ============================================
# 7. Guardar dataset limpio
# ============================================
CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CLEAN_PATH, index=False)

print("\nDataset limpio guardado correctamente")
print(f"Ruta de salida: {CLEAN_PATH}")
print(f"Filas finales: {df.shape[0]}")
print(f"Columnas finales: {df.shape[1]}")

print("\nNulos por columna después de limpiar:")
print(df.isna().sum())



