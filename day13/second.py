# Most mentioned Chinese Remainder Theorem
# But I did it in a more brute-force manner which makes use of the fact the pattern repeats every LCM.

def shuttle_search():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        bus_lst = text_lst[1].split(",")
        
        bus_id_index_lst = []
        # List to hold indexes of valid bus ids
        for i in range(len(bus_lst)):
            if bus_lst[i] != "x":
                bus_id_index_lst.append(i)

        # First and Second Bus Ids
        first = int(bus_lst[bus_id_index_lst[0]])
        second = int(bus_lst[bus_id_index_lst[1]])
        timestamp_diff = bus_id_index_lst[1] - bus_id_index_lst[0]

        # Finding the first timing valid for first and second buses.
        first_timing = find_first_timing_of_two_buses(13, timestamp_diff, first, second)
        timing = first_timing

        # Given all bus ids in the input are all prime numbers, LCM is product of two bus ids
        lcm = first * second

        # Finding timing that matches bus in the correct sequence with LCM and next bus_id
        for idx in range(2, len(bus_id_index_lst)):
            bus_id = int(bus_lst[bus_id_index_lst[idx]])
            timing = find_next_timing_with_lcm(lcm, timing, bus_id, bus_id_index_lst[idx])
            lcm = lcm * bus_id
        
        return timing
        
        
def find_next_timing_with_lcm(lcm, start_timing, next_bus_id, timestamp_diff):
    while (start_timing + timestamp_diff) % next_bus_id != 0:
        start_timing = start_timing + lcm
    return start_timing

def find_first_timing_of_two_buses(start_timing, difference, first_id, second_id):
        while (start_timing + difference) % second_id != 0 or start_timing % first_id != 0:
            start_timing += 1
        return start_timing

answer = shuttle_search()
print(answer)