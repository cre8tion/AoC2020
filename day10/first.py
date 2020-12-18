def get_jolt_diff_dict():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        adapter_lst = [int(i) for i in input_list]
        adapter_lst.sort()
        
        # Dictionary to hold values; Inclusive of first case 0 -> 1, with 1 diff
        jolt_dict = {1 : 1, 2 : 0, 3 : 0}

        # Loop through all adapters
        for i in range(len(adapter_lst) - 1):
            diff = adapter_lst[i+1] - adapter_lst[i]
            jolt_dict[diff] = jolt_dict[diff] + 1
        
        # Last case which your device adapter is always 3 higher than highest adapter
        jolt_dict[3] = jolt_dict[3] + 1

        return jolt_dict
            
jolt_diff_dict = get_jolt_diff_dict()
ans = jolt_diff_dict[1] * jolt_diff_dict[3]
print(ans)
