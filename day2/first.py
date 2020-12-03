def valid_passwords():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        lst = [i.split(" ") for i in text_lst]
        
        count = 0

        for i in lst:
            num_range = i[0]
            num_range_lst = num_range.split('-')

            char = i[1][:1]
            
            sentence_count = i[2].count(char)

            if sentence_count >= int(num_range_lst[0]) and sentence_count <= int(num_range_lst[1]):
                count += 1
        
        return count



result = valid_passwords()
print(result)