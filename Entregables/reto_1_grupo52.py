""" def reto1(nombre,apellido):
    cursos = ["Python", "Java", "SQL", "JavaScript", "Html y CSS"]
    edad= int(input(f"Hola {nombre}, para la inscripción al curso necesitaremos los siguientes datos: \nEdad: "))
    curso_seleccionado = cursos[int(input(f"{cursos}\nSeleccione curso a inscribir: ")) -1]
    usuario = nombre[0] + apellido
    print(f"Bienvenido al curso de {curso_seleccionado}: \nTu usuarios es: {usuario}.")
    return [f"{nombre} {apellido}", edad, curso_seleccionado, usuario]

print(reto1("Andres", "Cepeda")) """
