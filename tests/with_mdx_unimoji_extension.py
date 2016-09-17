# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase

from markdown import markdown
from mdx_unimoji import UnimojiExtension


class Test(TestCase):
    def test_without_emojis(self):
        text = 'This was a triumph. The *cake* is a lie.'
        should_be = '<p>This was a triumph. The <em>cake</em> is a lie.</p>'
        result = markdown(text, extensions=[])
        self.assertEqual(should_be, result)

    def test_with_emojis(self):
        text = 'This was a triumph. The :cake: is a lie. ;)'
        should_be = '<p>This was a triumph. The <span class="emoji" style="color:maroon">🍰</span> is a lie. <span class="emoji">😉</span></p>'
        result = markdown(text, extensions=[UnimojiExtension()])
        self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
