from pathlib import Path
import pandas as pd
from scipy.stats import pearsonr, f_oneway

# ============================================
# 1. Definir rutas
# ============================================

BASE_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = BASE_DIR / "data" / "processed" / "ventas_poblacion_2023.csv"

# ============================================
# 2. Cargar dataset final
# ============================================

df = pd.read_csv(DATASET_PATH)

print("Dataset final cargado correctamente")
print(f"Dimensiones: {df.shape}")

# ============================================
# 3. Estadística descriptiva básica
# ============================================

print("\nResumen descriptivo de variables numéricas:")
print(df[["Quantity", "UnitPrice", "LineTotal"]].describe())

# ============================================
# 4. Correlación entre cantidad y facturación
# ============================================

corr, p_value_corr = pearsonr(df["Quantity"], df["LineTotal"])

print("\n--- CORRELACIÓN DE PEARSON ---")
print(f"Correlación entre Quantity y LineTotal: {corr:.4f}")
print(f"p-valor: {p_value_corr:.6f}")

if p_value_corr < 0.05:
    print("Conclusión: existe una relación estadísticamente significativa entre cantidad y facturación.")
else:
    print("Conclusión: no se observa una relación estadísticamente significativa entre cantidad y facturación.")

# ============================================
# 5. ANOVA por trimestre
# ============================================

# Agrupar facturación por factura para evitar trabajar solo a nivel de línea
facturas = (
    df.groupby(["InvoiceNo", "Quarter"], as_index=False)
    .agg(invoice_revenue=("LineTotal", "sum"))
)

q1 = facturas[facturas["Quarter"] == 1]["invoice_revenue"]
q2 = facturas[facturas["Quarter"] == 2]["invoice_revenue"]
q3 = facturas[facturas["Quarter"] == 3]["invoice_revenue"]
q4 = facturas[facturas["Quarter"] == 4]["invoice_revenue"]

anova_stat, p_value_anova = f_oneway(q1, q2, q3, q4)

print("\n--- ANOVA POR TRIMESTRE ---")
print(f"Estadístico F: {anova_stat:.4f}")
print(f"p-valor: {p_value_anova:.6f}")

if p_value_anova < 0.05:
    print("Conclusión: existen diferencias estadísticamente significativas entre trimestres.")
else:
    print("Conclusión: no se observan diferencias estadísticamente significativas entre trimestres.")

# ============================================
# 6. Medias por trimestre
# ============================================

print("\nMedia de facturación por factura y trimestre:")
print(facturas.groupby("Quarter")["invoice_revenue"].mean())



