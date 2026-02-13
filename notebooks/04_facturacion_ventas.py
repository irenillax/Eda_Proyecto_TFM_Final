import pandas as pd

# ===============================
# CARGA DATASET LIMPIO DE VENTAS
# ===============================

df_sales = pd.read_csv(
    "data/processed/online_retail_clean.csv"
)

print("Dataset ventas cargado:")
print(df_sales.shape)
print(df_sales.head())

# ===============================
# FACTURACIÓN POR PAÍS
# ===============================

# Crear revenue
df_sales["revenue"] = df_sales["Quantity"] * df_sales["UnitPrice"]

# Agrupar ventas por país
ventas_pais = (
    df_sales
    .groupby("Country", as_index=False)
    .agg(
        total_revenue=("revenue", "sum"),
        total_quantity=("Quantity", "sum"),
        num_invoices=("InvoiceNo", "nunique")
    )
)

print("Ventas por país:")
print(ventas_pais.head())

# Guardar dataset intermedio
ventas_pais.to_csv(
    "data/processed/ventas_por_pais.csv",
    index=False
)



# Cargar dataset limpio
df = pd.read_csv("data/processed/online_retail_clean.csv")

# Asegurar datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Eliminar devoluciones
df = df[df["Quantity"] > 0]

# Crear columna facturación
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("DIMENSIONES DATASET FACTURACIÓN:")
print(df.shape)

print("\nFACTURACIÓN TOTAL:")
print(df["Revenue"].sum())

