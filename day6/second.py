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
        
        total_questions_answered_all = 0

        for group in group_lst:
            # Using Dictionary as Storage
            questions_dict = {}
            
            for person in group:
                for i in range(len(person)):
                    question_count = questions_dict.get(person[i], 0)
                    question_count += 1
                    questions_dict[person[i]] = question_count
            
            for key, value in questions_dict.items():
                # Checking everyone answers the question
                if value == len(group):
                    total_questions_answered_all += 1
        
        return total_questions_answered_all

total = get_total_questions()
print(total)