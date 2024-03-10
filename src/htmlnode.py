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
