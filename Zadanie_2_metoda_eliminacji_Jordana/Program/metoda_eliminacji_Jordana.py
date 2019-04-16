def jordan(macierz, wektor):
    """
    :param macierz: macierz wczytana z pliku dane.txt po przekształceniach do formatu listy list nxn
    :param wektor: wektor wczytany z pliku dane.txt po przekształceniach do formatu listy nx1
    :return: wektor wynikowy w formie listy nx1
    """
    liczba_wierszy = len(wektor)     # liczbie wierszy (oraz kolumn) przypisujemy długość wektora
    # deklaracja listy buforowej nxn użytej później do zapamiętywania współczynników konkretnego wiersza macierzy
    lista_buforowa = [0] * liczba_wierszy
    for k in range(liczba_wierszy):   # przesuwanie się po wierszach macierzy
        # pod warunkiem spełniania założenia o niesprzeczności oraz oznaczoności układu
        for wiersz in macierz:      # przesuwamy się po kolejnych wierszach macierzy
            wiersz_kopia = [round(wartosc, 8) for wartosc in wiersz]     # zapisujemy aktualny wiersz (kopie)
            # oraz dokonujemy przybliżenia jego wartości w celu eliminacji błędu niedokładności
            # wynikającego z działaniach na float
            if wiersz_kopia == [0] * liczba_wierszy:        # sprawdzamy czy współczynniki macierzy są zerowe
                wektor_kopia = [round(wartosc, 8) for wartosc in wektor]
                # podobnie zapisujemy i przyblizamy wektor (kopie)
                if wektor_kopia[macierz.index(wiersz)] == 0:
                    # sprawdzamy czy aktualny wiersz macierzy składa się z samych zer i jednocześnie zerowy jest wektor
                    print("Układ nieoznaczony")   # jeśli tak to wyświetlamy komunikat o nieoznaczoności układu
                else:
                    # sprawdzamy czy aktualny wiersz macierzy składa się z samych zer
                    # i jednocześnie niezerowy jest wektor
                    print("Układ sprzeczny")  # jeśli tak to wyświetlamy komunikat o nieoznaczoności układu
                return None
                # wychodzimy z pętli
        maks = abs(macierz[k][k])    # tworzymy element max i przypisujemy mu wartość a_kk
        index = k   # tworzymy element index i przypisujemy do niego indeks aktualnego wiersza
        for i in range(liczba_wierszy - k):
            # przesuwanie się od zera do numeru kolumn w aktualnym wierszu podmacierzy
            if abs(macierz[k + i][k]) > maks:
                # szukamy elementu maksymalnego (podstawowego) w pierwszej kolumnie podmacierzy
                maks = abs(macierz[k + i][k])    # zapisujemy jego wartość
                index = k + i       # zapisujemy jego indeks
        # jeżeli indeks elementu podstawowego różni się od indeksu aktualnego wiersza to wykonujemy zamianę wierszy
        if index != k:
            for i in range(liczba_wierszy):
                lista_buforowa[i] = macierz[k][i]    # zapisujemy aktualny wiersz podmacierzy w liście buforowej
                macierz[k][i] = macierz[index][i]   # aktualny wiersz zamieniamy z wierszem z elementem podstawowym
                macierz[index][i] = lista_buforowa[i]
                # wiersz z elementem podstawowym zamieniamy z aktualnym wierszem podmacierzy
            bufor = wektor[index]   # tworzymy bufor przechowujący wiersz wektora z elementem podstawowym
            wektor[index] = wektor[k]
            # zamieniamy wiersz wektora z elementem podstawowym na aktualny wiersz podmacierzy
            wektor[k] = bufor   # zamieniamy aktualny wiersz podmacierzy z wierszem z elementem podstawowym
        akk = macierz[k][k]  # zapisujemy element podstawowy w zmiennej akk
        wektor[k] /= akk    # dzielimy aktualny wiersz wektora przez element podstawowy
        for j in range(liczba_wierszy - k):
            macierz[k][k + j] /= akk   # dzielimy cały aktualny wiersz podmacierzy przez element podstawowy
        for i in range(liczba_wierszy):
            if i != k:      # dla każdego wiersza róźnego od aktualnego wykonujemy operacje
                # dla każdego takiego wiersza zapisujemy element o indeksie aik gdzie i to indeks tego wiersza,
                # a k indeks wiersza aktualnego podmacierzy
                aik = macierz[i][k]
                wektor[i] -= wektor[k] * aik      # elementy wektora o indeksie różnym od k przekształcamy w ten sposób
                for j in range(liczba_wierszy):
                    macierz[i][j] -= macierz[k][j] * aik    # wiersze podmacierzy o indeksie różnym od k przekształcamy
    wektor = [round(x, 8) for x in wektor]
    # przybliżamy wartości wektora wynikowego eliminując błąd dokładności spowodowany działaniami na float
    return wektor   # zwróć wynik
