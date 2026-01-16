class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío y debe ser una cadena.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero mayor o igual a cero.")
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un entero mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor total: ${self.calcular_valor_total():.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self):
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)


def menu_principal(inventario):
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")
            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(producto)
                else:
                    print("Producto no encontrado.")
            elif opcion == "3":
                print("\nLista de productos:")
                inventario.listar_productos()
            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: ${total:.2f}")
            elif opcion == "5":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except TypeError as te:
            print(f"Error de tipo: {te}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
