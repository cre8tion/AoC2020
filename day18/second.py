# Solution using operator precedence and evaluation, adapted

import re

# Using class to wrap int
class IntegerA(int):
    def __mul__(self, b):
        return IntegerA(int(self) + b)
    def __add__(self, b):
        return IntegerA(int(self) + b)
    def __sub__(self, b):
        return IntegerA(int(self) * b)

def solve_homework():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        
        homework_sum = 0

        for line in text_lst:
            expression = modify_expression(line)
            homework_sum += evaluate(expression)
        
        return homework_sum

# Evaluate the expression with the IntegerA class
def evaluate(expr):
    return eval(expr, {}, {"IntegerA": IntegerA})

# Replace value with Class value, making * same operator as + with -, + having higher precedence levels as *
def modify_expression(expr):
    expr = re.sub(r"(\d+)", r"IntegerA(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return expr

result = solve_homework()
print(result)