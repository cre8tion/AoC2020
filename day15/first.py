def find_number_spoken(position):
    with open('input.txt') as fin:
        input_list = fin.readlines()
        input_str = input_list[0]
        text_lst = input_str.split(",")
        text_lst = [int(i) for i in text_lst]

        # Dictionary to store spoken numbers with list of spoken turns
        spoken_dict = {}

        # Turn count to keep track
        turn = 1

        # Adding all provided inputs
        for i in text_lst:
            spoken_dict[i] = [turn]
            turn += 1

        # Loop through from turn to position required + 1
        for i in range(turn, position+1):

            # First turn after all provided inputs
            # The last number in provided input will be the first time the number has been spoken
            if i == turn:
                turn_lst = spoken_dict[0]
                turn_lst.append(turn)
                spoken_dict[0] = turn_lst
                last = 0
            
            # Other turns
            else:
                turn_lst = spoken_dict[last]
                # If last number spoken is not new number
                if len(turn_lst) > 1:
                    last = turn_lst[-1] - turn_lst[-2]
                
                # If last number spoken is new number, next number spoken must be 0
                else:
                    last = 0
                
                # If new number spoken is present in dictionary, update entry
                if last in spoken_dict:
                    last_lst = spoken_dict[last]
                    last_lst.append(i)
                    spoken_dict[last] = last_lst
                
                # If new number spoken is not present in dictionary, create new entry
                else:
                    spoken_dict[last] = [i]

        # Loop through all keys to find the number spoken in the required position
        for key in spoken_dict.keys():
            if position in spoken_dict[key]:
                return key

number_spoken = find_number_spoken(2020)
print(number_spoken)