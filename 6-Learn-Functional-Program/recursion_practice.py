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

def count_nested_levels(nested_documents, target_document_id, level=1):

    
    for doc in nested_documents:
        if doc == target_document_id:
            return level
        else:
            found = count_nested_levels(nested_documents[doc], target_document_id, level + 1)
        
        if found != -1:
            return found
    
    return -1

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

levee = count_nested_levels(docx1, target_document_id=9, level=1)
print(levee)

def count_nested_levels(nested_documents, target_document_id, level=1):

    if target_document_id in nested_documents:
        print("Found")
        return level
    
    if nested_documents != {}:
        for entry in nested_documents:
            something = count_nested_levels(nested_documents[entry], target_document_id, level + 1)
            if something != None:
                return something