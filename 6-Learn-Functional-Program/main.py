def remove_invalid_lines(document):
    '''print(len(document))
    document = document.split("\n")
    print(len(document))
    document = "\n".join(document)
    print(len(document))'''

    return "\n".join(filter(lambda line: line.startswith("*"), document.split("\n"))) + "\n"
