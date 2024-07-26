def doc_format_checker_and_converter(conversion_function, valid_formats):

    def doc_checker(filename, content):
        check_filename = filename.split(".")
        if check_filename[1] in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("Invalid file format")
    
    return doc_checker
        


# Don't edit below this line

def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]