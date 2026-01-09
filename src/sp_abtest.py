import pandas as pd
import scipy.stats as stats

def exploracion_df_abtest(df, col_control):
    for categoria in df[col_control].unique():
        df_filtrado = df[df[col_control] == categoria]

        print(
            f'Los principales estadísticos de las columnas categóricas para el grupo {categoria} son:'
        )
        display(df_filtrado.describe(include='object').T)

        print(
            f'Los principales estadísticos de las columnas numéricas para el grupo {categoria} son:'
        )
        display(df_filtrado.describe(include='number').T)

        print('------------------------------------------------------------------------------------------------------')


def normalidad (df, lista_metricas):
    for metrica in lista_metricas:
        statistic, p_value = stats.shapiro(df[metrica])

        if p_value > 0.05:
            print(f'Para la columna {metrica}los datos SI siguen una distribución normal')
        else:
            print(f'Para la columna {metrica} los datos NO siguen una distribución normal')


def homocedasticidad (df, col_control, lista_metricas):
        for metrica in lista_metricas:
            df_empleados = []
            for valor in df[col_control].unique():
                df_empleados.append(df[df[col_control] == valor][metrica])

            statistic, p_value = stats.levene(*df_empleados)

            if p_value>0.05:
                print(f'Para la columna {metrica} las varianzas son homogéneas entre empleados, es decir, SI hay homocedsticidad')
            else:
                print(f'Para la columna {metrica} las varianzas no son homogéneas entre empleados, es decir, NO hay homocedsticidad')



def test_kruskal(df, col_control, metricas): 
    empleados = [ df[df[col_control] == valor][metricas].dropna() 
                 for valor in df[col_control].unique()] 
    # Test Kruskal-Wallis 
    statistic, p_value = stats.kruskal(*empleados) 
    if p_value > 0.05: 
        print(f'Para la métrica cons_con {metricas}, NO hay diferencias significativas entre los distintos niveles de empleados') 
    else: 
        print(f'Para la métrica {metricas}, SÍ hay diferencias significativas entre los distintos niveles de empleados')