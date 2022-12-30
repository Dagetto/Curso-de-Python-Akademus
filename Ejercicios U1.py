### EJERCICIO 1 ###

lista_frutas=['limon', 
              'manzana', 
              'naranja', 
              'pera',
              'kiwi', 
              'mango', 
              'banana'
             ] 
print (lista_frutas[3])

### EJERCICIO 2 ###

lista_frutas_2=['limones', 
                'manzanas'
               ] 
print (('SU CARRO DE COMPRAS CONTIENE LAS SIGUIENTES FRUTAS:')+ str(lista_frutas_2))

### EJERCICIO 3 ###

nombre = input('Escriba su nombre')

print (('Hola') + (' ') + nombre +  (',bienvenido'))

### EJERCICIO 4 ###

Primer_valor = input  ('ingrese el primer valor')
Segundo_valor = input  ('ingrese el segundo valor')

Primer_valor = int (Primer_valor)
Segundo_valor = int (Segundo_valor)
Suma_de_valores = Primer_valor + Segundo_valor

Lista_valores = [Primer_valor,
                 Segundo_valor,
                 Suma_de_valores
                ]
print (Lista_valores)

print (('primer valor ingresado:') + 
       (' ') + 
       str (Primer_valor) + 
       (' ') +
       ('segundo valor ingresado') + 
       (' ') + 
       str (Segundo_valor) + 
       (' ') +
       ('la suma de los valores es:') + 
       (' ') + 
       str (Suma_de_valores)
       )