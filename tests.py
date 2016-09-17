# coding: utf-8
from __future__ import unicode_literals

from unittest import main, TestCase
from markdown import markdown
from mdx_unimoji import UnimojiExtension


class Test(TestCase):
    def test_markdown_without_emoji_extension(self):
        text = 'I <3 you! Just kidding. :P'
        should_be = '<p>I &lt;3 you! Just kidding. :P</p>'
        result = markdown(text, extensions=[])
        self.assertEqual(should_be, result)

    def test_without_emojis(self):
        text = 'I love you! Just kidding. *smile*'
        should_be = '<p>I love you! Just kidding. <em>smile</em></p>'
        result = markdown(text, extensions=[])
        self.assertEqual(should_be, result)

    def test_with_emojis(self):
        text = 'I <3 you! Just kidding. :P'
        # should_be = '<p>I <span class="emoji" style="color:red">❤</span> you! Just kidding. <span class="emoji">😛</span></p>'
        should_be = '<p>I ❤ you! Just kidding. 😛</p>'
        result = markdown(text, extensions=['mdx_unimoji'])
        self.assertEqual(should_be, result)

    def test_mdx_overrides_emoji_option(self):
        img_heart = '<img alt="love" src="heart.png"/>'
        img_tongue = '<img alt=":P" src="tongue.png"/>'
        overrides = UnimojiExtension.EMOJI
        overrides.update({
            img_heart: ['<3'],
            img_tongue: ':p :P :-p :-P'.split(),
        })
        text = 'I <3 you! Just kidding. :P'
        should_be = '<p>I <img alt="love" class="emoji" src="heart.png" /> you! Just kidding. <img alt=":P" class="emoji" src="tongue.png" /></p>'
        result = markdown(text, extensions=[UnimojiExtension(emoji=overrides)])
        self.assertEqual(should_be, result)

    def test_mdx_overrides_emoji_option(self):
        overrides = UnimojiExtension.STYLES
        overrides.update({
            '❤': 'color:blue',
        })
        text = 'I <3 you! Just kidding. :P'
        should_be = '<p>I <span class="emoji" style="color:blue">❤</span> you! Just kidding. <span class="emoji">😛</span></p>'
        result = markdown(text, extensions=[UnimojiExtension(styles=overrides)])
        self.assertEqual(should_be, result)

    def test_mdx_span_class_option(self):
        text = 'I <3 you! Just kidding. :P'
        should_be = '<p>I <span class="other" style="color:red">❤</span> you! Just kidding. <span class="other">😛</span></p>'
        result = markdown(text, extensions=[UnimojiExtension(span_class='other')])
        self.assertEqual(should_be, result)

    def test_mdx_span_class_none_option(self):

        text = 'I <3 you! Just kidding. :P'
        should_be = '<p>I ❤ you! Just kidding. 😛</p>'
        result = markdown(text, extensions=[UnimojiExtension(span_class=None)])
        self.assertEqual(should_be, result)

    # def test_mdx_both_options(self):
    #     img_heart = '<img alt="love" src="heart.png"/>'
    #     img_tongue = '<img alt=":P" src="tongue.png"/>'
    #     overrides = UnimojiExtension.EMOJI
    #     overrides.update({img_heart: ['<3'],
    #                       img_tongue: ':p :P :-p :-P'.split()})
    #     text = 'I <3 you! Just kidding. :P'
    #     should_be = '<p>I <img alt="love" class="other" src="heart.png" /> you! Just kidding. <span class="other">😛</span></p>'
    #     result = markdown(text,
    #                       extensions=[UnimojiExtension(span_class='other',
    #                                                    emoji=overrides)])
    #     self.assertEqual(should_be, result)

if __name__ == '__main__':
    main()
