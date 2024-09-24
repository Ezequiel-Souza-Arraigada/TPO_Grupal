def cuadrilla():
    lado = 100
    print("-" * lado)#Borde superior
    lista = ["Fundamentos de Informatica", "Algebra ", "Teoria de Sistemas", "Fundamentos de Quimica", "Arquitectura de Computadoras", "Sistemas Operativos", "Programacion I"] #Lista de materias y opcion de salir
    print( "1 - Fundamentos de Informatica  | 2 - Algebra   |  3 - Teoria de Sistemas   | 4 - Fundamentos de Quimica  ")
    print()
    print( "5 - Arquitectura de Computadoras   | 6 - Sistemas Operativos   |  7 - Programacion I   | salir (-1)  ") #Listas de materias ya mostradas en pantalla
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
            return "Gracias por usar nuestro programa" 
        else:
            return "Error al ingresar la materia"

resultado_cuadrilla = cuadrilla()

print(resultado_cuadrilla)
print()