import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. Carga dataset final
# ==============================
df = pd.read_csv("data/processed/ventas_poblacion_2023.csv")

print("Dataset cargado:")
print(df.head())
print(df.shape)

# ==============================
# 2. TOP 10 países por facturación total
# ==============================
top_facturacion = (
    df.sort_values("total_revenue", ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_facturacion,
    x="total_revenue",
    y="Country",
    palette="viridis"
)
plt.title("Top 10 países por facturación total")
plt.xlabel("Facturación total")
plt.ylabel("País")
plt.tight_layout()
plt.savefig("figures/top_10_facturacion_total.png", dpi=300)
plt.show()
plt.close()

# ==============================
# 3. TOP 10 países por número de facturas
# ==============================
top_invoices = (
    df.sort_values("num_invoices", ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_invoices,
    x="num_invoices",
    y="Country",
    palette="crest"
)
plt.title("Top 10 países por número de facturas")
plt.xlabel("Número de facturas")
plt.ylabel("País")
plt.tight_layout()
plt.savefig("figures/top_10_num_facturas.png", dpi=300)
plt.show()
plt.close()

# ==============================
# 4. Facturación per cápita
# ==============================
df["revenue_per_capita"] = df["total_revenue"] / df["population_2023"]

top_pc = (
    df.sort_values("revenue_per_capita", ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_pc,
    x="revenue_per_capita",
    y="Country",
    palette="magma"
)
plt.title("Top 10 países por facturación per cápita")
plt.xlabel("Facturación per cápita")
plt.ylabel("País")
plt.tight_layout()
plt.savefig("figures/top_10_facturacion_per_capita.png", dpi=300)
plt.show()
plt.close()

print("✅ Todas las gráficas creadas y guardadas en /figures")

