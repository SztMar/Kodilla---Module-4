import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def calculation (num1, num2):
    if type(num1) == int or type(num1) == float and type(num2) == int or type(num2) == float:

        if remarks == 1:
            logging.info(f"Dodaję {num1} i {num2}")
            result = num1 + num2
            print(f"Wynik to: {result}")
        elif remarks == 2:
            logging.info(f"Odejmuję {num1} i {num2}")
            result = num1 - num2
            print(f"Wynik to: {result}")
        elif remarks == 3:
            logging.info(f"Mnożę {num1} i {num2}")
            result = num1 * num2  
            print(f"Wynik to: {result}")  
        elif remarks == 4:
            logging.info(f"Dzielę {num1} i {num2}")
            result = num1 / num2  
            print(f"Wynik to: {result}")  
        else:
            logging.info("Wybierz odpowiednią liczbę z listy.")
            exit(1)

if __name__ == "__main__":

    remarks = int(input("Podaj działanie, posługując się odpowiednią liczbą:1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    num1 = float(input("Podaj składnik 1:"))
    num2 = float(input("Podaj składnik 2:"))
    calculation(num1,num2)
