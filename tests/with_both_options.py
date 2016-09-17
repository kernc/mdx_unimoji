# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase

from markdown import markdown
from mdx_unimoji import UnimojiExtension


class Test(TestCase):
    def test_mdx_both_options(self):
        img_cake = '<img alt="cake" src="cake.png"/>'
        img_wink = '<img alt="wink" src="wink.png"/>'
        overrides = UnimojiExtension.EMOJI
        overrides.update({img_cake: ['<3'],
                          img_wink: ';-) ;] ;-]'.split()})
        text = 'This was a triumph. The :cake: is a lie. ;)'
        # should_be = '<p>This was a triumph. The <img alt="cake" class="other" src="cake.png"> is a lie. <img alt="wink" class="other" src="wink.png"/></p>'
        should_be = '<p>This was a triumph. The <span class="other" style="color:maroon">🍰</span> is a lie. <span class="other">😉</span></p>'
        result = markdown(text,
                          extensions=[UnimojiExtension(span_class='other',
                                                       emoji=overrides)])
        self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
