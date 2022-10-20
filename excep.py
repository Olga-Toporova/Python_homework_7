
import compl as clx

def verification_start():
    while True:
        try:
            nr = input("Выберите опцию: ")
            if nr.isdigit and int(nr) in range(0,3): return nr
            else: print("Некорректный ввод, значение вне диапазона 0-2")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")

def verification_numbers():
    while True:
        try:
            nr = input("Выберите опцию: ")
            if nr.isdigit and int(nr) in range(0,7): return nr 
            else: print("Некорректный ввод, значение вне диапазона 0-6")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")

def verification_div_choisen():
    while True:
        try:
            nr = input("Выберите опцию: ")
            if nr.isdigit and int(nr) in range(0,4): return nr  
            else: print("Некорректный ввод, значение вне диапазона 0-3")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


def try_input():
    while True:
        try: 
            number = input('Введите значение: ')
            if number.count(".") or number.count(","): number = float(number)
            else: number = int(number)
            return number
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


def check_input_compl(number1, number2):
    while True:
        try:
            compl_number = clx.complex_number(number1, number2)
            return compl_number
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")

def div_zero(number):
    while number == 0:
        print("Делитель не может быть нулём!")
        number = try_input()
    return number

def div_zero_complex(number):
    while number == 0:
        print("Делитель не может быть нулём!")
        number1, number2 = try_input(), try_input()
        number = check_input_compl(number1, number2)
    return number