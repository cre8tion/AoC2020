def get_total_questions():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        temp_lst = []
        group_lst = []

        # Formatting input into groups containing every person in the group for traversal
        for i in range(len(text_lst)):
            if i == len(text_lst) - 1:
                group_lst.append(temp_lst)

            if text_lst[i] != "":
                temp_lst.append(text_lst[i])
            else:
                group_lst.append(temp_lst)
                temp_lst = []
        
        total_questions_answered = 0

        for group in group_lst:
            # Using Set as Storage
            questions_set = set()

            for person in group:
                for i in range(len(person)):
                    questions_set.add(person[i])
            
            # Add total number of unique questions answered
            total_questions_answered += len(questions_set)
        
        return total_questions_answered

total = get_total_questions()
print(total)