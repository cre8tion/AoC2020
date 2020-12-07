def get_total_bags_in_shiny_gold():
    with open('input.txt') as fin:
        input_list = fin.readlines()

        # Messy Cleaning of Data
        text_lst = [i.replace("\n", "") for i in input_list]
        bags_lst = [i.split("bag") for i in text_lst]
        bags_lst = [[j.replace(",", "") for j in i] for i in bags_lst]
        bags_lst = [[j for j in i if j != "."] for i in bags_lst]
        
        bag_dict = {}

        for bag in bags_lst:
            for i in range(len(bag)):
                if i == 0:
                    key = bag[0].strip()
                    bag_dict[key] = []
                else:
                    temp_lst = bag[i].split(" ")
                    if len(temp_lst) > 1:
                        individual_bag = temp_lst[-3:-1]
                        individual_bag = " ".join(individual_bag)

                        # key: [tuples of (bag color, bag count)]
                        if "no" in temp_lst:
                            bag_dict[key].append((individual_bag,0))
                        else:
                            num_bags = int(temp_lst[-4:-3][0])
                            bag_dict[key].append((individual_bag, num_bags))
        
        total_bags = 0

        # Summing up all bags contained in shiny gold bag
        for i in bag_dict["shiny gold"]:
            total_bags += get_bags(bag_dict, i[0], i[1])

        return total_bags

# Recursion
def get_bags(dic, key, count):
    current_bag_list = dic[key]
    current_bags = count

    for i in current_bag_list:
        if i[1] == 0:
            return count
        else:
            current_bags += get_bags(dic, i[0], count * i[1])
    
    return current_bags


total_bags = get_total_bags_in_shiny_gold()
print(total_bags)