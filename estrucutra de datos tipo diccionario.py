'''La estructura de datos tipo diccionario utiliza una clave para acceder el valor. El subindice puede ser un entero, un float, un string, una tupla,etc.
(en general cualquier tipo de dato inmutable)
1. Para definir un diccionario, se encierra el listado de valores entre llaves. las parejas de clavo y valor se separan con comas,
y la clave y el valor se separan con dos puntos.

diccionario={'nombre': 'carlos','edad',: 22, 'cursos': ['python','django','javascript']}

2.Podemos acceder al elemento de un Diccionario mediante la clave de este elemento.

print diccionario['nombre'] #carlos
print diccionario ['edad'] #22
print diccionario['cursos'] #['python','django','javascript']

3.tambien es posible insertar una lista dentro de un diccionario. Para acceder a cada uno de los cusos usamos los indices:

print diccionario['cursos'][0]#python
print diccionario ['cursos'][1]#django
print diccionario ['cursos'][2]#javascript

4. Para recorrer todo el diccionario, podemos hacer uso de la estructura for:
for key in diccionario:
print key, ';', diccionario [key]'''

def cargar():
	diccionario={}
	continua='s'
	while continua == 's':
		caste=input('ingrese palabra en castellano:')
		ing=input ('ingrese palabra en ingles:')
		diccionario [caste]=ing
		continua=input('quiere cargar otra palabra: [s/n')
	return diccionario

def imprimir (diccionario):
	print ('listado completo del diccionario')
	for ingles in diccionario:
		print (ingles,diccionario[ingles])

def consulta_palabra (diccionario):
	pal=input ('ingrese la palabra en castellano a consultar')
	if pal in diccionario:
		print ('en ingles significa:', diccionario [pal])

#bloque principal

diccionario=cargar()
imprimir (diccionario)
consulta_palabra (diccionario)