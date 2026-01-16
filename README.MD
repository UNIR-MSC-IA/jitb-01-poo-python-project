
# Requisitos

1. **Crear una clase `Producto`** con atributos para:
	- nombre
	- precio
	- cantidad
2. **Implementar métodos** para:
	- añadir
	- actualizar
	- mostrar información de productos
3. **Desarrollar una clase `Inventario`** que gestione una colección de productos
4. **Implementar operaciones de inventario:**
	- añadir producto
	- buscar por nombre
	- calcular valor total
5. **Manejar excepciones** para entradas inválidas (cantidades negativas, nombres vacíos, etc.)
6. **Crear un menú interactivo** simple para probar las funcionalidades
7. **Mostrar resultados** de operaciones por consola de manera formateada
8. **Validar** que los datos ingresados sean del tipo correcto

---

# Instrucciones

1. Crea un archivo llamado `sistema_inventario.py` donde implementarás todo el código del sistema.
2. Define la clase **Producto** con un método constructor que inicialice los atributos:
	- `nombre` (`str`)
	- `precio` (`float`)
	- `cantidad` (`int`)
	Incluye validaciones para que:
	- el precio sea mayor o igual que cero
	- el nombre no esté vacío
	- la cantidad sea mayor o igual a cero
3. Añade a la clase **Producto** los siguientes métodos:
	- `actualizar_precio(nuevo_precio)`: para modificar el precio validando que sea mayor o igual que cero
	- `actualizar_cantidad(nueva_cantidad)`: para modificar la cantidad validando que sea mayor o igual a cero
	- `calcular_valor_total()`: que devuelva el valor total (precio × cantidad)
	- `__str__()`: para mostrar la información del producto de forma legible
4. Crea la clase **Inventario** con un constructor que inicialice una lista vacía para almacenar productos.
5. Implementa en la clase **Inventario** los siguientes métodos:
	- `agregar_producto(producto)`: para añadir un objeto de tipo Producto a la lista
	- `buscar_producto(nombre)`: para encontrar un producto por su nombre (búsqueda exacta, insensible a mayúsculas/minúsculas). Debe devolver el producto si lo encuentra o `None` si no existe
	- `calcular_valor_inventario()`: para sumar el valor total de todos los productos
	- `listar_productos()`: para mostrar todos los productos del inventario
6. Implementa un manejo de excepciones utilizando bloques `try-except` para capturar errores como valores inválidos (cantidades negativas), tipos de datos incorrectos o productos no encontrados.
7. Crea una función `menu_principal()` que muestre opciones al usuario:
	1. Agregar producto
	2. Buscar producto
	3. Listar productos
	4. Calcular valor total del inventario
	5. Salir
	y procese la entrada del usuario en un bucle hasta que elija salir.
8. En la sección principal del programa (bajo `if __name__ == "__main__":`), instancia un objeto de la clase Inventario y llama a la función `menu_principal()` para iniciar la aplicación.

---

# Criterios de evaluación

| Criterio                                 | Descripción                                                                                                                        | Peso   |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------|
| Implementación de la clase Producto       | Correcta definición de la clase Producto con sus atributos (nombre, precio, cantidad) y métodos (actualizar_precio, actualizar_cantidad, calcular_valor_total, __str__). Incluye validaciones básicas para los datos. | 30%    |
| Implementación de la clase Inventario     | Correcta implementación de la clase Inventario con métodos para agregar productos, buscar por nombre, calcular el valor total del inventario y listar todos los productos. | 30%    |
| Manejo de excepciones                     | Implementación de bloques try-except para manejar errores como valores inválidos (cantidades negativas), tipos de datos incorrectos o productos no encontrados. | 20%    |
| Interfaz de usuario y funcionalidad        | Desarrollo de un menú interactivo que permita al usuario realizar todas las operaciones solicitadas (agregar, buscar, listar productos y calcular valor total). | 20%    |

---

# Tecnología

- Python