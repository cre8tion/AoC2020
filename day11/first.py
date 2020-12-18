import copy

def final_occupied_seats():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        seat_lst = [list(i) for i in text_lst]
        
        # Setting the lengths
        col_length = len(seat_lst)
        row_length = len(seat_lst[0])
        
        new_seat_lst = copy.deepcopy(seat_lst)
        
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

                        # Checking if adjacent seats are occupied
                        if j - 1 in range(row_length) and seat_lst[i][j-1] == "#":
                            count += 1
                        if j + 1 in range(row_length) and seat_lst[i][j+1] == "#":
                            count += 1
                        if i - 1 in range(col_length) and seat_lst[i-1][j] == "#":
                            count += 1
                        if i + 1 in range(col_length) and seat_lst[i+1][j] == "#":
                            count += 1
                        if j - 1 in range(row_length) and i - 1 in range(col_length) and seat_lst[i-1][j-1] == "#":
                            count += 1
                        if j - 1 in range(row_length) and i + 1 in range(col_length) and seat_lst[i+1][j-1] == "#":
                            count += 1
                        if j + 1 in range(row_length) and i - 1 in range(col_length) and seat_lst[i-1][j+1] == "#":
                            count += 1
                        if j + 1 in range(row_length) and i + 1 in range(col_length) and seat_lst[i+1][j+1] == "#":
                            count += 1
                        
                        # If occupied seats and 4 or more occupied adjacent seats
                        if count >= 4 and seat_lst[i][j] == "#":
                            new_seat_lst[i][j] = "L"
                        
                        # If unoccupied seats and no occupied adjacent seats
                        elif count == 0 and seat_lst[i][j] == "L":
                            new_seat_lst[i][j] = "#"
        
        occupied_seats_count = 0

        # Count number of occupied seats
        for i in range(col_length):
            occupied_seats_count += new_seat_lst[i].count("#")
        
        return occupied_seats_count
            
occupied_seats = final_occupied_seats()
print(occupied_seats)