Unicode Emojis for Python-Markdown
==================================

Converts defined emoticon symbols to Unicode emojis, supported on a
variety of devices [1].

[1]: http://apps.timwhitlock.info/emoji/tables/unicode#block-1-emoticons

Usage:

```python
>>> from __future__ import print_function
>>> from markdown import markdown
>>> text = 'I <3 you! :P'
>>> print(markdown(text, ['mdx_unimoji']))    # doctest: +NORMALIZE_WHITESPACE
<p>I <span class="emoji" style="color:red">❤</span> you! <span class="emoji">😛</span></p>
```

**NOTE**: The emojis are only replaced when whitespace-delimited on both sides!

The following options are accepted:

 - `emoji`, the emoticon-to-list-of-aliases mapping,
 - `span_class`, the class name of the encompassing `<span>` element
   (default: 'emoji'). No element is created if `None`.

An example with these custom settings:

```python
>>> from mdx_unimoji import UnimojiExtension
>>> img_heart = '<img alt="love" src="heart.png"/>'
>>> img_tongue = '<img alt=":P" src="tongue.png"/>'
>>> overrides = UnimojiExtension.EMOJI
>>> overrides.update({img_heart: ['<3'],
...                   img_tongue: ':p :P :-p :-P'.split()})
>>> print(markdown(text,
...                extensions=[UnimojiExtension(span_class='other',
...                                             emoji=overrides)]))
... # doctest: +NORMALIZE_WHITESPACE
<p>I <img alt="love" class="other" src="heart.png" /> you! \
<img alt=":P" class="other" src="tongue.png" /></p>
```

You can use the `span_class` value in your CSS, e.g.:

    .emoji {
        font-family: "Apple Color Emoji", "Segoe UI Emoji",
                     "Noto Color Emoji", EmojiSymbols, "DejaVu Sans", Symbola;
    }

Install
-------

To install and make available to Markdown, you can issue:

    pip install mdx_unimoji

or

    pip install --upgrade git+git://github.com/kernc/mdx_unimoji.git

Then use the above provided examples to figure your way around.

HF!
