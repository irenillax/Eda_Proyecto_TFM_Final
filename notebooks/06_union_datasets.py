import pandas as pd

# ===============================
# 1. Cargar datasets
# ===============================
ventas_pais = pd.read_csv("data/processed/ventas_por_pais.csv")
poblacion = pd.read_csv("data/raw/world_population.csv")

# ===============================
# 2. Limpiar y preparar población
# ===============================

# Nos quedamos solo con país y población 2023
poblacion_2023 = poblacion[["Country Name", "2023"]].copy()

# Renombrar columnas para poder unir
poblacion_2023 = poblacion_2023.rename(columns={
    "Country Name": "Country",
    "2023": "population_2023"
})

print("Población 2023:")
print(poblacion_2023.head())
print(poblacion_2023.shape)

# ===============================
# 3. Unir datasets
# ===============================
dataset_final = ventas_pais.merge(
    poblacion_2023,
    on="Country",
    how="left"
)

print("\nDataset final:")
print(dataset_final.head())
print(dataset_final.shape)

# ===============================
# 4. Guardar dataset final
# ===============================
dataset_final.to_csv(
    "data/processed/ventas_poblacion_2023.csv",
    index=False
)

print("✅ Dataset final guardado correctamente")

import pandas as pd

df = pd.read_csv("data/processed/ventas_poblacion_2023.csv")

print("Shape del dataset final:")
print(df.shape)

