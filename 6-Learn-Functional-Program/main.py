def sum_nested_list(lst):
    dir_size = 0
    for file in lst:
        if type(file) == int:
            dir_size += file
            #print("I am a number")
        if type(file) == list:
            #print("I am a list")
            dir_size += sum_nested_list(file)


    return dir_size