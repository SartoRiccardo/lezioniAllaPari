# Import
from control.control import Control

# Variabili
boolD = False

# Funzioni


if __name__ == '__main__':
    if boolD:
        print("Inizio Programma\n")

    from control.io_manager import getTest
    print(getTest(2))
    Control()

    if boolD:
        print("\nFine Programma")
