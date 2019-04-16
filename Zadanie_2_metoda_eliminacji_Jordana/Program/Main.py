from math import ceil
from metoda_eliminacji_Jordana import jordan    # import z pliku metoda_eliminacji_Jordana funkcji Jordan

# Michał Dudkiewicz, Marcjan Jędrzejczak COPYRIGHT SIGN :D

print("""Witaj w programie obliczajacym rozwizania dowolnego ukladu rownan metoda eliminacji Jordana.
Prosze przed uruchomieniem programu wpisac uklad rownan, ktory ma zostac obliczony do pliku dane.txt 
znajdujacym sie w tym samym folderze. Poszczegolne elementy macierzy nalezy oddzielic conajmniej jedna spacja. 
Natomiast macierz i wektor nalezy umiescic w jednym wierszu oddzielone znakiem "|"
        """)

with open("dane.txt", 'r') as dane:  # otwieramy plik dane.txt jako dane w celu wczytania z niego układu równań
    wiersz_tekstu = dane.read().splitlines()  # wczytujemy kolejne równania w formie tekstu i zapisujemy je do listy
wiersz_tekstu_kopia = wiersz_tekstu.copy()
for item in wiersz_tekstu_kopia:
    if item in '':
        del wiersz_tekstu[wiersz_tekstu.index(item)]
liczba_wierszy = len(wiersz_tekstu)     # liczba wierszy/kolumn to liczba wierszy tekstu pliku dane.txt
print(liczba_wierszy)
wiersze = []    # deklarujemy pustą listę na gotowe elementy macierzy we właściwym formacie bez elementów wektora
wektor = []  # deklaracja pustego wektora
for numer_wiersza in wiersz_tekstu:     # przesuwamy się po kolejnych równaniach
    liczba = ""  # zmienna która będzie nam potrzebna do łączenie wieloznakowych elementów macierzy w jeden element
    for cyfra in numer_wiersza[:numer_wiersza.index("|")+1]:
        # w kolejnych równaniach przesuwamy się po poszczególnych znakach w tych równaniach
        # do momentu gdy napotkamy znak "|"
        if cyfra in ".-0123456789":
            # gdy napotkany znak jest różny od spacji oraz nie dotarto do końca macierzy "|"
            # zapisujemy go do zmiennej liczba i dodajemy do poprzedniej cyfry
            liczba += cyfra
        else:   # gdy napotkano spacje lub koniec wiersza macierzy
            if liczba:    # jeśli cyfra jest różna od "" (None)
                wiersze.append(float(liczba))  # rozszerz listę współczynników o ta liczbe
            liczba = ""  # w przypadku gdy napotkano spację lub koniec wiersza to liczbie przypisz None
            # zakoncz łączenie cyfr liczby
    for cyfra in numer_wiersza[numer_wiersza.index("|") + 1:]:
        # przesuwamy się po znakach w poszczególnych wierszach
        if cyfra in ".-0123456789":   # jeśli znak jest różny od spacji i końca linii
            liczba += cyfra        # zapisz wartość cyfry i dodaj do poprzedniej
        else:   # jeśli dotarto do końca wiersza lub spacji
            if liczba:         # jeśli liczba istnieje
                wektor.append(float(liczba))
                # przekonwertuj i zapisz liczbe do wektora
            liczba = ""   # liczbie przypisz None
    wektor.append(float(liczba))  # ostatnią wartość do wektora musimy dołączyć poza pętlą,
    # gdyz pętla kończy się przed ostatnim przypisaniem
macierz = []        # deklaracja nowej macierzy
for i in range(liczba_wierszy):
    macierz.append(list(wiersze[(i * liczba_wierszy):((i + 1) * liczba_wierszy)]))
    # nowej macierzy przypisz liste poszczególnych wierszy elementów (lista list)
wynik = jordan(macierz, wektor)     # oblicz wynik w formie listy fukcji jordan
if wynik is not None:   # jeśli układ nie jest ani sprzeczny ani nieoznaczony
    print("Otrzymane wyniki: ")
    for i in range(liczba_wierszy):      # wyświetla wyniki w czytelnej formie
        if wynik[i] == ceil(wynik[i]):
            print("x{0} = {1}".format(i + 1, int(wynik[i])))    # format dla wyników całkowitych
        else:
            print("x{0} = {1}".format(i + 1, wynik[i]))  # dla wyników zmiennoprzecinkowych
