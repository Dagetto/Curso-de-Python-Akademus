#Parametros tipo lista
def sumarizar (lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma 
def mayor (lista):
	may=lista[0]
	for x in range (1,len(lista)):
	    if lista [x]>may:
		    may=lista[x]
	return may 
def menor (lista):
	men=lista[0]
	for x in range(1,len(lista)):
	    if lista[x]<men:
		    men=lista[x]
	return men 
listavalores=[10,56,23,34,190,298]
print ('lista completa')
print(listavalores)
print('suma de los elemetos',sumarizar(listavalores))
print('el numero mayor:', mayor(listavalores))
print('el numero menor:',menor(listavalores))
