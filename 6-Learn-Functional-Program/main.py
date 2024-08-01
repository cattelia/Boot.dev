from functools import reduce

'''
def paginator(page_length):
    # IN: number
    # OUT: returned function
    
    def paginate(document):
        # IN: string `paginate("Boots loves salmon because he is a bear.")`
        # OUT: list of substring pages
        print(f"paginate() received the input: '{document}'")
        pages = document.split()

        def add_word_to_pages(pages, word):
            # IN: list of strings (pages), string (word)
            # OUT: list of string (pages) with (word) added

            if pages == []:
                return word.split()
            else:
                for item in word.split():
                    pages.append(item)
            
            #return " ".join(pages)
            return pages
        
        document = add_word_to_pages(pages, document)
        print(f"add_word_to_pages() returned: {document}")


    return paginate


paginate = paginator(5)
pages = paginate("Boots loves salmon because he is a bear.")
print(pages)
'''




from functools import reduce


def paginator(page_length):
    

    def paginate(document):
        # IN: document --> string
        # OUT: list of substring pages
        pages = document.split()

        def add_word_to_pages(pages, word):
            if pages == []:
                return word.split()
            else:
                return f"{pages} {word}"

        content = reduce(add_word_to_pages, pages)        
        return content
        
    return paginate




paginate = paginator(5)
print(paginate) # <function paginator.<locals>.paginate at 0x7f828dcc9ee0>
pages = paginate("Boots loves salmon.")
print(pages)
