meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Istoric comenzi
while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tava = tavi.pop(0)
    
    print(f"{student} a comandat {comanda}.")
    
    istoric_comenzi.append((student, comanda))
    
istoric_comenzi

count_guias = sum(1 for _, comenzi in istoric_comenzi if comenzi == "guias")
count_papansi = sum(1 for _, comenzi in istoric_comenzi if comenzi == "papanasi")
count_ceafa = sum(1 for _, comenzi in istoric_comenzi if comenzi == "ceafa")

tavi_ramase = len(tavi)

ceafa_ramasa = meniu.count("ceafa")
papanasi_ramasi = meniu.count("papanasi")
guias_ramas = meniu.count("guias")

comenzi_status = f"\nS-au comandat {count_guias} guias, {count_ceafa} ceafa si {count_papansi} papanasi."
tavi_status = f"\nMai sunt {tavi_ramase} tavi."
ceafa_status = f"\nMai sunt {papanasi_ramasi} papanasi."
guias_status = f"\n{guias_ramas} guias."
print(comenzi_status, tavi_status, ceafa_status, guias_status)
