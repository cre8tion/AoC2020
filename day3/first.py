def map_traverse_trees():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        tree_map = [list(i) for i in text_lst]
        
        num_cols = len(tree_map[0])
        num_rows = len(tree_map)

        trees = 0
        pos = [0,0]

        for i in range(num_rows-1):
            pos[0] += 1
            pos[1] = (pos[1] + 3)% num_cols
            if tree_map[pos[0]][pos[1]] == "#":
                trees += 1
        
        return trees
            
trees = map_traverse_trees()
print(trees)