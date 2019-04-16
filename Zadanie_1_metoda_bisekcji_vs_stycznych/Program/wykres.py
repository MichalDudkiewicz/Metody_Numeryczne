import pylab as pb  # do generowania wykresu
from funkcja import wzor_funkcji


def pokaz(rozwiazanie_bisekcja, rozwiazanie_newton, wybor, zmienna_iteracyjna):
    # funkcja pokazujaca wykres (nie ma potrzeby jej używać, ale jak już jest niech zostanie :P)
    pb.legend(['wykres funkcji f(x)', 'miejsce zerowe z metody bisekcji: {}'.format(rozwiazanie_bisekcja),
               'miejsce zerowe z metody Newtona: {}'.format(rozwiazanie_newton)],
              loc='upper left')  # tworzy legendę wykresu
    pb.title('f(x)=' + str(wzor_funkcji(wybor)))  # tworzy tytuł wykresu
    pb.grid(True)  # tworzy siatke na wykresie
    pb.xlabel("x")  # opis osi x
    pb.ylabel("y")  # opis osi y
    fig = pb.gcf()
    fig.canvas.set_window_title('Wykres ' + str(zmienna_iteracyjna))
    print("Prosze zamknac okno z Wykresem {} aby kontynuowac".format(zmienna_iteracyjna))
    pb.show(block=True)  # pokazuje wykres
