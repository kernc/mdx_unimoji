# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase

from markdown import markdown
from mdx_unimoji import UnimojiExtension


class Test(TestCase):
    def test_mdx_overrides_emoji_option(self):
        img_cake = '<img alt="cake" src="cake.png"/>'
        img_wink = '<img alt="wink" src="wink.png"/>'
        overrides = UnimojiExtension.EMOJI
        overrides.update({
            img_cake: [':cake:'],
            img_wink: ';) ;-) ;] ;-]'.split(),

        })
        text = 'This was a triumph. The :cake: is a lie. ;)'
        should_be = '<p>This was a triumph. The <img alt="cake" class="emoji" src="cake.png" /> is a lie. <img alt="wink" class="emoji" src="wink.png" /></p>'
        result = markdown(text, extensions=[UnimojiExtension(emoji=overrides)])
        self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
