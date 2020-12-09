def find_encryption_weakness():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        # Preamble list
        preamble = text_lst[:25]

        # Find Invalid Number and its index
        for i in range(25, len(text_lst)):
            # Invalid number
            if not sum_in_preamble(int(text_lst[i]), preamble):
                invalid_number = int(text_lst[i])
                index = i
                break
            else:
                # Adjust for new preamble
                preamble = gen_new_preamble(preamble, int(text_lst[i]))
        
        # List of previous numbers before invalid number
        prev_list = text_lst[:683]

        # Find contigous set which sums to invalid_number
        contigous_set = find_contigous_set(prev_list, invalid_number)

        # Return encryption weakness
        return max(contigous_set) + min(contigous_set)
        
def find_contigous_set(prev_list, target):
    # Start from 0
    for i in range(len(prev_list)-1):
        temp_sum = int(prev_list[i])
        temp_lst = [int(prev_list[i])]

        # Start from i+1
        for j in range(i+1, len(prev_list)):
            temp_sum += int(prev_list[j])
            temp_lst.append(int(prev_list[j]))
            
            # Return list that sums to target
            if temp_sum == target:
                return temp_lst
            
            # Break loop since temp_sum > target
            elif temp_sum > target:
                break

def sum_in_preamble(value, preamble):
    # Loop through preamble to see if sum of any pairs equals to target value
    for i, item in enumerate(preamble):
        for j in range(i+1, len(preamble)):
            total_of_two_items = int(preamble[i]) + int(preamble[j])
            if(total_of_two_items == value):
                return True
    return False

def gen_new_preamble(preamble, num):
    preamble.append(num)
    preamble.pop(0)
    return preamble

encryption_weakness = find_encryption_weakness()
print(encryption_weakness)
