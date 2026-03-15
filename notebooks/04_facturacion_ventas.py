from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
CLEAN_PATH = BASE_DIR / "data" / "processed" / "online_retail_clean.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "ventas_por_pais.csv"

# ============================================
# 2. Cargar dataset limpio de ventas
# ============================================

df_sales = pd.read_csv(CLEAN_PATH)

print("Dataset limpio de ventas cargado correctamente")
print(f"Filas: {df_sales.shape[0]}")
print(f"Columnas: {df_sales.shape[1]}")

# ============================================
# 3. Facturación por país
# ============================================

ventas_pais = (
    df_sales
    .groupby("Country", as_index=False)
    .agg(
        total_revenue=("LineTotal", "sum"),
        total_quantity=("Quantity", "sum"),
        num_invoices=("InvoiceNo", "nunique")
    )
    .sort_values("total_revenue", ascending=False)
)

print("\nVentas por país:")
print(ventas_pais.head())

# ============================================
# 4. Guardar dataset agregado
# ============================================

ventas_pais.to_csv(OUTPUT_PATH, index=False)

print("\nDataset ventas_por_pais guardado correctamente")
print(f"Ruta de salida: {OUTPUT_PATH}")
print(f"Dimensiones: {ventas_pais.shape}")

# ============================================
# 5. Métricas generales
# ============================================

print("\nFacturación total global:")
print(df_sales["LineTotal"].sum())
