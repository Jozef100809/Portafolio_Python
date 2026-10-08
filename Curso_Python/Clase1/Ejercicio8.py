nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
nota1 = float(input("Ingrese su primera calificación: "))
nota2 = float(input("Ingrese su segunda calificación: "))
nota3 = float(input("Ingrese su tercera calificación: "))

promedio = (nota1 + nota2 + nota3) /3

if promedio >= 71:
    print("Tu promedio es:", promedio, "\n¡Aprobaste my friend", nombre,"!" "\nDe edad:", edad)
else:
    print("Tu promedio es:", promedio, "\n¡Reprobaste mi chavalín", nombre,"!" "\nDe edad:", edad)