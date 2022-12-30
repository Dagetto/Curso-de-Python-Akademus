def meses_faltantes(inicio,final):
	meses=('enero','febrero', 'marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
	return meses [inicio:final]


#bloque principal
#se recupera desde el mes indicado hasta el otro mes indicado

print('imprimir los nombres de meses comprendidos entre un mes y otro:')
inicio=int(input('ingrese el numero del mes:'))
final=int(input('ingrese el numero del mes:'))
mesesfalta=meses_faltantes(inicio,final)
print (mesesfalta)