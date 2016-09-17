# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase

from markdown import markdown
from mdx_unimoji import UnimojiExtension


class Test(TestCase):
    def test_mdx_span_class_option(self):
        text = 'This was a triumph. The :cake: is a lie. ;)'
        should_be = '<p>This was a triumph. The <span class="other" style="color:maroon">🍰</span> is a lie. <span class="other">😉</span></p>'
        result = markdown(text, extensions=[UnimojiExtension(span_class='other')])
        self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
