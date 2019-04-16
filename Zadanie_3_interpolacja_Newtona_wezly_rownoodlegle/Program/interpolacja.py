from matematyka import silnia
import sympy as sp



def roznice_skonczone(tab_y):
    """
    obliczanie tabeli różnic skończonych
    :param tab_y: tabeli wartości funkcji
    :return: lista list różnic skończonych
    """
    liczba_wezlow_interpolacji = len(tab_y)
    delta_y = [[]]
    delta_y[0] = tab_y
    for licznik in range(1, liczba_wezlow_interpolacji):
        delta_y.append([round(delta_y[licznik - 1][i + 1] - delta_y[licznik - 1][i], 8)
                        for i in range(liczba_wezlow_interpolacji - licznik)])
    return delta_y


def interpolacja_wprzod(tab_x, tab_y):
    """
    Interpolacja dla pierwszej połowy przedziału interpolacji
    :param tab_x: lista wartości argumentow funkcji
    :param tab_y: lista wartości funkcji
    :return: wzór wielomianu interpolującego w pierwszej połowie przedziału
    """
    h = tab_x[1] - tab_x[0]
    liczba_wezlow = len(tab_y)
    delta_y = roznice_skonczone(tab_y)
    args_x = sp.Symbol('x')
    # if arg_x < (tab_x[0] + tab_x[-1]) / 2:
    q = (args_x - tab_x[0])/h
    wspolczynniki = []
    for i in range(liczba_wezlow):
        wspolczynniki.append(round(delta_y[i][0]/silnia(i), 4))
    wielomian = [wspolczynniki[0], q * wspolczynniki[1]]
    wspolczynniki_kopia = wspolczynniki.copy()
    wspolczynnik = wspolczynniki[-1]
    i = 1
    while wspolczynnik == 0 and len(wspolczynniki) > 1:
        del wspolczynniki[wspolczynniki.index(wspolczynnik)]
        wspolczynnik = wspolczynniki_kopia[-1 - i]
        i += 1
    qt = q
    for i in range(len(wspolczynniki) - 2):
        qt -= 1
        q *= qt
        wielomian.append(q * wspolczynniki[i + 2])
    wartosc = 0
    for item in wielomian:
        wartosc += item
    wartosc = sp.simplify(wartosc)
    return wartosc


def interpolacja_wstecz(tab_x, tab_y):
    """
     Interpolacja dla drugiej połowy przedziału interpolacji
     :param tab_x: lista wartości argumentow funkcji
     :param tab_y: lista wartości funkcji
     :return: wzór wielomianu interpolującego w drugiej połowie przedziału
     """
    args_x = sp.Symbol('x')
    h = tab_x[1] - tab_x[0]
    q = (args_x - tab_x[-1])/h
    liczba_wezlow = len(tab_y)
    delta_y = roznice_skonczone(tab_y)
    wspolczynniki = []
    for i in range(liczba_wezlow):
        wspolczynniki.append(round(delta_y[i][-1] / silnia(i), 4))
    wielomian = [wspolczynniki[0], q * wspolczynniki[1]]
    wspolczynniki_kopia = wspolczynniki.copy()
    wspolczynnik = wspolczynniki[-1]
    i = 1
    while wspolczynnik == 0 and len(wspolczynniki) > 1:
        del wspolczynniki[wspolczynniki.index(wspolczynnik)]
        wspolczynnik = wspolczynniki_kopia[-1 - i]
        i += 1
    qt = q
    for i in range(len(wspolczynniki) - 2):
        qt += 1
        q *= qt
        wielomian.append(q * wspolczynniki[i + 2])
    wartosc = 0
    for item in wielomian:
        wartosc += item
    wartosc = sp.simplify(wartosc)
    return wartosc
