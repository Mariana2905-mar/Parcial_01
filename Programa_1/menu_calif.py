Calificaciones = []
activo = True
#mientras la variable activo sea true ,sigue repitiendo bloque de abajo
while activo:
    print("===CONTROL DE CALIFICACIONES===")
    print("1.Registrar Calificación")
    print("2.Mostrar calificaciones")
    print("3.Mostrar promedio")
    print("4.salir")
    Opcion = input("Elige una opcíon:")#input sirve para que el usuario lea indicacion y escriba resultado
    if Opcion == "1":
        #try le dice al programa que si inggresan un dato que no corresponde no se rompa el programa
        try:
            nota = float(input("ingresa la calificacion:"))
            if 0 <= nota <= 10:
                Calificaciones.append(nota)
                print("calificacion registrada correctamente.")
            #else debe de estar al mismo nivel que if
            else:
                print("la calificacion debe de estar entre 0 y 10.")
        #try y except van al mismo nivel ,except atrapa el error si hay ,en este caso si usuario no ingresa numeros
        except ValueError:
            print("Entrada invalida,debes ingresar un numero.")
    #hasta aqui termina opcion 1
    #continua opcion 2
    #elif dice si el usuario no elige opcion 1 ,PERO SI OPCION 2,entonces haz esto
    elif Opcion == "2":
        if Calificaciones == []:#esto dice si la lista de calificaciones esta vacia
            print("No hay calificaciones registradas.")
        else:
            #para cada elemento dentro de lista de calif.. tomando uno a la vez y llamandolo nota haz lo siguiente
            for nota in Calificaciones:
                print(nota)
    #continuamos con la opcion 3
    elif Opcion == "3":
        if Calificaciones ==[]:
            print("No hay calificaciones registradas.")
        else:
            promedio = sum(Calificaciones)/ len (Calificaciones)
            #promedio es variable y la operacion que se hace es sumar calificaciones y dividir entre numero de calificaciones
            print("El promedio es:",promedio)
    #print puede recibir varias cosas como texto y variables separadas por una ","
    #continuamos con opcion 4
    elif Opcion == "4":
        activo = False
        print("saliendo del programa...")
    #parte donde si la persona escribe otra cosa que no sea opcion 1,2,3 o 4
    else:
        print ("opcion invalida. Intente de nuevo")