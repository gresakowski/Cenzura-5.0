from functions import open_file, cenzura0, cenzura1, cenzura2, cenzura_cont, wybór_stopnia

a0 = input('Podaj tekst do ocenzurowania: ')
b = open_file()                             # stworzenie listy wulgaryzmów
a2 = a0.split(' ')


while True:
    choice0 = input("""W jaki sposób chcesz usunąć wulgaryzmy w tekście? 
        0 - usunąć cały wyraz;
        1 - pozostawić pierwszą literę;
        2 - pozostawić pierwszą i ostatnią literę;
    Wybór: """)
    if choice0 == '0' or choice0 == '1' or choice0 == '2':
        result0 = wybór_stopnia(choice0,a2,b)
        break
    else:
        print('Podaj poprawnie wybrany stopień.')
        print("\n")


choice = ''
print(f'\nTeskt oryginalny: \n{a0}')
print(f'\nTekst po naniesieniu wstępnych poprawek: \n{result0}')
while True:
    choice = input('\nCzy chcesz poddać tekst dalszym modyfikacjom (T/N)? ')
    choice = choice.upper()
    if choice == 'T':
        cenzura_cont(result0)
        b = open_file()
        result0 = wybór_stopnia(choice0,a2,b)
        print(f'\nTekst po dodatkowych modyfikacjach: \n{result0}')
    elif choice == 'N':
        print(f'\n\nOstateczna wersja tekstu:\n{result0}')
        break
