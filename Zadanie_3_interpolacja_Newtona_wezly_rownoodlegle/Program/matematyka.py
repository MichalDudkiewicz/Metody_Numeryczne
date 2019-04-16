def silnia(x):
    """
    obliczanie silni z x
    :param x: liczba której chcemy obliczyć silnię (int)
    :return: wartośc silni z x (float)
    """
    n = x
    if x > 1:
        for i in range(1, x):
            n *= x - i
        return n
    elif x == 1 or x == 0:
        return 1
    else:
        print("Prosze podac dodatnia liczbe calkowita")
        return None