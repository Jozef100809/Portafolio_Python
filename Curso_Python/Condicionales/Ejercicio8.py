while True:
    usuario = str(input("Ingrese su nombre de usuario:"))
    contraseña = str(input("Inhgrese su contraseña:"))

    if usuario == "Józef" and contraseña == "python123":
        print("Acceso permitido")
        break
    else:
        print("Usuario o contraseña incorrectas, intente de nuevo")
