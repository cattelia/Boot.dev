class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        # str -> html element: "p", "a", "h1"
        self.tag = tag
        # str -> html element value: text inside "p", link inside "a", text inside "h1"
        self.value = value
        # list -> HTMLNode objects representing the child of this node
        self.children = children
        # dict  -> key-value pair representing attributes of HTML. I.E. {"href" : "https://www.google.com"}
        self.props = props



    def to_html(self):
        raise NotImplementedError
    
    def get_props(self):
        return self.props


    def props_to_html(self):
        props_str = ""
        for key, value in self.props.items():
            print(key, value)


props = {
    "href": "https://www.google.com", 
    "target": "_blank",
}
h = HTMLNode(None,None,None, props)

print(type(h.get_props()))
h.props_to_html()