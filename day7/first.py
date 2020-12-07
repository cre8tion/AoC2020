def get_bag_colors():
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
                        bag_dict[key].append(individual_bag)
                    
        total_colors = 0

        # Checking whether shiny gold bag in within each unique bag
        for key in bag_dict.keys():
            if contains_shiny_gold(bag_dict, key):
                total_colors += 1
        
        return total_colors

# Recursion
def contains_shiny_gold(dic, key):
    have_shiny_gold = False
    if key != "no other" and "shiny gold" in dic[key]:
        return True
    else:
        for i in dic[key]:
            if i != "no other" and contains_shiny_gold(dic, i):
                have_shiny_gold = True
                break
    return have_shiny_gold


total_colors = get_bag_colors()
print(total_colors)