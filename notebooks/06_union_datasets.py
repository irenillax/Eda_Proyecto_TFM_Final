from pathlib import Path
import pandas as pd

# ============================================
# 1. Definir rutas
# ============================================

BASE_DIR = Path(__file__).resolve().parents[1]
SALES_PATH = BASE_DIR / "data" / "processed" / "online_retail_clean.csv"
POP_PATH = BASE_DIR / "data" / "raw" / "world_population.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "ventas_poblacion_2023.csv"

# ============================================
# 2. Cargar datasets
# ============================================

ventas = pd.read_csv(SALES_PATH)
poblacion = pd.read_csv(POP_PATH)

print("Dataset de ventas cargado:")
print(ventas.shape)

print("\nDataset de población cargado:")
print(poblacion.shape)

# ============================================
# 3. Preparar dataset de población
# ============================================

poblacion_2023 = poblacion[["Country Name", "2023"]].copy()

poblacion_2023 = poblacion_2023.rename(columns={
    "Country Name": "Country",
    "2023": "population_2023"
})

print("\nPoblación 2023 preparada:")
print(poblacion_2023.head())
print(poblacion_2023.shape)

# ============================================
# 4. Unir datasets
# ============================================

dataset_final = ventas.merge(
    poblacion_2023,
    on="Country",
    how="left"
)

# ============================================
# Eliminar filas sin población
# ============================================

dataset_final = dataset_final.dropna(subset=["population_2023"])

print("\nFilas después de eliminar países sin población:")
print(dataset_final.shape)

# ============================================
# 5. Crear variable derivada
# ============================================

dataset_final["revenue_per_capita"] = (
    dataset_final["LineTotal"] / dataset_final["population_2023"]
)

# ============================================
# 6. Guardar dataset final
# ============================================

dataset_final.to_csv(OUTPUT_PATH, index=False)

print("\nDataset final guardado correctamente")
print(f"Ruta de salida: {OUTPUT_PATH}")

print("\nDimensiones del dataset final:")
print(dataset_final.shape)

print("\nPrimeras filas del dataset final:")
print(dataset_final.head())

print("\nNulos por columna:")
print(dataset_final.isna().sum())
