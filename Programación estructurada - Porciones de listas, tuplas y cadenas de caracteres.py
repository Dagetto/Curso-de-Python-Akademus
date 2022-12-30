def meses_faltantes(numero):
	meses=('enero','febrero', 'marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
	return meses [numero:]


	#bloque principal
	#se recupera desde el mes indecado hasta el final de la lista

print ('imprimir los nombres de los meses que faltan hasta fin de año')
numero=int(input('ingrese numero del mes:'))
mesesfalta=meses_faltantes(numero)
print (mesesfalta)

