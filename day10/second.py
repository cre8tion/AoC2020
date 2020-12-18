# This is where it starts being hard
# I actually had to refer to this: https://www.reddit.com/r/adventofcode/comments/ka9pc3/2020_day_10_part_2_suspicious_factorisation/
#
# If you have a chain of consecutive adapters (e.g. 14, 15, 16, 17), you can use the length of the chain to figure out the multiplier. 
# In the case of [14, 15, 16, 17], you multiply by 4.
# The multiplier is the Tribonacci sequence:
# [n, n+1] => multiply by 1
# [n, ..., n+2] => multiply by 2
# [n, ..., n+3] => multiply by 4
# [n, ..., n+4] => multiply by 7
# [n, ..., n+5] => multiply by 13
# etc...
# 
# *Only works with the pre-condition that the gaps are only of size 1 and 3, which is the case for this input*
# 
# The most obvious way to solve this is via DP
# However, I will try that another day...
# 

def get_distinct_arrangement():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        adapter_lst = [int(i) for i in input_list]
        adapter_lst.sort()

        adapter_lst.insert(0, 0)
        adapter_lst.append(adapter_lst[len(adapter_lst)-1] + 3)

        # Entire chain list
        chain_lst = []
        # Temporary chain list
        temp_lst = []

        # Generating chains of consecutive adapters
        for i in range(len(adapter_lst)-1):
            # Initialising the temp_lst
            if len(temp_lst) == 0:
                temp_lst.append(adapter_lst[i])
            
            # Last item in sorted_adapter_lst
            if i == len(adapter_lst) - 2:
                # Within the chain
                if adapter_lst[i+1] - adapter_lst[i] == 1:
                    temp_lst.append(adapter_lst[i+1])
                
                # Put the temp_lst into chain_lst
                if len(temp_lst) > 1:
                    chain_lst.append(temp_lst)
                    temp_lst = []
            
            # Within the chain
            elif adapter_lst[i+1] - adapter_lst[i] == 1:
                temp_lst.append(adapter_lst[i+1])
            
            # Outside the chain
            elif adapter_lst[i+1] - adapter_lst[i] == 3:
                # Need a new temp_lst
                if len(temp_lst) == 1:
                    temp_lst = []

                # Put the temp_lst into chain_lst
                else:
                    chain_lst.append(temp_lst)
                    temp_lst = []
        
        # Initialise distinct_arrangement count
        dist_arrangement = 1

        # Multiplier
        for i in chain_lst:
            if len(i) == 2:
                dist_arrangement *= 1
            elif len(i) == 3:
                dist_arrangement *= 2
            elif len(i) == 4:
                dist_arrangement *= 4
            elif len(i) == 5:
                dist_arrangement *= 7
            elif len(i) == 6:
                dist_arrangement *= 13
        
        return dist_arrangement

distinct_arrangement = get_distinct_arrangement()
print(distinct_arrangement)
