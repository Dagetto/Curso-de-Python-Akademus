'''Uno de los elementos mas importantes que podemos encontrar en las estructuras de datos de Python es que podemos definir elementos que sean tambien estructuras de datos. En general se dice que podemos anida una estructura de datos dentro de otra estructura de datos.
En los ejemplos anteriores se dejo ver que podemos definir elementos de una lista que sean tambien de tipo lista o de tipo tupla.
Tambien hemos mencionado que un diccionario consta de claves y valores para esas claves. A continuacion desarrollaremos un problema donde los valores para esas claves sean tuplas y/o lista.

Ej. aplicado a un problema:
Confeccionar un programa que permita cargar un codigo de producto como clave en un diccionario. Guardar para dicha clave el nombe del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1. Carga de datos en el diccionario.
2.Listado completo de productos.
Consulta de un producto por su clave, mostrar el nombre, precio y stock.
3. Consulta de un producto por su clave, mostrar el nombre, el precio y stock.
4. Listado de todos los productos que tengan un stock con valor 0'''

def cargar():
	productos={} #diccionario
	continua='s'
	while continua=='s':
		codigo=int(input('ingrese el codigo del producto:'))
		descripcion=input('ingrese la descripcion:')
		precio=float(input('ingrese el precio:'))
		stock=int(input('ingrese el stock actual:'))
		productos [codigo]=(descripcion, precio, stock)
		continua=input('desea cargar otro producto [s/n]?')
	return productos


def imprimir(productos):
	print('listado completo de productos:')
	for codigo in productos:
		print(codigo, productos [codigo][0], productos [codigo][1], productos [codigo][2])


def consulta (productos):
	codigo=int(input('ingrese el codigo del articulo a consultar:'))
	if codigo in productos:
		print (productos[codigo][0],productos[codigo][1],productos [codigo][2])


def listado_stock_cero (productos):
	print ('listado de articulos con stock en cero:')
	for codigo in productos:
		if productos [codigo][2]==0:
			print (codigo, productos [codigo][0], productos[codigo][1], productos[codigo][2])

#bloque principal 

productos=cargar()
imprimir(productos)
consulta (productos)
listado_stock_cero (productos)