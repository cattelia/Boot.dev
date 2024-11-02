from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:

    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        
        # TEXT_TYPE is key to TextType.NAME.VALUE but NAME is a func in TextType class
        #   Need to treat like dictionary. Class[Key].value
        self.text_type = TextType[TEXT_TYPE.upper()].value

        if URL == None:
            self.url = URL
        elif URL != None and URL[0:8] == "https://" or URL[0:7] == "http://":
            self.url = URL
        else:
            self.url = None

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def __eq__(self, obj):
        
        if self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url:
            return True
        else:
            return False
        
