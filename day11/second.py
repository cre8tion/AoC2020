import copy

def final_occupied_seats_2():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        seat_lst = [list(i) for i in text_lst]
        
        # Setting the lengths
        col_length = len(seat_lst)
        row_length = len(seat_lst[0])
        
        # Initialise seat list
        new_seat_lst = copy.deepcopy(seat_lst)
        
        # Seats Representation
        exit_lst = ["L", "#"]
        
        # Given an arbitary number of loops
        for t in range(100):
            # Copying the seat_arrangement_list
            seat_lst = copy.deepcopy(new_seat_lst)
            new_seat_lst = copy.deepcopy(seat_lst)

            for i in range(col_length):
                for j in range(row_length):
                    # If not floor
                    if seat_lst[i][j] != ".":
                        count = 0

                        # Initialise temporary variables
                        temp_j = copy.deepcopy(j)
                        temp_i = copy.deepcopy(i)

                        # Checking if adjacent first seat in each direction is occupied

                        while temp_j - 1 in range(row_length):
                            if seat_lst[i][temp_j-1] in exit_lst:
                                if seat_lst[i][temp_j-1] == "#":
                                    count += 1
                                break
                            else:
                                temp_j -= 1
                        
                        temp_j = copy.deepcopy(j)

                        while temp_j + 1 in range(row_length):
                            if seat_lst[i][temp_j+1] in exit_lst:
                                if seat_lst[i][temp_j+1] == "#":
                                    count += 1
                                break
                            else:
                                temp_j += 1
                        
                        temp_j = copy.deepcopy(j)
                        
                        while temp_i - 1 in range(col_length):
                            if seat_lst[temp_i-1][j] in exit_lst:
                                if seat_lst[temp_i-1][j] == "#":
                                    count += 1
                                break
                            else:
                                temp_i -= 1
                        
                        temp_i = copy.deepcopy(i)

                        while temp_i + 1 in range(col_length):
                            if seat_lst[temp_i+1][j] in exit_lst:
                                if seat_lst[temp_i+1][j] == "#":
                                    count += 1
                                break
                            else:
                                temp_i += 1
                        
                        temp_i = copy.deepcopy(i)

                        while temp_j - 1 in range(row_length) and temp_i - 1 in range(col_length):
                            if seat_lst[temp_i-1][temp_j-1] in exit_lst: 
                                if seat_lst[temp_i-1][temp_j-1] == "#":
                                    count += 1
                                break
                            else:
                                temp_i -= 1
                                temp_j -= 1
                        
                        temp_j = copy.deepcopy(j)
                        temp_i = copy.deepcopy(i)
                        
                        while temp_j - 1 in range(row_length) and temp_i + 1 in range(col_length):
                            if seat_lst[temp_i+1][temp_j-1] in exit_lst:
                                if seat_lst[temp_i+1][temp_j-1] == "#":
                                    count += 1
                                break
                            else:
                                temp_i += 1
                                temp_j -= 1
                        
                        temp_j = copy.deepcopy(j)
                        temp_i = copy.deepcopy(i)

                        while temp_j + 1 in range(row_length) and temp_i - 1 in range(col_length):
                            if seat_lst[temp_i-1][temp_j+1] in exit_lst:
                                if seat_lst[temp_i-1][temp_j+1] == "#":
                                    count += 1
                                break
                            else:
                                temp_i -= 1
                                temp_j += 1
                        
                        temp_j = copy.deepcopy(j)
                        temp_i = copy.deepcopy(i)
                        
                        while temp_j + 1 in range(row_length) and temp_i + 1 in range(col_length):
                            if seat_lst[temp_i+1][temp_j+1] in exit_lst:
                                if seat_lst[temp_i+1][temp_j+1] == "#":
                                    count += 1
                                break
                            else:
                                temp_i += 1
                                temp_j += 1
                        
                        # If occupied seats and 5 or more occupied adjacent seats
                        if count >= 5 and seat_lst[i][j] == "#":
                            new_seat_lst[i][j] = "L"
                        
                        # If unoccupied seats and no occupied adjacent seats
                        elif count == 0 and seat_lst[i][j] == "L":
                            new_seat_lst[i][j] = "#"
        
        occupied_seats_count = 0

        # Count number of occupied seats
        for i in range(col_length):
            occupied_seats_count += new_seat_lst[i].count("#")
        
        return occupied_seats_count
            
occupied_seats = final_occupied_seats_2()
print(occupied_seats)