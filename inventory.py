from models import Inventario

def menu():
    inv = Inventario()

    while True:
        print("\n=== 🛒 Supermercado - Gestión de Inventario ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.agregar_producto(nombre, cantidad, precio)
            print("✅ Producto añadido con éxito")

        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            inv.eliminar_producto(id_producto)
            print("🗑 Producto eliminado")

        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto: "))
            cantidad = int(input("Nueva cantidad (Enter para omitir): ") or -1)
            precio = float(input("Nuevo precio (Enter para omitir): ") or -1)
            inv.actualizar_producto(id_producto,
                                    cantidad if cantidad != -1 else None,
                                    precio if precio != -1 else None)
            print("♻ Producto actualizado")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inv.buscar_producto(nombre)
            for p in productos:
                print(p)

        elif opcion == "5":
            productos = inv.mostrar_productos()
            print("\n=== Inventario ===")
            for p in productos:
                print(p)

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    menu()
