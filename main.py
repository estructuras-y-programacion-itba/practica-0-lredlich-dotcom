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
    return tirada


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
        tabla[num+3][1]=puntos
    elif dec.lower()=="evaluar":
        evaluar_tirada(tirada,jugador)
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
        tabla[dsc-1][1]=evaluar_tirada(tirada,jugador)[dsc-1]   
def main():
    tabla1=[["Generala",0],["Poker",0],["Full",0],["Escalera",0],["Puntos 1",0],["Puntos 2",0],["Puntos 3",0],["Puntos 4",0],["Puntos 5",0],["Puntos 6",0]]
    tabla2=[["Generala",0],["Poker",0],["Full",0],["Escalera",0],["Puntos 1",0],["Puntos 2",0],["Puntos 3",0],["Puntos 4",0],["Puntos 5",0],["Puntos 6",0]]
    tirar_dados("Jugador1")

main()
