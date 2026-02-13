import pandas as pd

# Cargar datasets en bruto
df_sales = pd.read_csv("data/raw/online_retail.csv")
df_population = pd.read_csv("data/raw/world_population.csv")

# Comprobaciones básicas
print("Dataset ventas:")
print(df_sales.shape)
print(df_sales.head())

print("\nDataset población:")
print(df_population.shape)
print(df_population.head())


