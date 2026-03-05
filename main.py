import random
# Tu implementacion va aqui
def tirar_dados(jugador):
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    print(f"La tirada del {jugador} es: {tirada}")

    for n in range(2):
        respuesta=input("¿Quieres volver a tirar algún dado? (s/n): ")
        while respuesta.lower() not in ["s","n"]:
            respuesta=input("Respuesta no válida. ¿Quieres volver a tirar algún dado? (s/n): ")
        if respuesta.lower()=="s":    
            for i in range(len(tirada)):
                res=input(f"¿Quieres volver a tirar el dado en la posicion {i}? (s/n): ")
                if res.lower()=="s":
                    tirada[i] = random.randint(1,6)
            print(f"La tirada del {jugador} es: {tirada}")
        elif respuesta.lower()=="n":
            break
    print(f"La tirada final del {jugador} es: {tirada}")
    return tirada,n

def evaluar_tirada(tirada,jugador):
    tirada.sort()
    generala=False
    poker=False
    full=False
    escalera=False
    if tirada[0]==tirada[4]:
        print(f"{jugador} ha sacado un Generala!")
        generala=True
    if tirada[0]==tirada[3] or tirada[1]==tirada[4]:
        print(f"{jugador} ha sacado un Poker!")
        poker=True
    if (tirada[0]==tirada[2] and tirada[3]==tirada[4]) or (tirada[0]==tirada[1] and tirada[2]==tirada[4]):
        print(f"{jugador} ha sacado un Full!")
        full=True
    if tirada==[1,2,3,4,5] or tirada==[2,3,4,5,6]:
        print(f"{jugador} ha sacado una Escalera!")
        escalera=True
    else:
        print(f"{jugador} no ha sacado ninguna combinación especial.")
    return generala, poker, full, escalera

def sumarpuntos(tirada):
    puntos=0
    num=input("¿Qué número quieres sumar? (1-6): ")
    while num not in ["1","2","3","4","5","6"]:
        num=input("Número no válido. ¿Qué número quieres sumar? (1-6): ")
    num=int(num)
    for dado in tirada:
        if dado==num:
            puntos+=num
    print(f"Has sumado {puntos} puntos por el número {num}.")
    return puntos

def decision(tirada,jugador,tabla):
    dec=input("¿Quieres evaluar tu tirada o sumar puntos? (evaluar/sumar): ")
    while dec.lower() not in ["evaluar","sumar"]:
        dec=input("Decisión no válida. ¿Quieres evaluar tu tirada o sumar puntos? (evaluar/sumar): ")
    if dec.lower()=="sumar":
        if all(tabla[i][1]!=0 and tabla[i][1]!=-1 for i in range(4,10)):
            print("Ya has sumado puntos por todos los números. No puedes sumar más puntos.")
            elegir=input("Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
            while elegir not in ["1","2","3","4","5","6","7","8","9","10"]:
                elegir=input("Opción no válida. Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
            elegir=int(elegir)
            while tabla[elegir-1][1]!=0:
                print("Ya has sumado puntos por esa opción. Elige otra.")
                elegir=input("Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
                while elegir not in ["1","2","3","4","5","6","7","8","9","10"]:
                    elegir=input("Opción no válida. Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
                elegir=int(elegir)
            tabla[elegir-1][1]=-1
            return tabla
        else:
            num=input("¿Qué número quieres sumar? (1-6): ")
            while num not in ["1","2","3","4","5","6"]:
                num=input("Número no válido. ¿Qué número quieres sumar? (1-6): ")
            num=int(num)
            while tabla[num+3][1]!=0:
                print("Ya has sumado puntos por ese número. Elige otro.")
                num=input("¿Qué número quieres sumar? (1-6): ")
                while num not in ["1","2","3","4","5","6"]:
                    num=input("Número no válido. ¿Qué número quieres sumar? (1-6): ")
                num=int(num)
            puntos=sumarpuntos(tirada)
            if all(tabla[i][1]!=0 for i in range(4,10)):
                print("Ya has sumado puntos por todos los números. No puedes sumar más puntos.")
                puntos=0
            tabla[num+3][1]=puntos
    elif dec.lower()=="evaluar":
        generala, poker, full, escalera = evaluar_tirada(tirada,jugador)
        ntiro=tirada(jugador)[1]
        if all(tabla[i][1]!=0 for i in range(0,4)):
            print("Ya has evaluado todas las combinaciones especiales. No puedes evaluar más combinaciones.")
            elegir=input("Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
            while elegir not in ["1","2","3","4","5","6","7","8","9","10"]:
                elegir=input("Opción no válida. Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
            elegir=int(elegir)
            while tabla[elegir-1][1]!=0:
                print("Ya has sumado puntos por esa opción. Elige otra.")
                elegir=input("Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
                while elegir not in ["1","2","3","4","5","6","7","8","9","10"]:
                    elegir=input("Opción no válida. Elige que descartar (1-Generala/2-Poker/3-Full/4-Escalera/5-Uno/6-Dos/7-Tres/8-Cuatro/9-Cinco/10-Seis): ")
                elegir=int(elegir)
            tabla[elegir-1][1]=-1
            return tabla
        else:
            dsc=input("¿Qué combinación quieres evaluar? (Escribir el número) (1-Generala/2-Poker/3-Full/4-Escalera): ")
            while dsc.lower() not in ["1","2","3","4"]:
                dsc=input("Combinación no válida. ¿Qué combinación quieres evaluar? (Escribir el número) (1-Generala/2-Poker/3-Full/4-Escalera): ")
            dsc=int(dsc)
            while tabla[dsc-1][1]!=0:
                print("Ya has evaluado esa combinación. Elige otra.")
                dsc=input("¿Qué combinación quieres evaluar? (Escribir el número) (1-Generala/2-Poker/3-Full/4-Escalera): ")
                while dsc.lower() not in ["1","2","3","4"]:
                    dsc=input("Combinación no válida. ¿Qué combinación quieres evaluar? (Escribir el número) (1-Generala/2-Poker/3-Full/4-Escalera): ")
                dsc=int(dsc)
            if ntiro==0:
                if dsc==1:
                    if generala == False:
                        print("No has sacado Generala. No sumas puntos.")
                        tabla[0][1]=0
                    else:
                        print("Has sacado Generala Real. Sumás 80 puntos.")
                        tabla[0][1]=80
                elif dsc==2:
                    if poker == False:
                        print("No has sacado Poker. No sumas puntos.")
                        tabla[1][1]=0
                    else:
                        print("Has sacado Poker a la primera. Sumás 45 puntos.")
                        tabla[1][1]=45
                elif dsc==3:
                    if full == False:
                        print("No has sacado Full. No sumas puntos.")
                        tabla[2][1]=0
                    else:
                        print("Has sacado Full a la primera. Sumás 35 puntos.")
                        tabla[2][1]=30
                elif dsc==4:
                    if escalera == False:
                        print("No has sacado Escalera. No sumas puntos.")
                        tabla[3][1]=0
                    else:
                        print("Has sacado Escalera a la primera. Sumás 25 puntos.")
                        tabla[3][1]=20
            else:
                if dsc==1:
                    if generala == False:
                        print("No has sacado Generala. No sumas puntos.")
                        tabla[0][1]=0
                    else:
                        print("Has sacado Generala. Sumás 50 puntos.")
                        tabla[0][1]=50
                elif dsc==2:
                    if poker == False:
                        print("No has sacado Poker. No sumas puntos.")
                        tabla[1][1]=0
                    else:
                        print("Has sacado Poker. Sumás 40 puntos.")
                        tabla[1][1]=40
                elif dsc==3:
                    if full == False:
                        print("No has sacado Full. No sumas puntos.")
                        tabla[2][1]=0
                    else:
                        print("Has sacado Full. Sumás 30 puntos.")
                        tabla[2][1]=30
                elif dsc==4:
                    if escalera == False:
                        print("No has sacado Escalera. No sumas puntos.")
                        tabla[3][1]=0
                    else:
                        print("Has sacado Escalera. Sumás 20 puntos.")
                        tabla[3][1]=20
    return tabla

def main():
    tabla1=[["Generala",0],["Poker",0],["Full",0],["Escalera",0],["Puntos 1",0],["Puntos 2",0],["Puntos 3",0],["Puntos 4",0],["Puntos 5",0],["Puntos 6",0]]
    tabla2=[["Generala",0],["Poker",0],["Full",0],["Escalera",0],["Puntos 1",0],["Puntos 2",0],["Puntos 3",0],["Puntos 4",0],["Puntos 5",0],["Puntos 6",0]]
    tirada1 = tirar_dados("Jugador1")[0]
    tabla1=decision(tirada1,"Jugador1",tabla1)
    print("Tabla del Jugador 1:")
    for fila in tabla1:
        print(fila)
    tirada2 = tirar_dados("Jugador2")[0]
    tabla2=decision(tirada2,"Jugador2",tabla2)
    print("Tabla del Jugador 2:")
    for fila in tabla2:
        print(fila)
    


main()
