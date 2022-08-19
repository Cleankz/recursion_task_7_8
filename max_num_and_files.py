# 7 задание:
from genericpath import isdir
import os.path

# def search(inp_list, first_max_num,idx):
#     second_max_num = first_max_num

#     if inp_list[idx] >= first_max_num:
#         first_max_num = inp_list[idx]

#     if idx == len(inp_list) - 1:
#         return second_max_num

#     return search(inp_list,first_max_num,idx + 1)

def find_max_num(inp_list):
    first_max_num = inp_list[0]
    second_max_num = 0
    more_first_max = False
    count_f_max_num = 0

    for i in inp_list:
        if i >= first_max_num:
            first_max_num = i
            count_f_max_num = count_f_max_num + 1
        if i == first_max_num and count_f_max_num > 1:
            more_first_max = True
    for j in inp_list:
            if j > second_max_num and j != first_max_num:
                second_max_num = j
            if more_first_max:
                second_max_num = first_max_num


    return second_max_num


# 8 задание:
def show_dir_and_files(way_name):
    print(os.listdir(way_name))
    for i in (os.listdir(way_name)):
        if os.path.isdir(i):
            print(i)
            show_dir_and_files(i)
#print(show_dir_and_files("D:\worktable\new_life 2.0\study\programing\python\practic\recursion\task3-4"))