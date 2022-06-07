from modul import game_loop,  get_teszt, start, vege , loading


jatekmod = input("Játékmod:\n\t1.Egy játékos\n\t2.Két játékos\nJátékmód választás(1,2):\t")
# 
start(jatekmod)
# 
teszt = get_teszt()
# 
idok = []
pontszamok = []
pontszam:int = game_loop(teszt,jatekmod,pontszamok,idok)
# 
loading()
# 
print("\n")
print('\u001b[37m-'*30)

for i in pontszamok:
    pontok = i

for e in idok:
    idoszakmok = e
print(f"\u001b[1m|Elért pontszám(ok):\t{pontok} |")
# 
print(f"|Időtartam:\t{idoszakmok} másodperc  |")
# 
beiras = open('nev.txt' , 'a' , encoding='utf-8')
beiras.write(f"{pontok} pont\t")
beiras.write(f"{idoszakmok} ms\n")
beiras.close()
# 
jatekosok = open("nev.txt",'r', encoding='utf-8' )
print(f"|       GRATULÁLUNK!          |")
print('-'*30)
vege(teszt)