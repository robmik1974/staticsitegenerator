"""..."""


class HTMLNode:
    """..."""

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """..."""
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        """..."""
        output_string = ""
        if self.props:
            for key, value in self.props.items():
                output_string += f' {key}="{value}"'
        return output_string

    def __repr__(self):
        return f"HTMLNode(\
            {self.tag},\
            {self.value},\
            {self.children}\
            {self.props}\
            )"


class LeafNode(HTMLNode):
    """..."""

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        """..."""
        if self.value is None:
            raise ValueError("value for leaf node is required")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """..."""

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """..."""
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        result = ""
        for leafnode in self.children:
            result += leafnode.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag},children: {self.children},{self.props})"
