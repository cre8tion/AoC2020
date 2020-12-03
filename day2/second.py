def valid_passwords_two():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        lst = [i.split(" ") for i in text_lst]
        
        count = 0

        for i in lst:
            num_range = i[0]
            num_range_lst = num_range.split('-')

            char = i[1][:1]
            
            first_position = False
            second_position = False

            if i[2][int(num_range_lst[0])-1] == char:
                first_position = True
            if i[2][int(num_range_lst[1])-1] == char:
                second_position = True
            
            if (first_position ^ second_position == True):
                count += 1
        
        return count


result = valid_passwords_two()
print(result)