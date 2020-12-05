def get_seat_ids():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        seat_ids_lst = []

        for i in text_lst:
            row = get_row(i[:7])
            col = get_col(i[7:])
            seat_ids_lst.append(int((row * 8) + col))
        
        return seat_ids_lst


def get_row(inp):
    minimum = 0
    maximum = 127
    for i in inp:
        if(maximum-minimum != 1):
            if i == "F":
                maximum = ((maximum + minimum + 1)/2) - 1
            elif i == "B":
                minimum += ((maximum - minimum + 1)/2)
        else:
            if i == "F":
                return minimum
            elif i == "B":
                return maximum


def get_col(inp):
    minimum = 0
    maximum = 7
    for i in inp:
        if(maximum-minimum != 1):
            if i == "L":
                maximum = ((maximum + minimum + 1)/2) - 1
            elif i == "R":
                minimum += ((maximum - minimum + 1)/2)
        else:
            if i == "L":
                return minimum
            elif i == "R":
                return maximum

def find_missing_id(lst):
    for i in range(len(lst)):
        if i == 0:
            prev = lst[0]
        else:
            if lst[i] - 2 == prev:
                return lst[i] - 1
            else:
                prev = lst[i]


seat_ids = get_seat_ids()
seat_ids.sort()

your_id = find_missing_id(seat_ids)
print(your_id)