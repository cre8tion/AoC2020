from itertools import product

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
                
                # Original key of mem
                key = int(mem_lst[0][4:-1])
                key = bin(key)[2:]
                key_lst = list(key)

                # Value to be written
                value = int(mem_lst[1])
                
                # Generate new masked key with bitmask
                new_key = apply_bitmask_mem(mask, key_lst)

                # Obtain all possible addresses from new masked key
                addresses = get_addresses_from_masked_key(new_key)
                addresses = [int(i,2) for i in addresses]
                
                # Setting addresses and value
                for address in addresses:
                    mem[address] = value
        
        sum_memory = 0

        # Summing up all the values in the memory
        for key in mem.keys():
            num = mem[key]
            sum_memory += num

        return sum_memory
                

def apply_bitmask_mem(mask, key):
    new_key = []

    # Loop from last char to first char of key list
    for i in range(-1,-len(key)-1,-1):
        # If mask is X
        if mask[i] == "X":
            new_key.insert(0, "X")
        # If mask is 0
        elif mask[i] == "0":
            new_key.insert(0, key[i])
        # If mask is 1
        elif mask[i] == "1":
            new_key.insert(0, "1")
    
    # Loop from the char before first char of key list to first char of mask list
    for i in range(-len(key)-1, -len(mask)-1, -1):
        new_key.insert(0, mask[i])
    
    return new_key

def get_addresses_from_masked_key(key):
    num_xs = key.count('X')
    
    # Generate all possible combinations
    replacements = product(("0", "1"), repeat=num_xs)

    # List to store all possible addresses
    addresses = []

    # For each replacement sequence
    for i in replacements:
        temp_k = list(key)
        temp_count = 0

        # Generate new address
        for j in range(len(temp_k)):
            if temp_k[j] == "X":
                temp_k[j] = i[temp_count]
                temp_count += 1
        
        new_k = "".join(temp_k)
        addresses.append(new_k)

    return addresses


answer = initialization_program()
print(answer)