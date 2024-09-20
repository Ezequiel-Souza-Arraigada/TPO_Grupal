
def cuadrilla():
    lado = 100
    print("-" * lado)#Borde superior
    lista = ["Matematica", "Lengua", "Informatica", "Teatro", "Geografia", "Fisica", "Ciencias Naturales"] #Lista de materias y opcion de salir
    print( "1 - Matematica  | 2 - Lengua   |  3 - Informatica   | 4 - Teatro  ")
    print()
    print( "5 - Geografia   | 6 - Fisica   |  7 - Ciencias Naturales   | salir (-1)  ") #Listas de materias ya mostradas en pantalla
    lado = 100
    print("-" * lado)#Borde inferior
    print()
    materia = int(input("Ingrese el numero de materia: ")) 

    print()  
    normal = 0
    while normal == 0: 
        if materia == 1:
            return lista[0]
        elif materia == 2:
            return lista[1]
        elif materia == 3:
            return lista[2]
        elif materia == 4:
            return lista[3]
        elif materia == 5:
            return lista[4]
        elif materia == 6:
            return lista[5]
        elif materia == 7:
            return lista [6]
        elif materia == -1:
            normal = normal + 1
            return "Gracias por usar nuestro programa" ####Arreglar####
        else:
            return "Error al ingresar la materia"

resultado_cuadrilla = cuadrilla()

print(resultado_cuadrilla)
    







