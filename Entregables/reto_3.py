def reto_3(dicccionario : dict) -> str:
    tutor :str = ''
    if dicccionario == None or dicccionario == {}:
        return None
    else:
        max_valor = max(tutores.values())
        for llave, valor in tutores.items():
            if max_valor == valor:
                tutor += llave + ', '
        tutor = tutor[:-2]
        return tutor


### otra versión
def reto_3(diccionario: dict) -> str:
   
    if diccionario:

        llaves = []
        valores = list(diccionario.values())
        max_v = max(valores)
        
        for k,v in diccionario.items():

            if v == max_v:
                llaves.append(k)
        
        return ', '.join(llaves)
    
    else:
        return None
    
#tutores = {'John': 16, 'Alex': 12, 'Bob': 8, 'Mike': 14, 'Molly': 14}
tutores = {}
#tutores = {'John': 12, 'Bob': 14, 'Mike': 16, 'Molly': 16, 'Adam': 10}
tutor = reto_3(tutores)
print("Best: {}".format(tutor))

