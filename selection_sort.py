items = ["C", "D", "B", "E", "A"]

def sorter(list):
    for swap_pass in range(1, len(list)):
        for pos in range(0, len(list) - 1):
            if list[pos] > list[pos + 1]:
                temp = list[pos + 1]
                list[pos + 1] = list[pos]
                list[pos] = temp
    return list



print(sorter(items))
