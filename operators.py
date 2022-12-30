#OPERADORES ARITMETICOS
print( 3+4)
print( 3-4)
print( 3*4)
print( 3/4)

print(10//3) #division con resultados en numeros enteros
print(2**3) #exponente al cubo
print('prueba suma operadores' + str (3))

print ('hola' *10) #se puede multiplicar una STR con numeros enteros, no con FLOAT
my_float=2.5*2
print ('hola'* int(my_float)) #si se puede realizar si se convierte el float en entero

print (len('hola'))

#OPERADORES COMPARATIVOS

print (3>4)
print (3<4)
print (3==4)
print (3>=4)
print (3<=4)
print (3>4==2)

print('ingresa tu edad')
edad=int(input())
if edad >= 18:
	print ('sos mayor de edad')
else:
	print('sos menor de edad')

#Los operadores comparativos en el caso de texto compara el orden alfabetico,no cuenta caracteres
#firacode comandos pc
print ('aaaa'<='aaaa')
print ('aaaa'<='bbbb')
print ('aaaa'=='bbbb')
print ('aaaa'>'bbbb')

#OPERADORES LOGICOS

print (3>4 and "hola">"python") 
print (3>4 or "hola"<"python") 
print ('zaby'<'zac')#COMPARACION DE TEXTO
print (not(3>4)) 
print(3>4 or 'hola'>'python' and 4==4)

'''print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False'''