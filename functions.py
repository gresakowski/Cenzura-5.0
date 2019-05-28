# funkcja otwierająca plik z istniejącą listą słów i tworząca listę na jego podstawie
def open_file():
    cenz_file = open('spis.txt','r')
    cenz = [line.strip() for line in cenz_file.readlines()]
    cenz_file.close()
    return cenz


# cenzura0 - wykropkowanie wszystkich znaków cenzurowanego wyrazu
def cenzura0(a1,b):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>']
    a_cenz = []
    for a in a1:
        last_char = a[(len(a) - 1)]
        if last_char in interpunction:
            aa = a[0:(len(a) - 1)]
            if aa.lower() in b:
                a = '.' * (len(a)-1) + ' ' + a[(len(a)-1)]
                a_cenz.append(a)
            else:
                a_cenz.append(a)
        else:
            if a.lower() in b:
                a = '.' * (len(a))
                a_cenz.append(a)
            else:
                a_cenz.append(a)
    a_cenz = ' '.join(a_cenz)
    return a_cenz


# cenzura1 - wykropkowanie wszystkich znaków cenzurowanego wyrazu, z wyjątkiem pierwszego
def cenzura1(a1,b):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>']
    a_cenz = []
    for a in a1:
        last_char = a[(len(a)-1)]
        if last_char in interpunction:
            aa = a[0:(len(a)-1)]
            if aa.lower() in b:
                a = a[0] + '.' * (len(a) - 2) + ' ' + a[(len(a) - 1)] #  +' '+ żeby kropkowanie nie zlewało się ze znakiem int. Wydłuża to wynik o jeden znak
                a_cenz.append(a)
            else:
                a_cenz.append(a)
        else:
            if a.lower() in b:
                a = a[0] + '.'*(len(a)-1)
                a_cenz.append(a)
            else:
                a_cenz.append(a)
    a_cenz = ' '.join(a_cenz)
    return a_cenz


# cenzura2 - wykropkowanie wszystkich znaków cenzurowanego wyrazu, z wyjątkiem pierwszego i ostatniego
def cenzura2(a1,b):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>']
    a_cenz = []
    for a in a1:
        last_char = a[(len(a)-1)]       # ostatni znak ciągu znaków
        if last_char in interpunction: # jeżeli ostatni znak to znak interpunkcyjny
            aa = a[0:(len(a)-1)]        # słowo bez znaku
            if aa.lower() in b:
                a = a[0] + '.' * (len(a) - 3) + a[(len(a)-2)] + a[(len(a)-1)]
                a_cenz.append(a)
            else:
                a_cenz.append(a)
        else:                       # jeżeli ostatni znak to nie znak interpunkcyjny
            if a.lower() in b:
                a = a[0] + '.' * (len(a) - 2) + a[(len(a) - 1)]
                a_cenz.append(a)
            else:
                a_cenz.append(a)
    a_cenz = ' '.join(a_cenz)
    return a_cenz


# funkcja do wybrania sposobu usunięcia słowa:
def wybór_stopnia(choice,a1,b):
    if choice == 0:
        result0 = cenzura0(a1,b)
    elif choice == 1:
        result0 = cenzura1(a1,b)
    elif choice == 2:
        result0 = cenzura2(a1, b)
    else:
        print('Podaj poprawnie wybrany stopień.')
    return result0


# cenzura_cont - funkcja umożliwiająca dalsze modyfikowanie tekstu
def cenzura_cont(a_cenz):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>']
    b1 = input('Który wyraz chcesz usunąć? ')
    a = a_cenz.split(' ')
    if b1 in a or b1.capitalize() in a or b1.upper() in a:
        b1 = (f'\n{b1}')
        cenz_file = open('spis.txt', 'a')
        cenz_file.write(b1)
        cenz_file.close()
    elif b1 not in a or b1.capitalize() in a and b1.upper() not in a:
        for i in interpunction:
            b1 += i
            if b1 in a or b1.capitalize() in a or b1.upper() in a:
                b1 = b1[0:(len(b1)-1)]
                b1 = (f'\n{b1}')
                cenz_file = open('spis.txt', 'a')
                cenz_file.write(b1)
                cenz_file.close()
            else:
                pass
    else:
        print('Podane słowo nie występuje w tekście lub zostało już z niego usunięte')