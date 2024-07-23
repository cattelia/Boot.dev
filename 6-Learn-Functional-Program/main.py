def count_nested_levels(nested_documents, target_document_id, level=1):
    print(f"Currently evaluating {nested_documents}")
    found = False
    
    for doc in nested_documents:
        if doc == target_document_id:
            found = True
            print(f"Level: {level}")
        
        if found == False and nested_documents[doc] != {}:

            something = count_nested_levels(nested_documents[doc], target_document_id, level+1)


    if found == False:
        return -1
    return level


def count_nested_levels2(nested_documents, target_document_id, level=1):

    if target_document_id in nested_documents:
        print("Found")
        return level
    
    if nested_documents != {}:
        for entry in nested_documents:
            something = count_nested_levels(nested_documents[entry], target_document_id, level + 1)
            if something != None:
                return something
docx1 = {
    1: {
        2: {
            3: {}, 
            4: {
                5: {}
                }
            }, 
        6: {}, 
        7: {
            8: {
                9: {
                    10: {}
                    }
                }
            }
        }
}

thing = {
    1: {
        3: {}
    },
    2: {}
}


#count_nested_levels(thing, target_document_id=3, level=1)
level = count_nested_levels(docx1, target_document_id=6, level=1)
print(f"Result {level}")