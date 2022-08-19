# 7 задание:
from genericpath import isdir
import os.path

def search(inp_list, first_max_num,idx = None):

    second_max_num = first_max_num
    if idx is None:
        idx = 0

    if inp_list[idx] >= first_max_num:
        first_max_num = inp_list[idx]

    if idx == len(inp_list) - 1:
        return second_max_num

    return search(inp_list,first_max_num,idx + 1)

def find_max_num(inp_list):

    idx = 0
    second_max_num = search(inp_list,inp_list[idx])

    return second_max_num

print(find_max_num([1,2,3,4,5,6,7,8,9]))

# 8 задание:
def show_dir_and_files(way_name):
    print(os.listdir(way_name))
    for i in (os.listdir(way_name)):
        if os.path.isdir(i):
            print(i)
            show_dir_and_files(i)
#print(show_dir_and_files("D:\worktable\new_life 2.0\study\programing\python\practic\recursion\task3-4"))