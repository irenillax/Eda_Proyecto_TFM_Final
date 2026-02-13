import pandas as pd

# Cargar dataset limpio
df = pd.read_csv("data/processed/online_retail_clean.csv")

# Asegurar tipo datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# =========================
# ANÁLISIS TEMPORAL
# =========================

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month

ventas_por_anyo = df.groupby("Year")["Quantity"].sum()
print("\nVENTAS POR AÑO:")
print(ventas_por_anyo)

# ========================
# VENTAS POR MES
# ========================

ventas_por_mes = df.groupby(["Year", "Month"])["Quantity"].sum()

print("\nVENTAS POR MES:")
print(ventas_por_mes)

# ========================
# VENTAS POR PAÍS
# ========================

ventas_por_pais = df.groupby("Country")["Quantity"].sum().sort_values(ascending=False)

print("\nVENTAS POR PAÍS:")
print(ventas_por_pais.head(10))

# ========================
# TOP PRODUCTOS VENDIDOS
# ========================

top_productos = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP 10 PRODUCTOS MÁS VENDIDOS:")
print(top_productos.head(10))

# ========================
# DEVOLUCIONES
# ========================

devoluciones = df[df["Quantity"] < 0]

print("\nNÚMERO DE REGISTROS CON DEVOLUCIONES:")
print(devoluciones.shape[0])

# ========================
# DATASET SIN DEVOLUCIONES
# ========================

df_ventas = df[df["Quantity"] > 0]

print("\nDIMENSIONES SIN DEVOLUCIONES:")
print(df_ventas.shape)

# Ventas por año (sin devoluciones)
ventas_por_anyo_ok = df_ventas.groupby("Year")["Quantity"].sum()
print("\nVENTAS POR AÑO (SIN DEVOLUCIONES):")
print(ventas_por_anyo_ok)


