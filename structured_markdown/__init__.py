from .engine import *

def html(inp, name=None):
    """
    inp: SMD string to parse
    name: name of root div, if set to none, no root div will be returned
    returns: parsed html string
    """
    smd_instance = StructuredMarkdown(inp)
    return smd_instance.html(lines=None, name=name)

def css(inp):
    """
    inp: SMD string to parse
    returns: parsed css string
    """
    smd_instance = StructuredMarkdown(inp)
    return smd_instance.html(lines=None, selector=None)

def parse(inp, name=None):
    """
    inp: SMD string to parse
    name: name of root div, if set to none, no root div will be returned
    returns: tuple of parsed html string, parsed css string
    """
    # get kwargs for templating, maybe...
    # template name has to be a StructuredMarkdown object
    # and {{ name }} has to be a string, int, float, bool, etc.
    smd_instance = StructuredMarkdown(inp)
    return (
        smd_instance.html(lines=None, name=name),
        smd_instance.css(lines=None, selector=None),
    )

def parse_from_file(file_name, name=None):
    with open(file_name, "r") as fin:
        inp = file.read()
    return parse(inp, name=Name)

def parse_inline_style(file_name, name=None):
    pass
    "puts everything into one html document with a head, doctype, body, etc"
