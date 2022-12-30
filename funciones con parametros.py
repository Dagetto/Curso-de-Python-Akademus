'''FUNCIONES CON PARAMETROS
Un parametro es un valor que la funcion espera recibir cuando sea llamada(invocada), con el fin de ejecutar acciones en base a este.
Una funcion puede esperar uno o mas parametros (separados por comas)o ninguno.
Def funcion (nombre,apellido):
#codigo a ejecutar de la funcion
los parametros se indican entre los parentesis en forma de variable. Los valores de estos parametros seran utilizados dentro de la funcion como una variable local.
def funcion (nombre,apellido):
	datoscompletos+nombre,apellido
	print datoscompletos
si queremos acceder a los parametros desde afuera de la funcion nos dara un error.
los argumentos siempre hay que pasarlos en el mismo orden en el que se espera.

PARAMETROS POR OMISION
podemos asignar valores por defecto a los parametros de las funciones:
def funcion(nombre,apellido='blanco')
print nombre,apellido

tambien es posible llamar a la funcion, pasadole los argumentos esperados como pares
clave=valor.
def funcion (nombre,apellido='blanco')
print nombre,apellido
funcion(apellido='gomez',nombre='carlos')

PARAMETROS ARBITRARIOS
es posible que una funcion espere recibir un numero desconocido de argumentos, estos argumentos llegan a la funcion en forma de tupla. 
para separarlo se utiliza *
def funcion (parametrofijo,*arbitrarios) #los parametros arbitrarios se recorren como tupla.
for parametros in arbitrarios:
	print parametros
	funcion ('fijo','arbitrarios1','arbitrarios2','arbitrarios1')
Los parametros arbitrarios deben suceder a los fijos. Es posible obtener parametros como pares de clave=valor, el nombre del parametro
deben preceder los signos**

#EJEMPLOS 1 CON PARAMETROS SIMPLES'''

def mostrar_mensaje(mensaje):
	#funcion con parametros simples
	print ('********************')
	print (mensaje)
	print('*********************')

def cargar_suma():
	valor1=int(input('ingresa el primer valor:'))
	valor2=int (input('ingresa el segundo valor:'))
	suma=valor1+valor2
	print('la suma es:',suma)
mostrar_mensaje('calculo de la suma de los dos valores')
cargar_suma()
