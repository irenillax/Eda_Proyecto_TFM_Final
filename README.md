# Proyecto Final - Análisis de Ventas Online Retail

Este proyecto recoge un análisis completo de un dataset de ventas de comercio electrónico, combinando trabajo en **Python** para la preparación y análisis de los datos, y **Power BI** para la construcción de un dashboard final orientado a negocio.

El objetivo no ha sido solo describir los datos, sino entender mejor el comportamiento de las ventas, detectar patrones relevantes y presentar conclusiones útiles de forma clara y visual.

Objetivos del proyecto:

- Limpiar y transformar el dataset original.
- Dejar trazable el proceso de preparación de los datos.
- Integrar una segunda fuente de población para enriquecer el análisis.
- Analizar ventas por país, mes, trimestre y producto.
- Incorporar un análisis estadístico básico para apoyar las conclusiones.
- Diseñar un dashboard en Power BI con una visión general y otra más analítica.

Dataset utilizados:
Se han utilizado dos fuentes de datos:

1. Online Retail:
   Dataset transaccional de ventas de comercio electrónico.

2. World Population:
   Dataset de población por país, utilizado para enriquecer el análisis y calcular métricas ajustadas por tamaño poblacional.

Estructura del proyecto:
- `data/raw/` → datasets originales.
- `data/processed/` → datasets procesados generados durante el flujo de trabajo.
- `notebooks/` → scripts en Python organizados por fases.
- `figures/` → gráficos generados en Python.
- `dashboards/` → archivo final de Power BI.
- `Informe/` → informe final en PDF.


Flujo de trabajo en Python:
El proyecto está dividido en varios scripts para mantener una estructura ordenada y reproducible:

- `01_carga_datos.py` → carga inicial de datos.
- `02_limpieza_ventas.py` → limpieza, tratamiento de nulos, duplicados, devoluciones y creación del dataset limpio.
- `03_eda_ventas.py` → análisis exploratorio inicial.
- `04_facturacion_ventas.py` → agregaciones de facturación por país.
- `05_facturacion_analisis.py` → análisis estadístico básico.
- `06_union_datasets.py` → unión con dataset de población y cálculo de facturación per cápita.
- `07_visualizaciones.py` → generación de visualizaciones en Python.


Principales transformaciones realizadas:
Durante la fase de limpieza y transformación se realizaron, entre otras, las siguientes acciones:

- Conversión de tipos de datos.
- Revisión y eliminación de duplicados.
- Eliminación de devoluciones y operaciones no válidas.
- Tratamiento de valores nulos en variables clave.
- Creación de variables derivadas como:
  - `LineTotal`
  - `Year`
  - `Month`
  - `Quarter`
  - `Hour`
  - `DayOfWeek`
  - `WeekOfYear`
  - `IsWeekend`
  - `HasCustomerID`
  - `IsReturn`

Además, se genera y guarda explícitamente el dataset limpio `online_retail_clean.csv`, de forma que el flujo de trabajo quede cerrado y trazable.


Análisis realizado:
Se ha trabajado tanto el análisis descriptivo como una parte de análisis estadístico básico.


Análisis descriptivo:
- facturación total.
- ventas por país.
- evolución mensual.
- análisis trimestral.
- productos con mayor facturación.
- relación entre cantidad vendida y facturación.
- comparación entre facturación total y facturación per cápita.


Análisis estadístico:
Para reforzar las conclusiones, se incorporan análisis sencillos pero justificados, entre ellos:

- correlación entre cantidad vendida y facturación,
- comparación de diferencias entre trimestres mediante análisis estadístico básico.


Dashboard en Power BI:
El dashboard final está dividido en dos páginas:

1. Visión General:
Incluye:
- facturación total.
- top 10 países por facturación.
- evolución mensual de la facturación.
- filtros por país, mes y año.

2. Análisis Avanzado:
Incluye:
- relación entre cantidad vendida y facturación.
- facturación por hora del día.
- top 10 productos por facturación.
- distribución de la facturación trimestral.

Se ha intentado mantener una presentación más homogénea en idioma, etiquetas y formato visual.

Principales insights:
Entre los hallazgos más relevantes del proyecto destacan:

- una fuerte concentración de la facturación en Reino Unido.
- mejor rendimiento comercial en el cuarto trimestre.
- existencia de productos con alta facturación sin necesidad de ser los más vendidos en volumen.
- utilidad de comparar facturación absoluta con métricas ajustadas por población.


Tecnologías utilizadas:
- Python.
- Pandas.
- Matplotlib.
- Seaborn.
- SciPy.
- Power BI.
- GitHub.


Cómo ejecutar el proyecto:
Orden recomendado de ejecución de scripts:
1. `01_carga_datos.py`
2. `02_limpieza_ventas.py`
3. `03_eda_ventas.py`
4. `04_facturacion_ventas.py`
5. `05_facturacion_analisis.py`
6. `06_union_datasets.py`
7. `07_visualizaciones.py`


Archivos principales de salida:
- `data/processed/online_retail_clean.csv`
- `data/processed/ventas_por_pais.csv`
- `data/processed/ventas_poblacion_2023.csv`
- dashboard final en `dashboards/`
- informe final en `Informe/`


Conclusión:
Este proyecto refleja un flujo completo de análisis de datos, desde la carga y limpieza del dataset hasta la visualización final y la comunicación de resultados. Además del análisis descriptivo, se ha reforzado la parte metodológica dejando el proceso más trazable, homogéneo y reproducible.
