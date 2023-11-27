from menu import *
from funcion import *


if __name__ == "__main__":
    #read ranking
    ranking = read_data("programacion\ejercicios\pygame\data.json")
    print(ranking)
    ejecutar_menu(ranking)
