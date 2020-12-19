def shuttle_search():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        ids = text_lst[1].replace(",","")
        bus_lst = ids.split("x")
        bus_lst = [int(i) for i in bus_lst if i != ""]
        
        timestamp = int(text_lst[0])
        timestamp_lst = []

        # Finding the first arrival of each bus after timestamp specified in first row
        for i in bus_lst:
            quotient = timestamp // i
            next_quotient = quotient + 1
            timestamp_lst.append(next_quotient * i)
        
        # Finding the closest time arrival
        earliest_time = min(timestamp_lst)

        # Finding the exact bus id that matches the closest time arrival
        for i in bus_lst:
            if earliest_time % i == 0:
                bus_id = i
                break
        
        answer = (earliest_time - timestamp) * bus_id
        return answer

answer = shuttle_search()
print(answer)