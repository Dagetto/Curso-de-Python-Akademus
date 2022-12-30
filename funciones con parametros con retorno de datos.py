'''EJEMPLO 2 RETORNO DE DATOS
retorno de datos, se devuelven a la llamada de la funcion que recoge los datos'''

def retorno_superficie (lado):
	sup=lado*lado
	return sup #con la isntruccion return se retorna los datos de la funcion
va=int(input('introduce el valor del cuadrado:'))
superficie=retorno_superficie(va) # recogemos los datos que enviamos lo almacenamos en la variable superficie
print('el algoritmo del cuadrado es:', superficie)
