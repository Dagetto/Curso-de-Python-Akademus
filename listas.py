###Listas###
#conjunto de elementos ordenandos que comienza desde el numero 0. indice 0, indice 1, indice 2, etc. 
#Se pueden combinar datos, str, int, float, etc.
my_list= list()
my_other_list=[]

print(len(my_list))

my_list=[35,24,62,52,30,30,17]

print (my_list)
print(len(my_list))

my_other_list=[35,1.77,  'Lucas', 'Monzon']

print (type(my_other_list))

print(my_other_list[0])
print(my_other_list[-2])
print(my_other_list[1])
#print(my_other_list[4]) index error porque no existe el elemento 4, la lista esta compuesta por el rango 0/3
print(my_list.count(30)) #cuenta cuantas veces se encuentra el elemento '30' en my_list
print(my_other_list.count('Lucas'))

age,height, name, surname =my_other_list #necesita especificar todos los elementos de la lista
print (surname)

print (my_list+my_other_list) #se pueden sumar listas, concatenando listas.


my_other_list.append('faimali') #agrega elementos a la lista luego del ultimo elemento
print(my_other_list)

my_other_list.insert(1,'verde')#insertamos valores nuvos en la posicion indicada de la lista
print (my_other_list)

my_other_list.insert(1, 'azul')
print (my_other_list)

my_other_list.remove('verde') #elimina elementos especificos de la lista.
print (my_other_list)

print (my_list.pop ()) #elimina el ultimo elemento
print(my_list)

my_pop_element=my_list.pop(2)#elimina el elemento pero lo guarda para continuar trabajando con los otros elementos.
print (my_pop_element)

del my_list[2] #elimina por indice
print (my_list)

my_new_list = my_list.copy()
print (my_new_list)

my_list.clear()
print(my_list)

my_new_list.reverse()
print (my_new_list)

my_new_list.sort() #ordena elementos, en este caso que son datos int los ordena de menor a mayor.
print (my_new_list)

print(my_new_list[1:3]) #selecciona imprimir un rango.

my_list='hola python' #LA LISTA SE CONVIERTE EN STR, esto nos indica que es un lenguaje de 'tipeado debil' o 'dinamico''. si agregamos [] se definiria nuevamente como lista
print (my_list)
print (type(my_list))

