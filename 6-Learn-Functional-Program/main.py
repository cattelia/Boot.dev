def file_type_getter(file_extension_tuples):
    file_type_dictionary = {}

    # Get individual tuples from the list of tuples
    for file_tuple in file_extension_tuples:
        # Get the file types and their file names
        for file in file_tuple[1]:
            # And then add them to a dictionary
            file_type_dictionary[file] = file_tuple[0]

    print(file_type_dictionary)

    return lambda ext: file_type_dictionary.get(ext, "Unknown")



#file_extension_tuples = [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])]
#print(file_type_getter(file_extension_tuples))