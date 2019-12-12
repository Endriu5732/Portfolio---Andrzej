from datetime import date
from datetime import datetime
from datetime import timedelta
import calendar

while True:
    try:
        print ("Podaj datę początku cyklu, podając w liczbach: ")
        dzien, miesiac, rok = int(input("dzień: ")),int(input("miesiąc: ")),int(input("rok: "))
        dlugosc = int(input("Podaj długość cyklu: "))
    except ValueError: print ('Musisz wpisać liczbę !')
    else:
        break

if dzien or miesiac or rok or dlugosc == 0:
    print ('Program nieakceptuje wartości 0: ')

    try:
        start = date(rok,miesiac,dzien)
        w = int(dlugosc/2)

        najlepszy = start + timedelta(days=w)
        x = najlepszy + timedelta(days=6)
        y = najlepszy - timedelta(days = 6)
        print ('Cykl zaczyna się',start)
        print ('Dni płodne przypadają od: ',y,'do: ',x)
        print()
        print (calendar.month(theyear=rok,themonth=miesiac))
        print (calendar.month(theyear=rok,themonth=miesiac+1))
    except ValueError: print('Koniec programu')
    try:
        print ("Najlepszym dniem na zajście w ciąże jest dzień :", najlepszy)
        print ()
    except NameError: print()
