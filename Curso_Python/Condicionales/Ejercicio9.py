while True:
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    tiene_entrada = bool

    if nombre == "Józef" and edad == 67 :
        tiene_entrada = True

        if edad >= 16 and tiene_entrada:
            print("Acceso permitido")
            break
        else:
            print("Acceso denegado")
    else:
        print("Intentelo de nuevo")