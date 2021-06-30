import numpy as np

def reto_4(diccionario: dict) -> tuple:
    import numpy as np
    participantes = list(diccionario.keys())
    ma = [list(arquero.values()) for arquero in arqueros.values()]
    a = [list(map(lambda res: 5 if res < 6 else res, i)) for i in ma]
    b = np.array(a)
    c = np.round(np.average(b, axis=0), decimals=1)
    d = np.sum(b, axis=1)
    e = participantes[d.argmax()]
    return (a,b,c,d,e)
    """ print(a)
    print(b)
    print(c)
    print(d)
    print(e) """
   

#arqueros= {'Robin Hood': {'prueba 1': 8, 'prueba 2': 3, 'prueba 3': 9}, 'Odiseo': {
#'prueba 1': 5, 'prueba 2': 7, 'prueba 3': 9}, 'Green Arrow': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}}
arqueros= {'Odiseo': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Hawk Eye': {
'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Katniss': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}}
#arqueros= {'Robin': {'prueba 1': 9, 'prueba 2': 9, 'prueba 3': 9}}
a, b, c, d, e = reto_4(arqueros)
#reto_4(arqueros)
a = f"Resultados: {a}"
b = f"Matriz: \n{b}"
c = f"Promedio: {c}"
d = f"Puntajes: {d}"
e = f"Seleccionado: {e}"
print(a, b, c, d, e, sep='\n')



