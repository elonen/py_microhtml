from unittest import TestCase
import io
from microhtml import *

def long_example():
    # Rendering a non-indented string (result: <p>Third <em>and last</em> paragraph</p>)
    raw_html = str(ᑉp("Third ", ᑉem("and last"), ' paragraph'))

    # Writing a nicely formatted / tidied XHTML document
    return ᑉhtml( lang='en_US' )(
        ᑉhead(ᑉtitle("Test page")),
        ᑉbody(
            ᑉp("Hi!", width=123), # 123 becomes "123"
            ᑉhr(class_='someclass'), # Reserved words like "class" can be written with a trailing underscore
            ᑉp('Literal strings are safely <em>escaped</em> by default.'),
            ᑉrawstr(raw_html), # Use ᑉrawstr() if you don't want escaping
            ᑉtag('applet', code='Bubbles.class', width=350, height=350),  # Tag with custom name
            ᑉdiv(style='float: right')(  # This is how you can type attributes on left and content on right
                ᑉdiv(style='border: 1px solid black')(
                    ᑉa("Nested", href='#anchortest'), '|', 'link')))).pretty()

correct_result = '''
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
</html>'''

class TestLongExample(TestCase):
    def test_correct_result(self):
      self.assertEquals(long_example().strip(), correct_result.strip())

if __name__== "__main__":
    print(long_example())
