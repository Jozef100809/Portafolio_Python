precio = int(input("Ingrese el precio del producto encontrado: "))

if precio >= 100:
    precio_final = precio * 0.90
else:
    precio_final = precio
    print("El precio final es: ", precio_final)