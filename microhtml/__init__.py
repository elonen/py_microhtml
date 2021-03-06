#!/usr/bin/env python3

"""
py_microhtml – Minimalistic HTML generator for Python 3.6+ with compact syntax

Copyright 2019 Jarno Elonen.
Released under the MIT license. See LICENSE for details.
"""
from functools import partial
from tidylib import tidy_document
import sys, html

class _TagWrapper:
    def __init__(self, tag_name: str, *args, **kwargs):
        self.tag_name = tag_name
        self.children = [] # type: list

        self.tag_attribs = ''
        for k, v in kwargs.items():
            attrname = (k[:-1] if k.endswith('_') else k).replace('__', '-')
            self.tag_attribs += f' {attrname}="{html.escape(str(v))}"'

    def __call__(self, *content_args) -> '_TagWrapper':
        for c in content_args:
            self.children.append(c if callable(c) else html.escape(str(c)))
        return self

    def __str__(self):
        return self.render()

    def render(self) -> str:
        '''Generate HTML but don't indent/tidy it'''
        return f'<{self.tag_name}{self.tag_attribs}>' + \
               ''.join([str(x) for x in self.children]) + \
               f'</{self.tag_name}>'

    def pretty(self, tidy_warnings=False) -> str:
        '''Like render() but format through tidylib'''
        txt, errors = tidy_document(self.render(), {
            'indent':1, 'output-xhtml': True, 'force-output': 1, 'doctype': 'strict', 'show-warnings': tidy_warnings})
        if errors:
            print('HTML tidy: ' + str(errors), file=sys.stderr)
        return txt

class _Raw_Wrapper:
    def __init__(self, text: str):
        self.text = text
    def __str__(self):
        return self.text
    def __call__(self):
        pass

def ᑉtag( tag_name: str, *args, **kwargs) -> _TagWrapper:
    '''User function to add a tag by giving it's name as parameter.'''
    cw = _TagWrapper(tag_name, *args, **kwargs)
    for x in args:
        cw(x)
    return cw

def ᑉrawstr(text: str) -> _Raw_Wrapper:
    return _Raw_Wrapper(text)


_ALL_TAGS = 'a abbr address area article aside audio b base bdi bdo blockquote body br button canvas caption ' \
    'cite code col colgroup command datalist dd del details dfn div dl dt em embed fieldset figcaption '\
    'figure footer form h1 h2 h3 h4 h5 h6 head header hgroup hr html i iframe img input ins kbd keygen '\
    'label legend li link map mark menu meta meter nav noscript object ol optgroup option output p param '\
    'pre progress q rp rt ruby s samp script section select small source span strong style sub summary sup '\
    'table tbody td textarea tfoot th thead time title tr track u ul var video wbr '.split()

# Add all HTML tags as convenience functions (such as ᑉdiv())
for tagname in _ALL_TAGS:
        setattr(__import__(__name__), 'ᑉ'+tagname, partial(ᑉtag, tagname))

# Print stubs for type checkers (.pyi file)
if __name__ == "__main__":
    for x in _ALL_TAGS:
        print('def ᑉ{}(*args: Any, **kwargs: Any) -> _TagWrapper: ...'.format(x))
