def eliminar_valor(lista, val):
    try:
        lista.remove(val)
        print(f"Valor {val} eliminado con mucho éxito.")
    except ValueError:
        print(f"Error: El valor {val} no existe en la lista.")

def main():
    try:
        entrada_usuario = input("Ingrese una lista de valores enteros separados por espacio, no por comas: ")
        lista_valores = list(map(int, entrada_usuario.split()))

        print("Lista original:", lista_valores)

        valor_a_eliminar = int(input("Por favor, ingrese el valor que desea eliminar: "))

        eliminar_valor(lista_valores, valor_a_eliminar)

        print("Lista resultante:", lista_valores)

    except ValueError:
        print("Error: Ingrese valores enteros válidos.")

if __name__ == "__main__":
    main()
