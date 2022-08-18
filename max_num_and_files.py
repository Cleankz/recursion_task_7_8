# 7 задание:
from genericpath import isdir
import os.path
def search(inp_list, first_max_num,second_max_num,idx = 0):

    if first_max_num <= inp_list[idx]:
        second_max_num = first_max_num
        first_max_num = inp_list[idx]

    if idx == len(inp_list) - 1:
        return second_max_num
    return search(inp_list,first_max_num,second_max_num,idx + 1)
def find_max_num(inp_list):
    second_max_num = search(inp_list,0,0)
    return second_max_num

# 8 задание:
def show_dir_and_files(way_name):
    print(os.listdir(way_name))
    for i in (os.listdir(way_name)):
        if os.path.isdir(i):
            print(i)
            show_dir_and_files(i)
print(show_dir_and_files("D:\worktable\new_life 2.0\study\programing\python\practic\recursion\task3-4"))