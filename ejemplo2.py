global examenesPresentados, examenesGanados, examenesPerdidos, sumaPuntaje
examenesPresentados = 0
examenesGanados = 0
examenesPerdidos = 0
sumaPuntaje = 0

def almaceneUsuario():
    global examenesPresentados, examenesGanados, examenesPerdidos, sumaPuntaje
    examenesPresentados += 1
    puntaje = int(input("digite el puntaje del examen: "))
    sumaPuntaje += puntaje
    if (puntaje > 70):
        examenesGanados += 1
    else:
        examenesPerdidos += 1

def muestreResultados():
    print("Cantidad de Examenes Presentados: ", examenesPresentados)    
    print("Cantidad de Examenes Ganados: ", examenesGanados)
    print("Cantidad de Examenes Perdidos: ", examenesPerdidos)
    print("Puntaje promedio: ", float(sumaPuntaje/examenesPresentados))

menu = int(input("digite opción 1.NuevoUsuario 2.Resultados 3.Salir: "))
while(menu != 3):
    if (menu == 1): almaceneUsuario()
    elif (menu == 2): muestreResultados()
    menu = int(input("digite opción 1.NuevoUsuario 2.Resultados 3.Salir: "))
