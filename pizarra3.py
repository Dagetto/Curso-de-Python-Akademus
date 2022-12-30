#STRINGS
my_string= 'mi string'
my_other_string= 'mi otro string'

print(len(my_string))
print (len(my_other_string))

print(my_string+'   '+my_other_string)

my_other_newstring='mi nueva cuerda\ncon salto de espacio'#salto de linea 
print (my_other_newstring)

my_tab_string='\testa es una string con tabulacion' #tabulado
print(my_tab_string)

my_escape_string='\t esta es una string con  combinacion de  tabulado y \n salto' #combinacion tabulado y salto
print(my_escape_string)

my_escape_string2='\\t esta es una string que anula el tabulado y el \\n salto' #forma de anular la funcion del tabulado repitiendo el simbolo
print(my_escape_string2)

#FORMATEO
name,surname, age = 'juan', 'perez', 27
print('mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) #se realiza mediante comando .format 
print('mi nombre es %s %s y mi edad es %d' %(name,surname,age)) #se realiza de manera manual. Realizarlo de manera manual asegura que ingesamos texto (%s) o numeros (%d) de manera mas segura

print(f'mi nombre es {name} {surname} y mi edad es {age}'.format(name, surname, age)) #ESTA SERIA LA FORMA MAS CORRECTA DE UN FORMATEO SEGURO
'''FORMATEO DE MANERA MANUAL:
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision'''

#DESEMPAQUETADO DE CARACTERES

lenguaje='python'
a,b,c,d,e,f='python' #se le asigna una variable a cada letra
print (a)
print (b)

#DIVISION

lenguaje_slice= lenguaje [0:4]
print (lenguaje_slice)
lenguaje_slice= lenguaje [1:4]
print (lenguaje_slice)
lenguaje_slice= lenguaje [0:1]
print (lenguaje_slice)
lenguaje_slice= lenguaje [-2]
print (lenguaje_slice)

lenguaje_slice= lenguaje [0:6:2] #PERMITE ESTABLECER RANGOS Y EVITAR CARACTERES (REVISAR)
print (lenguaje_slice)

#REVERSE

reversed_lenguaje=lenguaje [::-1] #EMPIEZA DESDE 1, NO 0
print (reversed_lenguaje)

#FUNCIONES

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count('t'))
print(lenguaje.isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())# SE COMPRUEBA SI EL TEXTO ESTA EFECTIVAMENTE EN LA CONDICION .UPPER

