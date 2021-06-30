""" import numpy as np
import pandas as pd

archivo = pd.read_csv(
    'https://raw.githubusercontent.com/JParrales/mision-tic-2021-ciclo_python/master/G25/Reto%205/notas.csv')

archivo['PUNTAJE'] = archivo['MATEMATICA'] + archivo['LENGUAJE'] + \
    archivo['CIENCIAS'] + archivo['CIUDADANAS'] + archivo['IDIOMAS']

by_puntaje = archivo.sort_values('PUNTAJE', ascending=False).head()
tabla_1 = by_puntaje[['ESTUDIANTE', 'PUNTAJE']]
puestos = [1,2,3,4,5]
tabla_1 = by_puntaje.set_index(np.array(puestos))
tabla_1.index.name = 'PUESTO'

promedio = archivo.mean()
promedio.round(2)

tabla_2 = pd.DataFrame(promedio)

tabla_2.columns = ['PROMEDIO']
tabla_2.index.name = 'PRUEBAS'

print(tabla_1)
print(tabla_2) """

def reto_5(ruta_archivo: str) -> list:
    import numpy as np
    import pandas as pd

    archivo = pd.read_csv(ruta_archivo)

    archivo['PUNTAJE'] = archivo['MATEMATICA'] + archivo['LENGUAJE'] + archivo['CIENCIAS'] + archivo['CIUDADANAS'] + archivo['IDIOMAS']
    puestos = [1,2,3,4,5]
    by_puntaje = archivo.sort_values('PUNTAJE', ascending=False).head().set_index(np.array(puestos))
    by_puntaje.index.name='PUESTO'
    top = by_puntaje[['ESTUDIANTE', 'PUNTAJE']]

    medio = archivo.mean()
    medio.round(2)

    promedio = pd.DataFrame(medio.round(2))

    promedio.columns = ['PROMEDIO']
    promedio.index.name = 'PRUEBAS'
    return [top,promedio]

top, promedio = reto_5('https://raw.githubusercontent.com/JParrales/mision-tic-2021-ciclo_python/master/G85/Reto%205/resultados.csv')
print('Tabla 1:\n', top)
print('\nTabla 2:\n', promedio)