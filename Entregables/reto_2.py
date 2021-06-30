from functools import cmp_to_key


def reto_2(cliente: int, nombre: str, direccion: 'str', telefono: int, miembro: bool, bd_clientes: dict) -> dict:
    
    if len(str(cliente)) != 8:
        return f"Ingrese un id de tipo valido."
    else:
        num1 = nombre.find(" ")
        primer_nombre = nombre[:num1].upper()
        apellido = nombre[num1+1:].upper()
        client ={
            'nombre': primer_nombre,
            'apellido': apellido,
            'direccion': direccion.lower(),
            'telefono': telefono,
            'membresia': miembro
        }

        if cliente in bd_clientes and client == clientes[cliente]:

            return f"El cliente {cliente} Se encuentra en la base de datos"
        
        elif cliente in bd_clientes and client != clientes[cliente]:
                        
            bd_clientes[cliente] = client
            return f"Cliente {cliente}, actualizado en la base de datos"

        elif cliente not in bd_clientes:
            new_client ={cliente: client}
            bd_clientes.update(new_client)
            return f"El cliente {cliente} se agregó a la base de datos"
 

def bd_clientes():

    clientes = {

        34043243: {
            'nombre': 'HOMERO',
            'apellido': 'SIMPSON',
            'direccion': 'avenida siempreviva 742',
            'telefono': 46637600,
            'membresia': False
        },
        42140704: {
            'nombre': 'MARGE',
            'apellido': 'SIMPSON',
            'direccion': 'siempreviva',
            'telefono': 46637600,
            'membresia': True
        },
        21015602: {
            'nombre': 'NED',
            'apellido': 'FLANDERS',
            'direccion': 'avenida siempreviva 864',
            'telefono': 63392730,
            'membresia': True
        },
        26677308: {
            'nombre': 'MOU',
            'apellido': 'SZYSLAK',
            'direccion': 'calle wualnut 668',
            'telefono': 76484377,
            'membresia': False
        },
        16361910: {
            'nombre': 'MONTY',
            'apellido': 'BURNS',
            'direccion': 'mansion burns',
            'telefono': 24275370,
            'membresia': True
        },
    }

    return clientes


clientes = bd_clientes()


##EJEMPLO1
print(reto_2(34043243,'Homero Simpson','AVENIDA SIEMPREVIVA 742',46637600,False, clientes))
print(clientes.get(34043243,'Cliente no se encuentra en DB.'))
##EJEMPLO2
#print(reto_2(42140704,'marge simpson','avenida siempreviva 742',46637600,True, clientes))
#print(clientes.get(42140704,'Cliente no se encuentra en DB.'))
##EJEMPLO3
#print(reto_2('cc24687900','pepito perez','CL Perezlandia ESQ.',3036052,True, clientes))
#print(clientes.get(24687900,'Cliente no se encuentra en BD.'))
##EJEMPLO4
#print(reto_2(24687900,'pepito perez','CL Perezlandia ESQ.',3036052,True, clientes))
#print(clientes.get(24687900,'Cliente no se encuentra en BD.'))


