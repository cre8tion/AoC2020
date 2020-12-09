def get_final_acc_from_instructions():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        text_lst = [i.split(" ") for i in text_lst]

        # Initalising variables
        current_acc = 0
        instr_index_lst = []
        current_instr=0

        # Run until new instruction is repeated
        while current_instr not in instr_index_lst:
            instr_index_lst.append(current_instr)
            command = text_lst[current_instr][0]
            value = text_lst[current_instr][1]
            
            # Running commands
            if command == "acc":
                current_acc += int(value)
                current_instr += 1
            elif command == "jmp":
                current_instr += int(value)
            elif command == "nop":
                current_instr += 1

        return current_acc

final_acc = get_final_acc_from_instructions()
print(final_acc)
