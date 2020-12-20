def initialization_program():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        # Using a dictionary to store the memory
        mem = {}

        for i in text_lst:
            if i.startswith('mask = '):
                # Set new mask
                mask = i.replace("mask = ", "")
                mask = list(mask)
                
            else:
                mem_lst = i.split(" = ")
                
                # Key of mem
                key = int(mem_lst[0][4:-1])

                # Binary list of value
                value = bin(int(mem_lst[1]))[2:]
                value_lst = list(value)
                
                new_value = apply_bitmask(mask, value_lst)

                mem[key] = new_value
        
        sum_memory = 0

        # Summing up all the values in the memory
        for key in mem.keys():
            num = "".join(mem[key])
            num = int(num,2)
            sum_memory += num

        return sum_memory
                

def apply_bitmask(mask, value):
    res = []

    # Loop from last char to first char of value list
    for i in range(-1,-len(value)-1,-1):
        # If mask is not present
        if mask[i] == "X":
            res.insert(0, value[i])
        # If mask is present
        else:
            res.insert(0, mask[i])
    
    # Loop from the char before first char of value list to first char of mask list
    for i in range(-len(value)-1, -len(mask)-1, -1):
        # If mask is not present
        if mask[i] == "X":
            res.insert(0, "0")
        # If mask is present
        else:
            res.insert(0, mask[i])
    
    return res

sum_memory = initialization_program()
print(sum_memory)