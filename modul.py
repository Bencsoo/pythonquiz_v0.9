import os
import random
import time
import sys


class Tesztkerdes:
    def __init__(self , feladvany:str , a:str , b:str , c:str , megoldas:str , s:str):
        self.feladvany = feladvany
        self.a = a
        self.b = b
        self.c = c
        self.megoldas = megoldas
        self.s = s



def get_teszt() -> list[Tesztkerdes]:
    tesztsor:list[Tesztkerdes] = []
    kerdesek_file = open('teszt.txt' , encoding='utf-8-sig')
    megoldasok_file = open('megoldas.txt', encoding='utf-8-sig')
    segitseg_file = open("segitseg.txt" , encoding='utf-8')
    
    for x in range(10):
        k:str = kerdesek_file.readline().strip()
        a:str = kerdesek_file.readline().strip()
        b:str = kerdesek_file.readline().strip()
        c:str = kerdesek_file.readline().strip()
        m:str = megoldasok_file.readline().strip()
        s:str = segitseg_file.readline().strip()
        tesztsor.append(Tesztkerdes(k, a , b , c , m ,s))
    return tesztsor

def game_loop(tesztsor:list[Tesztkerdes] , jatekmod, pontszamok:list , idok:list) -> int:
    if jatekmod == "1":
        pontszam:int = 0
        felezessz:int = 1
        plido = time.time()
        for f in tesztsor:
            randomsz:int = random.randint(0, 1)
            rszam:int = random.randint(0, 1)
            print(f.feladvany)
            print(f"\t{f.a}")
            print(f"\t{f.b}")
            print(f"\t{f.c}")
            if felezessz == 1:
                felezes:str = input("\n\u001b[36m Felezes-t szeretnél kérni?(I/N)\u001b[0m")
                if felezes.lower() == "I".lower():
                    os.system('cls')
                    print(f.feladvany)
                    if rszam == 0:print(f"\t{f.s}")
                    if f.megoldas.lower() == "A".lower():
                        if randomsz == 0:
                            print(f"\t{f.b}")
                        if randomsz == 1:
                            print(f"\t{f.c}")
                    elif f.megoldas.lower() == "B".lower():
                        if randomsz == 0:
                            print(f"\t{f.a}")
                        if randomsz == 1:
                            print(f"\t{f.c}")
                    elif f.megoldas.lower() == "C".lower():
                        if randomsz == 0:
                            print(f"\t{f.b}")
                        if randomsz == 1:
                            print(f"\t{f.a}")
                    if rszam == 1:print(f"\t{f.s}")
                    felezessz -= 1
            if felezessz == 0 or felezes.lower() == "N".lower():
                valasz:str = input("\nHelyes választ betűjele:")
            if valasz.lower() == f.megoldas.lower():
                print("\033[1;32m HELYES! \t+1 pont\u001b[0m")
                pontszam += 1
            else:
                print(f"\u001b[1;31m HIBÁS válasz , a helyes betűjel a/az {f.megoldas}\u001b[0m")
            time.sleep(0.2)
            os.system('cls')
            print("\u001b[0m")
        vegido = time.time()
        idok.append(f"{int(vegido-plido)}")
        pontszamok.append(f"{pontszam}")
        pontszamok = []
        idok = []
        return pontszam
    if jatekmod == "2":
        felezessz:int = 1
        felezesszk:int = 1
        pontszame:int = 0
        pontszamk:int = 0
        peido = int(time.time())
        for pe in tesztsor:
            randomsz:int = random.randint(0, 1)
            rszam:int = random.randint(0, 1)
            print(pe.feladvany)
            print(f"\t{pe.a}")
            print(f"\t{pe.b}")
            print(f"\t{pe.c}")
            if felezessz == 1:
                felezes:str = input("\n\u001b[36m Felezes-t szeretnél kérni?(I/N)\u001b[0m")
                if felezes.lower() == "I".lower():
                    os.system('cls')
                    print(pe.feladvany)
                    if rszam == 0:print(f"\t{pe.s}")
                    if pe.megoldas.lower() == "A".lower():
                        if randomsz == 0:
                            print(f"\t{pe.b}")
                        if randomsz == 1:
                            print(f"\t{pe.c}")
                    elif pe.megoldas.lower() == "B".lower():
                        if randomsz == 0:
                            print(f"\t{pe.a}")
                        if randomsz == 1:
                            print(f"\t{pe.c}")
                    elif pe.megoldas.lower() == "C".lower():
                        if randomsz == 0:
                            print(f"\t{pe.b}")
                        if randomsz == 1:
                            print(f"\t{pe.a}")
                    if rszam == 1:print(f"\t{pe.s}")
                    felezessz -= 1
            if felezessz == 0 or felezes.lower() == "N".lower():
                valasz:str = input("\nHelyes választ betűjele:")
            if valasz.lower() == pe.megoldas.lower():
                print("\033[1;32m HELYES! \t+1 pont\u001b[0m")
                pontszame += 1
            else:
                print(f"\u001b[1;31m HIBÁS válasz , a helyes betűjel a/az {pe.megoldas}\u001b[0m")
            time.sleep(0.2)
            os.system('cls')
            print("\u001b[0m")
        vegidope = time.time()
        print("Player2 következik")
        time.sleep(0.8)
        os.system('cls')
        pkido = int(time.time())
        for pk in tesztsor:
            randomsz:int = random.randint(0, 1)
            rszam:int = random.randint(0, 1)
            print(pk.feladvany)
            print(f"\t{pk.a}")
            print(f"\t{pk.b}")
            print(f"\t{pk.c}")
            if felezesszk == 1:
                felezes:str = input("\n\u001b[36m Felezes-t szeretnél kérni?(I/N)\u001b[0m")
                if felezes.lower() == "I".lower():
                    os.system('cls')
                    print(pk.feladvany)
                    if rszam == 0:print(f"\t{pk.s}")
                    if pk.megoldas.lower() == "A".lower():
                        if randomsz == 0:
                            print(f"\t{pk.b}")
                        if randomsz == 1:
                            print(f"\t{pk.c}")
                    elif pk.megoldas.lower() == "B".lower():
                        if randomsz == 0:
                            print(f"\t{pk.a}")
                        if randomsz == 1:
                            print(f"\t{pk.c}")
                    elif pk.megoldas.lower() == "C".lower():
                        if randomsz == 0:
                            print(f"\t{pk.b}")
                        if randomsz == 1:
                            print(f"\t{pk.a}")
                    if rszam == 1:print(f"\t{pk.s}")
                    felezesszk -= 1
            if felezesszk == 0 or felezes.lower() == "N".lower():
                valasz:str = input("\nHelyes választ betűjele:")
            if valasz.lower() == pk.megoldas.lower():
                print("\033[1;32m HELYES! \t+1 pont\u001b[0m")
                pontszamk += 1
            else:
                print(f"\u001b[1;31m HIBÁS válasz , a helyes betűjel a/az {pk.megoldas}\u001b[0m")
            time.sleep(0.2)
            os.system('cls')
            print("\u001b[0m")
        vegidopk = time.time()
        idok.append(f"{int(vegidope-peido)} , {int(vegidopk-pkido)}")
        pontszamok.append(f"{pontszame} , {pontszamk}")
        idok = []
        pontszamok = []
    return pontszame , pontszamk , pkido , peido



def start(jatekmod):
    if jatekmod == "1".lower():
        nev1 = input("Név:\n")
        while nev1 == "":
            nev1 = input("név:\n")
        beiras = open('nev.txt' , 'a' , encoding='utf-8')
        beiras.write(f"{nev1}\t")
        beiras.close()
    if jatekmod == "2".lower():
        nev1 = input("P1 Név:\n")
        while nev1 == "":
            nev1 = input("P1 Név:\n")
        nev2 = input("P2 Név:\n")
        while nev2 == "":
            nev2 = input("P2 Név:\n")
        beiras = open('nev.txt' , 'a' , encoding='utf-8')
        beiras.write(f"{nev1} vs {nev2}\t")
        beiras.close()
    print("\n")
    print("---"*18)
    print(f"|Üdv az Elm utcában ,                   \n|ez a QUIZ , Freddy Krueger-ről fog szólni,           |")
    print("|Csak egy felezésed van , jol vigyázz vele!!!!        |")
    print("|\t           Felkészültél?                      |")
    print("|Ha igen , nyomd meg az ENTER-t hogy elinduljon a QUIZ|")
    input(f"{'---'*18}\t")
    time.sleep(1)
    os.system('cls')


def vege(tesztsor:list[Tesztkerdes]):
    menu=True
    while menu:
        print ("""\u001b[1;31m
        1.Játékos lista
        2.Kérdések megoldásokkal
        3.Kilépés/Quit\u001b[0m
        """)
        menu=input("Ird le a megfelelő számot! ") 
        if menu=="1": 
            jatekosok = open("nev.txt",'r', encoding='utf-8' )
            print('-'*50)
            print("Játékosok és elért pontszámaik:\n")
            print(jatekosok.read())
            print('-'*50)
        elif menu=="2":
            print('-'*50)
            print("Megoldások kérdések sorrendjében:\n")
            for pe in tesztsor:
                print(pe.feladvany)
                print(f"=="*30)
                print(pe.s)
                print(f"--"*10)
                print("\t")
            print('-'*50)
        elif menu=="3":
            print("\n Reméljük újra látunk!!") 
            time.sleep(1)
            os.system('cls')
            menu = False
        elif menu !="":
            print("\n Hibás sorszám!Irj be egy újat!") 
            menu = True

def loading():
    print("Eredmény betöltése...")
    for i in range(0, 100):
        time.sleep(0.01)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print