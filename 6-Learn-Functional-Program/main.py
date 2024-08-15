def new_clipboard(initial_clipboard):
    # ?

    copy_clippy = initial_clipboard.copy()

    def copy_to_clipboard(key, value):
        copy_clippy[key] = value

    def paste_from_clipboard(key):
        if key not in copy_clippy:
            return ""
        else:
            return copy_clippy[key]

    return copy_to_clipboard, paste_from_clipboard

'''intitial_clipboard = {'a': 1, 'b': 2, 'c': 3}
copy_to_clipboard, paste_from_clipboard = new_clipboard(intitial_clipboard)
copy_to_clipboard('d', 4)
print(paste_from_clipboard('e'))
print(paste_from_clipboard('d'))
'''