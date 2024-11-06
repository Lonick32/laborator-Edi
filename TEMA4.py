import random

def cuvant_random():
    cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
    return random.choice(cuvinte)
    
def status(cuvinte, litere_ghicite, incercari_ramase):
    afiseaza_cuvant = [litera if litera in litere_ghicite else "_" for litera in cuvinte]
    print("Cuvant: " + "".join(afiseaza_cuvant))
    print(f"Incercari ramase: {incercari_ramase}")
    print(f"Litere ghicite: {litere_ghicite}")

print("Joc Spanzuratoare\n")

def play_spanzuratoare():
    cuvant = cuvant_random()
    litere_ghicite = set()
    incercari_ramase = 6
    castigat = False
    
    while incercari_ramase > 0:
        status(cuvant, litere_ghicite, incercari_ramase)
        ghicit = input("Scrie o litera: ")
        
        if len(ghicit) != 1 or not ghicit.isalpha():
            print("Scrie o singura litera")
            continue
        
        if ghicit in litere_ghicite:
            print("Ai scris litera")
            continue
        
        litere_ghicite.add(ghicit)
        
        if ghicit in cuvant:
            if all(cuvant in litere_ghicite for cuvant in cuvant for litera in cuvant):
                castigat = True
                break
        else:
            incercari_ramase -= 1
            print("Gresit")
    
    if castigat:
        print(f"Ai castigat! Cuvantul a fost {cuvant}")
    else:
        print(f"Ai pierdut! Cuvantul a fost {cuvant}")
        
play_spanzuratoare()
