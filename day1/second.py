def triples():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [int(i.replace("\n", "")) for i in input_list]
        
        return find3Numbers(text_lst, len(text_lst), 2020)


def find3Numbers(A, arr_size, sum): 
    for i in range(0, arr_size-1): 
        s = set()
        curr_sum = sum - A[i] 
        for j in range(i + 1, arr_size): 
            if (curr_sum - A[j]) in s:
                return [A[i], A[j], curr_sum-A[j]]
            s.add(A[j])

triple = triples()
result = triple[0] * triple[1] * triple[2]
print(result)