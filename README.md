# Minimalistic HTML generator for Python 3.6+ with compact syntax
[![Build Status](https://travis-ci.com/elonen/py_microhtml.svg?branch=master)](https://travis-ci.com/elonen/py_microhtml)

Safely construct valid HTML with Python code. Example:

```python
from microhtml import *
print(
  ᑉhtml(
    ᑉhead( ᑉtitle( 'Test page' )),
    ᑉbody( ᑉspan( 'Simple example.', class_='example' ))).pretty())
```

This prints out a valid, formatted XHTML document:
```xml
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
 <head>
   <title>
     Test page
   </title>
 </head>
 <body>
   <span class="example">One line example!</span>
 </body>
</html>
```

Yes, you'll probably need to copy-paste the unicode symbol and yes, you'll want to use a modern editor, but the resulting syntax is very compact and will not collide with your identifiers even with the `import *`.

Minimalism also extends to implementation – it's _very_ short (70 lines in v0.1). Check out `microhtml.py`.

Longer example with more features showcased:

```python
from microhtml import *

# Rendering a non-indented string (result: <p>Third <em>and last</em> paragraph</p>)
raw_html = str(ᑉp("Third ", ᑉem("and last"), ' paragraph'))

# Writing a nicely formatted / tidied XHTML document to a file descriptor
print(
  ᑉhtml( lang='en_US' )(
    ᑉhead(ᑉtitle("Test page")),
    ᑉbody(
        ᑉp("Hi!", width=123), # 123 becomes "123"
        ᑉhr(class_='someclass'), # Reserved words like "class" can be written with a trailing underscore
        ᑉp('Literal strings are safely <em>escaped</em> by default.'),
        ᑉrawstr(raw_html), # Use ᑉrawstr() if you don't want escaping
        ᑉtag('applet', code='Bubbles.class', width=350, height=350),  # Tag with custom name
        ᑉdiv(style='float: right')(  # This is how you can type attributes on left and content on right
            ᑉdiv(style='border: 1px solid black')(
                ᑉa("Nested", href='#anchortest'), '|', 'link')))).pretty())
```

This outputs:

```xml
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en_US">
  <head>
    <title>
      Test page
    </title>
  </head>
  <body>
    <p width="123">
      Hi!
    </p>
    <hr class="someclass">
    <p>
      Literal strings are safely &lt;em&gt;escaped&lt;/em&gt; by default.
    </p>
    <p>
      Third <em>and last</em> paragraph
    </p><applet code="Bubbles.class" width="350" height="350">
      </applet>
    <div style="float: right">
      <div style="border: 1px solid black">
        <a href="#anchortest">Nested</a>|link
      </div>
    </div>
  </body>
</html>
```

If you find unicode characters in source code a horrendous abomination, and don't mind endless nested `with` expressions, you might prefer [Yattag](http://www.yattag.org/).

Uses `tidylib` for pretty printing. Inspiration drawn from `pyhtml` by Cenk Altı.

Copyright 2019 Jarno Elonen.
Released under the MIT license. See LICENSE for details.
