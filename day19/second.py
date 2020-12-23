# REGEX, semi-adapted
import re

def match_rule_0():
    with open('input2.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        rules_lst = text_lst[:134]
        expression_lst = text_lst[135:]

        # Dictionary of rules
        rules = dict([rule.split(': ', 1) for rule in rules_lst])

        # Recursive function to get full string
        full_re = get_re('0', rules)
        
        count = 0

        for i in expression_lst:
            if re.fullmatch(full_re, i):
                count += 1

        return count
        

def get_re(rule_num, rules):
    rule = rules[rule_num]

    if rule_num == "8":
        # Include + sign for 8 for regex
        return get_re("42", rules) + "+"
    
    if rule_num == "11":
        a = get_re('42', rules)
        b = get_re('31', rules)
        
        # Limit the loops to 100
        return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'

    # If rule == "a" or "b"
    if re.fullmatch(r'"."', rule):
        return rule[1]
    
    else:
        # List of left and right sides
        sides = rule.split(" | ")
        re_lst = []

        # Loop through first and second rule
        for part in sides:
            nums = part.split(" ")
            # Regex from recursion
            temp_lst = [get_re(num, rules) for num in nums]

            re_lst.append(''.join(temp_lst))
        
        return '(?:' + '|'.join(re_lst) + ')'

result = match_rule_0()
print(result)