# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase

from markdown import markdown
from mdx_unimoji import UnimojiExtension


class Test(TestCase):
    def test_mdx_overrides_emoji_option(self):
        overrides = UnimojiExtension.STYLES
        overrides.update({
            '🍰': 'color:blue',
        })
        text = 'This was a triumph. The :cake: is a lie. ;)'
        should_be = '<p>This was a triumph. The <span class="emoji" style="color:blue">🍰</span> is a lie. <span class="emoji">😉</span></p>'
        result = markdown(text, extensions=[UnimojiExtension(styles=overrides)])
        self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
