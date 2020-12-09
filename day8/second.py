import copy

def get_final_acc_from_instructions():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        text_lst = [i.split(" ") for i in text_lst]

        current_acc = try_prevent_termination(text_lst)
        return current_acc

def try_prevent_termination(lst, ):
    for i in range(len(lst)-1, -1 , -1):
        if lst[i][0] == "jmp" or lst[i][0] == "nop":

            # Initalising variables
            current_acc = 0
            instr_index_lst = []
            current_instr=0

            # Creating copy to change command without affecting the original
            new_list = copy.deepcopy(lst)

            # Changing the command
            if new_list[i][0] == "jmp":
                new_list[i][0] = "nop"
            elif new_list[i][0] == "nop":
                new_list[i][0] = "jmp"

            # Run until new instruction is repeated
            while current_instr not in instr_index_lst:
                instr_index_lst.append(current_instr)
                command = new_list[current_instr][0]
                value = new_list[current_instr][1]

                # Running commands
                if command == "acc":
                    current_acc += int(value)
                    current_instr += 1
                elif command == "jmp":
                    current_instr += int(value)
                elif command == "nop":
                    current_instr += 1
                
                # Return current accumulator when a change in instruction results in successful termination
                if current_instr == len(lst) - 1:
                    return current_acc

final_acc = get_final_acc_from_instructions()
print(final_acc)