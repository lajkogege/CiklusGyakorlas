import math


def elso_feldat():
    i:int=0
    while i<= 150 :
        if i%2 ==0:
            print(i)
        i +=1
#Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
def masodik_feldat():
    i:int=0
    harommal_oszthato:int=0
    while i < 10:
        a:int=int(input("Kérek egy számot: "))
        i += 1
        if a %3==0:
            harommal_oszthato +=1
    print("Hárommal osztható számok összesen: ",harommal_oszthato)

#Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
def harmadik_feldat():
    szam:int=int(input("Kérek egy 10-el osztható számot: "))
    while not (szam % 10 ==0):
        print("10-el osztahtott!!")
        szam:int=int(input("Kérek egy 10-el osztható számot:"))
    print("A beirt szám osztahtó 10-el")

#Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def negyedik_feldat():
    szam:int=int(input("Kérek egy páros számot:"))
    while not (szam >= 10 and szam < 100 and szam %2==0 ):
        print("Nem jó számot adtál meg")
        szam: int = int(input("Kérek egy páros kétjegyűszámot:"))
    print(f"A {szam} páros és kettjegyű")

#Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*
def otodik_feldat():
    szam:int=int(input("Kérek egy pozitív páratlan számot:"))
    while (szam > 0 and( szam % 2 !=0)) :
        print("Ez nem páratlan!")
        szam: int = int(input("Kérek egy pozitív páratlan számot:"))
    print("Sikerült páratlan számot megadnod!")

def hatodik_feldat():
    szam:int=int(input("Kérek egy számot:"))
    while not (szam %3 == 0 or math.sqrt(szam) == int(math.sqrt(szam))):
        print("Nem osztható 3-mal és nem négyzett szám")
        szam: int = int(input("Kérek egy számot:"))
    if szam %3 == 0:
        print(f"A {szam} osztahtó 3-mal")
    elif math.sqrt(szam) == int(math.sqrt(szam)):
        print(f"A {szam} négyzett szám")
    else:
        print(f"A {szam} 3-mal osztahtó és negyzettszám is")

def hetedik_feldat():
    a:int=int(input("Kérem a háromszög egyik oldalát:"))
    b: int = int(input("Kérem a háromszög egyik oldalát:"))
    c: int = int(input("Kérem a háromszög egyik oldalát:"))
    while not ((a< b+c) and (b< a +c) and (c<a+b)):
        print("Nem szerkeszthető a 3-szög. Probáld újra!")
        a: int = int(input("Kérem a háromszög egyik oldalát:"))
        b: int = int(input("Kérem a háromszög egyik oldalát:"))
        c: int = int(input("Kérem a háromszög egyik oldalát:"))
    print("Szerkeszthető a háromszög")

#Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
def nyolcadik_feldat():
    szoveg:str=str(input("Kérek egy szöveget ami három karakteres: "))
    i:int=3
    while not (i == len(szoveg)):
        print("3 karakteres szöveget kérek")
        szoveg: str = str(input("Kérek egy szöveget ami három karakteres: "))
    nagy:str= szoveg.upper()
    print(nagy)

#Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
def kilencedik_feldat():
    szoveg:str=str(input("Kérek egy 4 karakteres kis betűs szót: "))
    i:int=4
    while not( i== len(szoveg) and szoveg.islower() ):
        print("4 karakteres kis betűs szót kérek!!")
        szoveg: str = str(input("Kérek egy 4 karakteres kis betűs szót: "))
    print("JÓ! Négy karakteres kis betűs szavat adtál meg!")

#Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!
def tizedik_feladat():
    szam:int=int(input("Kérek wgy számot: "))
    i:int=0
    while not (szam == 0):
        print(f"{szam:.2f}")
        szam: int = int(input("Kérek wgy számot: "))
    print("Vége")

#A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!
def tizenegyedik_feldat():
    szam: int = int(input("Kérek egy számot: "))
    i: int = 0
    while not (szam == 0):
        while not (szam > 0):
            print("Pozitiv számot adjál meg")
    szam: int = int(input("Kérek egy számot: "))
    print("Vége")