a_list = ['1', '4', '55', '65', '4', '15', '90']
int_list = [int(c) for c in a_list]
print("int_list:", int_list)

int_list_2d = [int(c) for c in a_list if len(c) > 1]
print("int_list_2d:", int_list_2d)
