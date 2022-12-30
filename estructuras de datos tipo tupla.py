'''CARACTERISTICAS
Permite almacenar una coleccion de datos que no son necesariamente del mismo tipo.
Los datos de la tupla son nmutables a diferencia de las listas que son mutables.
Una vez iniciada la tupla no podemos agregar, borrar o modificar sus elementos.
sintaxis:
nombretupla=(valor1,valor2,valor3,...)'''

def cargar_fecha():
	dd=int(input('ingrese numero de dia:'))
	mm=int(input('ingrese numero del mes:'))
	aa=int(input('ingrese numero del año:'))
	tupla=(dd,mm,aa)
	return tupla
def imprimir_fecha(fecha):
	print(fecha[0],fecha[1],fecha[2],sep='/')

#Bloque principal

fecha=cargar_fecha()
imprimir_fecha(fecha)
