def check_nearby_tickets():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        
        fields_lst = text_lst[:20]
        fields_lst = [i.split(": ") for i in fields_lst]
        
        fields_name_lst = [i[0] for i in fields_lst]
        fields_lst = [i[1].split(" or ") for i in fields_lst]

        my_ticket = text_lst[22:23][0]
        my_ticket = my_ticket.split(",")
        my_ticket = [int(i) for i in my_ticket]
        
        nearby_tickets_lst = text_lst[25:]
        nearby_tickets_lst = [i.split(",") for i in nearby_tickets_lst]
        

        # Generate valid range of numbers from all given fields
        valid_range = generate_valid_range(fields_lst)
        
        # Filter for only valid tickets
        valid_tickets_lst = filter_valid_tickets(nearby_tickets_lst, valid_range)
        
        # Dictionary to store range of values for each field
        fields_dic = create_fields_dic(fields_lst, fields_name_lst)

        # Dictionary to store possible indexes in all tickets for each field
        fields_indexes_dic = find_fields_indexes(fields_dic, valid_tickets_lst)

        # Dictionary to map one field to one index
        fields_index_dic = assign_fields_to_index(fields_indexes_dic)

        # List to store values with "departure "
        departure_values = []

        for key in fields_index_dic.keys():
            if key.startswith("departure"):
                idx = fields_index_dic[key]
                departure_values.append(my_ticket[idx])
        
        ans = 1
        for i in departure_values:
            ans *= i
        return ans
        

def find_fields_indexes(fields_dic, tickets_lst):
    fields_index_dic = {}
    num_tickets = len(tickets_lst)
    num_values = len(tickets_lst[0])

    for j in range(num_values):
        for key in fields_dic.keys():
            valid_key = True
            for i in range(num_tickets):
                if int(tickets_lst[i][j]) not in fields_dic[key]:
                    valid_key = False
                    break
            
            if valid_key:
                if key not in fields_index_dic:
                    fields_index_dic[key] = [j]
                else:
                    lst = fields_index_dic[key]
                    lst.append(j)
                    fields_index_dic[key] = lst
    
    return fields_index_dic

def assign_fields_to_index(fields_indexes_dic):
    fields_index_dic = {}
    idx_lst = []

    sorted_dic =  sorted(fields_indexes_dic.items(), key=lambda item: len(item[1]))

    for item in sorted_dic:
        for index in item[1]:
            if index not in idx_lst:
                idx_lst.append(index)
                fields_index_dic[item[0]] = index
                break
    
    return fields_index_dic
    

def create_fields_dic(fields_lst, fields_name_lst):
    fields_dic = {}

    for i in range(len(fields_lst)):
        range_lst = []

        left_range = fields_lst[i][0]
        right_range = fields_lst[i][1]
        left_range = left_range.split("-")
        right_range = right_range.split("-")
            
        for c in range(int(left_range[0]), int(left_range[1]) + 1):
            if c not in range_lst:
                range_lst.append(c)
        
        for c in range(int(right_range[0]), int(right_range[1]) + 1):
            if c not in range_lst:
                range_lst.append(c)
        
        fields_dic[fields_name_lst[i]] = range_lst

    return fields_dic

def generate_valid_range(fields):
    range_lst = []

    for i in fields:
        left_range = i[0]
        right_range = i[1]
        left_range = left_range.split("-")
        right_range = right_range.split("-")

        for c in range(int(left_range[0]), int(left_range[1]) + 1):
            if c not in range_lst:
                range_lst.append(c)
        
        for c in range(int(right_range[0]), int(right_range[1]) + 1):
            if c not in range_lst:
                range_lst.append(c)
    
    return sorted(range_lst)


def filter_valid_tickets(tickets_lst, valid_range):
    valid_tickets_lst = []

    for ticket in tickets_lst:
        valid = True
        for i in ticket:
            if int(i) not in valid_range:
                valid = False
                break
        if valid:
            valid_tickets_lst.append(ticket)
    
    return valid_tickets_lst

error_rate = check_nearby_tickets()
print(error_rate)