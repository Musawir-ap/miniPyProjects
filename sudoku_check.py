import copy

lines_box = []
print('enter lines.....')
while True:
    g_lines = [input()]
    if not any(g_lines):  # If any line in the group is empty, exit the loop
        break
    lines_box.extend(g_lines)

# group_lines = ['295743861', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '154938672']
box = [[int(char) for char in row] for row in lines_box]

def check(box):
    # check each line
    s_box = [[row[i:i+3] for i in range(0, 9, 3)] for row in box]
    s_box = [s_box[i:i+3] for i in range(0, 9, 3)]
    
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    _box = copy.deepcopy(box)
    for i in _box:
        i.sort()
        if i != r:
            row_flag = False
            break
        row_flag = True
        # print('row Ok')

    #check each cols
    _box = copy.deepcopy(box)
    for i in range(len(box)):
        cols = []
        for _ in _box:
            cols.append(_[i])
        cols.sort()
        # print(cols)
        if cols != r:
            col_flag = False
            break
        col_flag = True
        # print('col Ok')
    
    # check for each 3x3 box
    for i in range(0, len(_box), 3):
        b = _box[i:i+3]
        _c = 0
        temp = []

        
        for k in range(0, 9, 3):    
            for j in b:
                temp.append(j[k:k+3])

            flat_list = [ _ for sublist in temp for _ in sublist]
            flat_list.sort()
            if flat_list != r:
                box_flag = False
                break
            box_flag = True
            # print('box Ok')
            temp.clear()
            
    if row_flag and col_flag and box_flag:
        print('sudoku is Valid')
    else:
        print('invalid')
            
        
check(box)