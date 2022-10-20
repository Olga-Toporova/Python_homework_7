from main import main_op 
import excep as ex
from sys import exit


def hello_main():
    print("Добро пожаловать в меню!\nВыберите, с чем хотите работать:\n1 - рациональные числа;\n2 - комплексные числа;\n0 - выход из программы")
    option = ex.verification_start(input("Выберите опцию: "))
    return option


def div_choice():
    print("Уточните какое деление требуется:\n1 - обычное деление;\n2 - целочисленное;\n3 - остаток от деления;\n0 - вернуться в предыдущее меню")
    option = ex.verification_div_choisen(input("Выберите опцию: "))
    if option == "0": rational_numbers()
    else: return option


def rational_numbers():
    print("Вы выбрали рациональные числа.\nВыберите, какую операцию хотите осуществить:\n1 - сложение;\n2 - вычитание;\n3 - умножение;\n4 - деление;\n5 - возведение в степень;\n6 - корень из числа;\n0 - вернуться в предыдущее меню")
    option = ex.verification_numbers(input("Выберите опцию: "))
    if option == "0": 
        main_menu()
    elif option == "4":
        return main_op('r', f'4_{div_choice()}')
    else: main_op('r', f'{option}')


def complex_numbers():
    print("Вы выбрали комплексные числа.\nВыберите, какую операцию хотите осуществить:\n1 - сложение;\n2 - вычитание;\n3 - умножение;\n4 - деление;\n5 - возведение в степень;\n6 - корень из числа;\n0 - вернуться в предыдущее меню")
    option = ex.verification_numbers(input("Выберите опцию: "))
    if option == 0: hello_main()
    else: main_op('c', f'{option}')

def main_menu():
    option = hello_main()
    if option == "1":
        rational_numbers()
    elif option == "2":
        complex_numbers()
    elif option == "0":
        print("Заходите еще!")
        exit

main_menu()