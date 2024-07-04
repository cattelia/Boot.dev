full = {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504, 'e': 46043, 'c': 9243, 't': 30365, ' ': 74144, 'g': 5974, 'u': 10407, 'n': 24367, 'b': 5026, "'": 229, 's': 21155, 'f': 8731, 'a': 26743, 'k': 1755, 'i': 24613, ',': 5097, 'y': 7914, 'm': 10604, 'w': 7638, 'l': 12739, '(': 39, 'd': 16863, ')': 39, 'h': 19725, '\n': 7652, 'v': 3833, '.': 3124, '-': 445, ':': 68, '1': 92, '7': 23, '2': 24, '0': 21, '8': 20, '[': 4, '#': 1, '4': 17, ']': 4, '*': 28, 'z': 243, '?': 220, ';': 970, 'x': 677, 'q': 324, '!': 239, '"': 796, '3': 18, '5': 16, '9': 13, '6': 10, '_': 2, '/': 24, '%': 1, '@': 2, '$': 2}
d = {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504}

def main():
    dictionary = convert_dict(d)
    #print(type(dictionary)) # <class 'list'>
    #print(f"First dictionary: {dictionary}") # [{'alpha': 'p', 'num': 6121}, {'alpha': 'r', 'num': 20818}, {'alpha': 'o', 'num': 25225}, {'alpha': 'j', 'num': 504}]
    dictionary.sort(reverse=True, key=sort_on)
    #print(f"Second dictionary: {dictionary}")

def convert_dict(dict):
    new_dict = []
    for key, values in dict.items():
        temp = {"alpha": key, "num": values}
        #print(temp)
        new_dict.append(temp)
    return new_dict

def sort_on(dict):
    return dict["num"]

main()


sort_d = dict(sorted(d.items(), key=lambda item: item[1]))
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
#print(sort_d)

sort_full = dict(sorted(full.items(), key=lambda item: item[1], reverse=True))
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
for i in sort_full:
    if i.isalpha():
        print(i, sort_full[i])



