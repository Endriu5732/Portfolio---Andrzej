szukane_slowo = input('Co zjadłeś? ')
print("Nazwa kcal	białka	tłuszcze	węglowodany - w 100 gramach produktu")
with open('C:/Users/HP-Endi/PycharmProjects/przyklady/lista_produktow.txt', 'r', encoding='UTF-8') as plik:

    for linia in plik:
        if szukane_slowo in linia:
            print(linia.strip())