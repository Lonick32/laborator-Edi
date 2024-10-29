meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

numar_comenzi = {"papanasi": 0, "ceafa": 0, "guias": 0}

print("Comenzi:")
while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tavi.pop(0)

    print(f"{student} a comandat {comanda}.")
    istoric_comenzi.append((student, comanda))
    
    numar_comenzi[comanda] += 1
    meniu.remove(comanda)

print("\nInventar:")
print(f"S-au comandat {numar_comenzi['guias']} guias, {numar_comenzi['ceafa']} ceafa, {numar_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {'ceafa' in meniu}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu}.")
print(f"Mai sunt guias: {'guias' in meniu}.")

total_incasari = sum(numar_comenzi[produs] * pret for produs, pret in preturi if produs in numar_comenzi)
produse_ieftine = [produs for produs in preturi if produs[1] <= 7]

print("\nBani:")
print(f"Cantina a încasat: {total_incasari} lei.")
print(f"Produse care costă cel mult 7 lei: {produse_ieftine}.")
