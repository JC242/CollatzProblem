import random
import time

def math():
    numero = random.randint(100,1000)

    print(numero)

    while numero > 0:
        if numero % 2 == 0:
            numero = numero /2
        else:
            numero = (3 * numero) + 1

        time.sleep(2)
        print(numero)

if __name__ == "__main__":
    math()