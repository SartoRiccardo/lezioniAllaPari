# Import
from control.control import Control

# Variabili
boolD = False

# Funzioni


if __name__ == '__main__':
    if boolD:
        print("Inizio Programma\n")

    from control.io_manager import getTestScore
    print(getTestScore(10, "pizidavi"))

    Control()

    if boolD:
        print("\nFine Programma")
