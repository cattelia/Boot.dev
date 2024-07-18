def zipmap(keys, values):
    # If either the keys or values list is empty
    if len(keys) == 0 or len(values) == 0:
        return {}

    return zipmap(keys[0], values[0])