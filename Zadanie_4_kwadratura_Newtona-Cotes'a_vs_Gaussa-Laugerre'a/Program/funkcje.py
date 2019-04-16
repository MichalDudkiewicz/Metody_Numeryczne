from numpy import sin, cos
from horner import horner


def wartosc_funkcji(x, wybor_funkcji):
    """
    :param x: argument funkcji (float)
    :param wybor_funkcji: wybor funkcji z dostępnych (String)
    :return: wartość wybranej funkcji
    """
    wartosc = None
    if wybor_funkcji in "A":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "B":
        wartosc = abs(x - 5)
    elif wybor_funkcji in "C":
        wartosc = 2**x
    elif wybor_funkcji in "D":
        wartosc = sin(x)
    elif wybor_funkcji in "E":
        wartosc = cos(x) - x**3
    return wartosc
