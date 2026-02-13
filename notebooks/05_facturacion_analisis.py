import pandas as pd

# Cargar dataset limpio
df = pd.read_csv("data/processed/online_retail_clean.csv")

# Asegurar datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Eliminar devoluciones
df = df[df["Quantity"] > 0]

# Crear facturación
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# ======================
# FACTURACIÓN POR PAÍS
# ======================
facturacion_pais = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFACTURACIÓN POR PAÍS (TOP 10):")
print(facturacion_pais.head(10))

# ======================
# FACTURACIÓN POR AÑO
# ======================
df["Year"] = df["InvoiceDate"].dt.year

facturacion_anio = df.groupby("Year")["Revenue"].sum()

print("\nFACTURACIÓN POR AÑO:")
print(facturacion_anio)

