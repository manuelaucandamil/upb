import sqlite3
import customtkinter
from database import agregar_producto,mostrar_inventario,actualizar_producto,buscar_producto,eliminar_producto, conn

def menu():
    while True:
        print("\n--- Menú Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            codigo=input("Ingrese el codigo del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el Precio: "))
            agregar_producto(codigo,nombre, cantidad, precio)

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco si no desea cambiar): ")
            precio = input("Nuevo precio (deje en blanco si no desea cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            actualizar_producto(nombre, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(nombre)

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
    conn.close()