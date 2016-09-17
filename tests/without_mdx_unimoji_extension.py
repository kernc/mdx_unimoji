# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase

from markdown import markdown


class Test(TestCase):
    def test_markdown_without_emoji_extension(self):
        text = 'This was a triumph. The :cake: is a lie. ;)'
        should_be = '<p>This was a triumph. The :cake: is a lie. ;)</p>'
        result = markdown(text, extensions=[])
        self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
