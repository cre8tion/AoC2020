def find_first_invalid_number():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        # Preamble list
        preamble = text_lst[:25]

        # Find Invalid Number
        for i in range(25, len(text_lst)):
            # Invalid number
            if not sum_in_preamble(int(text_lst[i]), preamble):
                return int(text_lst[i])
            else:
                # Adjust for new preamble
                preamble = gen_new_preamble(preamble, int(text_lst[i]))

def sum_in_preamble(value, preamble):
    # Loop through preamble to see if sum of any pairs equals to target value
    for i, item in enumerate(preamble):
        for j in range(i+1, len(preamble)):
            total_of_two_items = int(preamble[i]) + int(preamble[j])
            if(total_of_two_items == value):
                return True
    return False

def gen_new_preamble(preamble, num):
    preamble.append(num)
    preamble.pop(0)
    return preamble

first_invalid_num = find_first_invalid_number()
print(first_invalid_num)
