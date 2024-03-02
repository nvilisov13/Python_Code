# Program for solving simple equations. Demo in YouTube link -> https://youtu.be/fu2618xLcp4?si=vxn5eXCADuaYOaAJ
# pip install matplotlib
import re
from pylab import *


def input_eq():
    equation = input('Введите уравнение: ')
    equation = equation.replace(' ', '').lower()
    reg_exp = r'[0-9]+|[a-z]|[=+*/-]'
    res = re.findall(reg_exp, equation)
    return res


def parsing_eq(list_eq):
    unk_num = 'abcdefghijklmnopqrstuvwxyz'
    sign_char = '-+*/'
    pos_x = char = sign = number = res_eq = ''
    if len(list_eq) == 5:
        i = 0
        while i < len(list_eq) - 1:
            if list_eq[i] in unk_num:
                char = list_eq[i]
                pos_x = i
            elif list_eq[i] in sign_char:
                sign = list_eq[i]
            elif re.match(r'\d+', list_eq[i]):
                number = list_eq[i]
            i += 1
    res_eq = list_eq[-1]
    return [char, pos_x, sign, number, res_eq]


def solution_eq_decorator(func):
    def wrapper(list_eq):
        print(f"Вызвана функция solution_eq с аргументами: {list_eq}")
        start_gp = int(list_eq[-2])
        end_gp = int(list_eq[-1])
        result = func(list_eq)
        match list_eq[-3]:
            case '+':
                plot(range(start_gp, end_gp),
                     [i + i for i in range(start_gp, end_gp)], list_eq[0])
            case '-':
                plot(range(start_gp, end_gp),
                     [i - i for i in range(start_gp, end_gp)], list_eq[0])
            case '*':
                plot(range(start_gp, end_gp),
                     [i * i for i in range(start_gp, end_gp)], list_eq[0])
            case '/':
                plot(range(start_gp, end_gp),
                     [i / i for i in range(start_gp, end_gp)], list_eq[0])
        show()
        return result
    return wrapper


@solution_eq_decorator
def solution_eq(list_eq):
    char, pos_x, sign, number, res_eq = list_eq
    pos_x = int(pos_x)
    number = int(number)
    res_eq = int(res_eq)
    res_x = 0.0
    dec_num = 3
    res_f = ''
    if pos_x == 0 and sign == '+':
        print(f"{char} = {res_eq} - {number}")
        res_x = res_eq - number
        res_f = f"{res_x} {sign} {number} = {res_eq}"
    elif pos_x != 0 and sign == '+':
        print(f"{char} = {res_eq} - {number}")
        res_x = res_eq - number
        res_f = f"{number} {sign} {res_x} = {res_eq}"
    elif pos_x == 0 and sign == '-':
        print(f"{char} = {res_eq} + {number}")
        res_x = res_eq + number
        res_f = f"{res_x} {sign} {number} = {res_eq}"
    elif pos_x != 0 and sign == '-':
        print(f"{char} = {number} - {res_eq}")
        res_x = number - res_eq
        res_f = f"{number} {sign} {res_x} = {res_eq}"
    elif pos_x == 0 and sign == '*':
        print(f"{char} = {res_eq} / {number}")
        res_x = round((res_eq / number), dec_num)
        res_f = f"{res_x} {sign} {number} = {res_eq}"
    elif pos_x != 0 and sign == '*':
        print(f"{char} = {res_eq} / {number}")
        res_x = round((res_eq / number), dec_num)
        res_f = f"{number} {sign} {res_x} = {res_eq}"
    elif pos_x == 0 and sign == '/':
        print(f"{char} = {res_eq} * {number}")
        res_x = res_eq * number
        res_f = f"{res_x} {sign} {number} = {res_eq}"
    elif pos_x != 0 and sign == '/':
        print(f"{char} = {res_eq} / {number}")
        res_x = round((number / res_eq), dec_num)
        res_f = f"{number} {sign} {res_x} = {res_eq}"
    print(res_f)
    print(f"{char} = {res_x}")
    return


try:
    solution_eq(parsing_eq(input_eq()))
except:
    print('Не соответствует введенному формату уравнений!')
