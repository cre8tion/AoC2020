def check_nearby_tickets():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        
        fields_lst = text_lst[:20]
        fields_lst = [i.split(": ") for i in fields_lst]
        fields_lst = [i[1].split(" or ") for i in fields_lst]
        
        nearby_tickets_lst = text_lst[25:]
        nearby_tickets_lst = [i.split(",") for i in nearby_tickets_lst]
        
        # Generate valid range of numbers from all given fields
        valid_range = generate_valid_range(fields_lst)
        
        # List to hold all invalid values
        all_invalid_values = []

        for ticket in nearby_tickets_lst:
            # Get all invalid values in each ticket
            invalid_lst = check_validity(ticket, valid_range)
            all_invalid_values.extend(invalid_lst)
        
        return sum(all_invalid_values)


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


def check_validity(ticket, valid_range):
    invalid_values = []

    for i in ticket:
        if int(i) not in valid_range:
            invalid_values.append(int(i))
    
    return invalid_values


error_rate = check_nearby_tickets()
print(error_rate)