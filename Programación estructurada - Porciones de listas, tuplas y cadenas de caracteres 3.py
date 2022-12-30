def meses_faltantes(numero):
	meses=('enero','febrero', 'marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
	return meses [:inicio]


	#bloque principal
	#se recuperan todos los meses anteriores al mes indicado

print ('imprimir los nombres de los meses anteriores')
inicio=int(input('ingrese numero del mes:'))
mesesfalta=meses_faltantes(inicio)
print (mesesfalta)