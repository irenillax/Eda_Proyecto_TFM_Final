import pandas as pd

# Cargar dataset de ventas en bruto
df_sales = pd.read_csv("data/raw/online_retail.csv")

# Información general del dataset
print("INFO DEL DATASET")
print(df_sales.info())

print("\nDIMENSIONES")
print(df_sales.shape)

print("\nPRIMERAS FILAS")
print(df_sales.head())

print("\nVALORES NULOS POR COLUMNA")
print(df_sales.isnull().sum())

print("\nFILAS DUPLICADAS")
print(df_sales.duplicated().sum())

print("\nTIPOS DE DATOS")
print(df_sales.dtypes)

print("\nTIPOS DE DATOS")
print(df_sales.dtypes)

# Convertir InvoiceDate a datetime
df_sales["InvoiceDate"] = pd.to_datetime(df_sales["InvoiceDate"])

import pandas as pd

# Cargar dataset de ventas en bruto
df_sales = pd.read_csv("data/raw/online_retail.csv")

# ✅ Convertir InvoiceDate a datetime (ESTO ES EL PUNTO 1)
df_sales["InvoiceDate"] = pd.to_datetime(df_sales["InvoiceDate"])

# Información general del dataset
print("INFO DEL DATASET")
print(df_sales.info())

print("\nDIMENSIONES")
print(df_sales.shape)

print("\nPRIMERAS FILAS")
print(df_sales.head())

print("\nVALORES NULOS POR COLUMNA")
print(df_sales.isnull().sum())

print("\nFILAS DUPLICADAS")
print(df_sales.duplicated().sum())

print("\nTIPOS DE DATOS")
print(df_sales.dtypes)

print("\nDATASET FINAL")
print(df_sales.shape)

import numpy as np

# Asegurar que InvoiceDate sea datetime
df_sales["InvoiceDate"] = pd.to_datetime(df_sales["InvoiceDate"], errors="coerce")

# ===============================
# VARIABLES DERIVADAS
# ===============================

# Facturación por línea
df_sales["LineTotal"] = df_sales["Quantity"] * df_sales["UnitPrice"]

# Variables temporales
df_sales["Year"] = df_sales["InvoiceDate"].dt.year
df_sales["Month"] = df_sales["InvoiceDate"].dt.month
df_sales["DayOfWeek"] = df_sales["InvoiceDate"].dt.dayofweek
df_sales["IsWeekend"] = df_sales["DayOfWeek"].isin([5, 6]).astype(int)
df_sales["Hour"] = df_sales["InvoiceDate"].dt.hour
df_sales["Quarter"] = df_sales["InvoiceDate"].dt.quarter
df_sales["WeekOfYear"] = df_sales["InvoiceDate"].dt.isocalendar().week.astype(int)

# Indicadores de negocio
df_sales["IsReturn"] = (df_sales["Quantity"] < 0).astype(int)
df_sales["HasCustomerID"] = df_sales["CustomerID"].notna().astype(int)

# Variables de texto
df_sales["DescLen"] = df_sales["Description"].fillna("").astype(str).str.len()
df_sales["DescWords"] = df_sales["Description"].fillna("").astype(str).str.split().str.len()

print("\nSHAPE FINAL TRAS FEATURE ENGINEERING:")
print(df_sales.shape)

# Guardar dataset con features (para Power BI)
df_sales.to_csv("data/processed/online_retail_features.csv", index=False)
print("Guardado: data/processed/online_retail_features.csv")






