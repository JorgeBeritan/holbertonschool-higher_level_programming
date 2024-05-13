def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list) - 1 :
        return None
    else:
        return my_list[idx]
my_list = [1, 2, 3, 4, 5]
print(element_at(my_list, 5))