from random import randint


zmienna1 = '''
-------
|     |
|  o  |
|     |
-------
'''
zmienna2 = '''
-------
| o   |
|     |
|   o |
-------
'''
zmienna3 = '''
-------
| o   |
|  o  |
|   o |
-------
'''
zmienna4 = '''
-------
| o o |
|     |
| o o |
-------
'''
zmienna5 = ''' 
-------
| o o |
|  o  |
| o o |
-------
'''
zmienna6 = '''
-------
| o o |
| o o |
| o o |
-------
'''

while True:
    try:
        x = int(input('Iloma kostkami chcesz rzucic?: '))
    except ValueError:
        print ('Musisz wpisać liczbę !')
    else:
        break
if x == 0:
        print ('Poddajesz się ? ')

for x in range (x):
    rzut = randint (1,7)
    print ('rzut nr ',x+1)
    print()

    if rzut == 1:
        print(zmienna1)


    if rzut == 2:
        print(zmienna2)


    if rzut == 3:
        print(zmienna3)


    if rzut == 4:
        print(zmienna4)


    if rzut == 5:
        print(zmienna5)


    if rzut == 6:
        print(zmienna6)


print ()




































