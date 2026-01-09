
# Proyecto EDA – Análisis Exploratorio de Datos

## Descripción del proyecto
Este proyecto consiste en la realización de un **Análisis Exploratorio de Datos (EDA)** utilizando **Python y Pandas**, aplicado a datos reales de campañas de marketing directo de una institución bancaria portuguesa.

El objetivo principal era **comprender el comportamiento de los clientes**, identificar patrones relevantes y extraer insights que ayuden a entender qué factores influyen en la contratación de un **depósito a plazo bancario**.

Por la imposibilidad de utilizar el archivo customer-details, el objetivo principal del análisis lo he tenido que modificar en **comprobar por empleado los indices de confianza del cliente, así como los contactos y duración con respecto a campañas anteriores**, analizando el comportamiento de los 11 empleados en estos indicadores.

---

## Objetivos del análisis
- Comprender la estructura y calidad de los datos
- Limpiar y transformar los datasets
- Realizar un análisis estadístico descriptivo
- Visualizar patrones, relaciones y distribuciones
- Extraer conclusiones basadas en datos

---

## Herramientas utilizadas
- **Python 3**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Visual Studio Code**
- **Git & GitHub**

---

## 📁 Estructura del repositorio

EDA/Proyecto EDA
    data
        row
            - bank.additional.csv
            - costumer-details.xlsx
        - data_limpios_nonulos.csv
        - data_limpios.csv
    notebooks
        - 01.eda_preliminar_optimo.ipynb
        - 02.limpieza.ipynb
        - 03.nulos.ipynb
        - 04.ab_testing.ipynb
    src
        - sp_eda.py
        - sp_limpieza.py
        - sp_abtest.py
    .gitignore
    README.md

---

## Descripción de los datasets

### bank-additional.csv

Dataset principal relacionado con campañas de marketing telefónico.

**Columnas principales:**
- `age`: Edad del cliente
- `job`: Profesión
- `marital`: Estado civil
- `education`: Nivel educativo
- `default`: Historial de impagos
- `housing`: Préstamo hipotecario
- `loan`: Préstamos personales
- `contact`: Tipo de contacto
- `duration`: Duración de la llamada (segundos)
- `campaign`: Número de contactos durante la campaña
- `pdays`: Días desde el último contacto
- `previous`: Contactos previos
- `poutcome`: Resultado de la campaña anterior
- `emp.var.rate`: Variación del empleo
- `cons.price.idx`: Índice de precios al consumidor
- `cons.conf.idx`: Índice de confianza del consumidor
- `euribor3m`: Tipo de interés
- `nr.employed`: Número de empleados
- `y`: Variable objetivo (suscripción)
- `date`, `contact_month`, `contact_year`
- `id_`: Identificador único

---

### customer-details.xlsx
Archivo Excel con información demográfica y de comportamiento del cliente, distribuido en 3 hojas (diferentes años).

**Columnas principales:**
- `Income`: Ingreso anual
- `Kidhome`: Número de niños en el hogar
- `Teenhome`: Número de adolescentes en el hogar
- `Dt_Customer`: Fecha de alta como cliente
- `NumWebVisitsMonth`: Visitas mensuales a la web
- `ID`: Identificador único del cliente

---

## Proceso de análisis (EDA)

### Carga de datos
- Lectura de archivos CSV y Excel(imposibilida de cargar este archivo)
- Exploración inicial con `sample()`, `info()` y `describe()`

---

### Limpieza y transformación de datos
- Identificación y tratamiento de valores nulos
- Conversión de tipos de datos (fechas y variables categóricas)
- Corrección de nombres
- Renombrado de columnas
- Creación de nuevas variables

---

### Análisis descriptivo
- Cálculo de estadísticos:
  - Media, mediana y desviación estándar
  - Distribuciones y percentiles
- Análisis de variables categóricas
- Correlación entre variables numéricas
- Comparativa entre clientes que contratan y no contratan el producto

---

### Visualización de datos
Se han utilizado gráficos para apoyar el análisis:
- Histogramas
- Boxplots
- Gráficos de barras

---

## 📈 Principales conclusiones
- El comportamiento entre los 11 empleados con respecto a las métricas analizadas tiene diferencias significativas.
- Los datos de las metricas analizadas no tiene una distribución normal, habiendo outliers en las 4 métricas, pudiendo distorcionar los resultados. 

---


