def map_traverse_trees():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        tree_map = [list(i) for i in text_lst]
        
        num_cols = len(tree_map[0])
        num_rows = len(tree_map)

        trees_arr = [0] * 5
        slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

        for j in range(len(slopes)):
            pos = [0,0]
            for i in range(num_rows-1):
                pos[0] += slopes[j][0]
                pos[1] = (pos[1] + slopes[j][1])% num_cols
                if pos[0] < num_rows and tree_map[pos[0]][pos[1]] == "#":
                    trees_arr[j] += 1
        
        return trees_arr
            
trees_array = map_traverse_trees()

product = 1
for i in trees_array:
    product *= i

print(product)