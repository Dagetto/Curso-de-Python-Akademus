''' los dos tipos de estructuras de datos fundamentales son las listas y las tuplas.
La lista es una estructura mutable(es decir podemos modificar sus elementos,agregar y borras) en cambio una tupla es una secuencia
de datos inmutable, es decir una vez definida no puede cambiar.
En Python vimos que podemos definir elementos de una lusta que sean de tipo lista, en ese caso decimos que tenemos una lista anidada.
Se pueden generar tuplas anidadas.
En general podemos crear y combinar tuplas con elementos de tipo lista y viceversa, es decir lista con componentes tipo tupla.
Sintaxis:
Lista_tupla=['juan',53,(25,11,1999)]'''

def cargar_paisespoblacion():
	paises=[] #lista
	for x in range(5):
		nom=input('ingrear el nombe del pais:')
		cant=int(input('ingrese la cantidad de habitantes:'))
		paises.append((nom,cant)) #elementos de la lista añadidos a la lsta
	return paises

def imprimir(paises):
	print('paises y su poblacion')
	for x in range(len(paises)):
		print(paises[x][0],paises[x][1])

def pais_maspoblacion(paises):
	pos=0
	for x in range(1,len(paises)):
		if paises [x][1]>paises [pos] [1]:
		    pos=x
	print('pais con mayor cantidad de habitantes:', paises[pos][0])


paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)
