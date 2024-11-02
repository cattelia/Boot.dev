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

    def __eq__(self, obj):
        
        if self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


t = TextNode("hello", "BOLD")
#print(t.text, t.text_type, t.url)
print(t) # Testing: __repr__()

s = TextNode("welcome", "italic", "http://www.google.com")
#print(s.text, s.text_type, s.url)
print(s) # Testing: __repr__()

u = TextNode("hello", "BOLD")

# Testing: __eq__(x, y)
print(t == s) # >> False
print(t == u) # >> True
print(s == u) # >> False






















'''
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class MyClass:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        print(f"My color is {self.color}")

my_object = MyClass(Color.RED.name)
my_object.get_color()
'''


'''
Yes, you can get the value of an Enum member in Python by providing its name.
Here's how:


from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Get the value of an enum member by its name
color_value = Color['RED'].value

print(color_value)  # Output: 1
'''