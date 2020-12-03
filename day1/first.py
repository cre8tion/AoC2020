def pairs():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [int(i.replace("\n", "")) for i in input_list]
        
        for i in text_lst:
            if 2020-i in text_lst:
                return (i, 2020-i)

pair = pairs()

result = pair[0] * pair[1]
print(result)