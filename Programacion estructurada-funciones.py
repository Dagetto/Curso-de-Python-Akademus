
'''concepto 
la programacion estructurada busca dividir o descomponer un problema complejo en pequeños problemas. La solucion de cada uno de esos pequeños problemas nos trae la solucion del problema complejo.
en python el planteo de esas pequeñas soluciones al problema complejo se hace dividiendo el programa en funciones.
Una funcion, es la forma de agrupar expresiones y sentencias (algoritmos) que realicen determinadas acciones, pero que estas, solo se ejecuten cuando son llamadas. Es decir, que al colocar un algoritmo dentro de una funcion, al correr el archivo, el algoritmo no sera ejecutado si no se ha hecho una referencia a la funcion que lo contiene.'''

'''definiendo funciones
En python, la definicion de funciones se realiza mediante la instruccion DEF mas un nombre de funcion descriptivo-para el cual, aplican las mismas reglas que para el nombre de las variables- seguido de parentesis de apertura y cierre. Como toda estructura de control en python, la definicion de la funcion finaliza con dos puntos (:)y el algoritmo que la compone, ira identado con 4 espacios:
def mi_funcion():
#aqui el algoritmo
Una funcion, no es ejecutada hasta tanto no sea invocada.Para invocar una funcion, simplemente se la llama por el nombre
def mi_funcion (): 
    print 'hola mundo'
mi_funcion()'''


def presentacion ():
	print('programa para hacer operaciones aritmeticas de suma y resta de dos valores')
	print ('********************')

def introducirdatos():
	global valor1
	global valor2 
	valor1= int(input('ingrese el primer valor'))
	valor2=int(input('ingrese el segundo valor'))

def suma():
	suma=valor1+valor2
	print('la suma de los dos valores es:', suma)

def resta():
	resta=valor1-valor2
	print('la resta de los valores es:',resta)

def finalizacion ():
	print('******************')
	print ('gracias por utilizar este programa')
#programa principal
presentacion()
introducirdatos()
suma()
resta ()
finalizacion()