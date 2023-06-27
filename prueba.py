import csv
import numpy


entrada = 2500
nombre = input('ingrese su nombre ')
lista_peliculas = ['spiderman']
lista_asientos = [1,2,3,4,5]
asientos = []

while True: 
    print('[1] ver peliculas en carteleras')
    print('[2] ver butacas diponibles ')
    print('[3] mostrar asientos para peliculas ')
    print('[4] elegir peliculas')
    print('[5]descuento de peliculas')
    print('[6] valor entrada')
    print('[7] asientos')
    print('[8] buscar asientos ocupados')
    

    opc = input('ingrese opcion ')

    if opc == '1':
        print(lista_peliculas)
    elif opc == '5':
        print('tiene derecho a un 10%, si es alumno duoc')
    elif opc == '6':
        print('el valor de la entrada general es de $2500 ') 
    elif opc == '7':
        print(lista_asientos)    
    elif opc == '8':
        print('asineto ocupados',asientos)
        print('asiento disponibles',lista_asientos)
        
    elif opc == '4':
        selcion_pelicula = input('selecione pelicula ')
        print('sr/a',nombre,'usted elijio ',selcion_pelicula)

        print('ahora debe elegir asientos')
        print(lista_asientos)
        asientos.append(input('ingrese asiento '))
        print('asiento seleccionado ',asientos)
        break

    alumno_duoc =  input('eres alumno duoc? (si/no)')
    if alumno_duoc == 'si':
            print('valor a pagar ',entrada - 250)
            print('****boleta*********')
            print('****nombre= ',nombre,'*********')
            print('***su asiento es ',asientos,'******') 
            print('***debe pagar ', entrada -250,'*********')

                
    elif alumno_duoc == 'no':
            print('valor de la entrada') 
            print('****boleta*********')
            print('****nombre= ',nombre,'*********')
            print('***su asiento es ',asientos,'******') 
            print('***debe pagar ', entrada -250,'*********')    
         

    
               







