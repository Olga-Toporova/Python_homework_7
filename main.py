import user_interface
import model_div as md
from model_mult import multiplication as mp
from model_sub import subtraction as sb
from model_sum import summ
from model_sqrt import square_root as sr
from model_sqrt import square_root_compl as sc
from model_pow import raise_to_power as rp
from excep import check_input_compl, try_input, div_zero, div_zero_complex
from logg import operation

def input_number(variety):
    if variety == 'r': number = try_input()
    else: 
        number1, number2 = try_input(), try_input()
        number = check_input_compl(number1, number2)
    return number

def main_op(variety, choice_in):
    type_op = 0
    if choice_in != '6':
        a, b = input_number(variety), input_number(variety)
    if choice_in == '1':
        result = (summ(a, b))
        type_op = 'сумма'
    if choice_in == '2':
        result =(sb(a, b))
        type_op = 'разность'        
    if choice_in == '3':
        result =(mp(a, b))
        type_op = 'умножение' 
    if choice_in == '4':
        result =(md.div_complex(a, div_zero_complex(b)))
        type_op = 'деление'
    if choice_in == '4_1':
        result =(md.division(a, div_zero(b)))
        type_op = 'деление'
    if choice_in == '4_2':
        result =(md.div_integer(a, div_zero(b)))
        type_op = 'целочисленное деление'
    if choice_in == '4_3':
        result =(md.div_remainder(a, div_zero(b)))     
        type_op = 'остаток от деления'
    if choice_in == '5':
        result =(rp(a, b))
    if choice_in == '6':
        if variety == 'r':
            result =(sr(input_number(variety)))
        if variety == 'c':
            result = (sc(input_number(variety)))
        type_op = 'извлечение корня'
        b = "" 

    print(result)
    operation(variety, type_op, a, b, result)
    