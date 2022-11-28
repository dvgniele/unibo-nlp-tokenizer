# Tokenizer

> A simple Tokenizer for the Italian language

## Table of Contents

-   [Regex Features](#regex)
-   [XML Output](#xml-out)
-   [Custom Configuration Support](#custom-configuration-support)
-   [Emoticons Support](#emoticons-support)
-   [Emoji Support](#emoji-support)

###

<a name="regex"></a>

## Regex Features

-   Emojis 😏
-   Emoticons
-   Domain
-   Numbers
-   Operators (numerical)
-   Punctuation
-   Literals

<a name="xml-out"></a>

## XML Output

> The generate output will be put in the _ready-to-use_ `data/output/output.xml` document, to be used as easy as possile. 😊

```

<?xml version="1.0" encoding="UTF-8" ?>
<tokenized>
	<item>
		<type>literal</type>
		<token>emoji</token>
	</item>
	<item>
		<type>literal</type>
		<token>test</token>
	</item>
	<item>
		<type>emoji</type>
		<token>😶‍🌫️</token>
	</item>
</tokenized>

```

<a name="custom-configuration-support"></a>

## Custom Configuration Support

> The tokenizer offers the possibility to insert a custom regex list, to increase (or to change) the recognition methods. To make use of this feature, the only necessary operation is to add a new rule inside of the file `data/config/custom_config.json`, as shown:

```
{
    "config": [
        {
            "name":"3 CONSECUTIVE DOTS",
            "regex":"[.][.][.]",
            "index": 2
        },
        {
            "name":"4 CONSECUTIVE DOTS",
            "regex":"[.][.][.][.]"
        }
    ]
}

```

> The `index` argument is optional, and can be used to choose the priority to recognize the `type`. It can be omitted if there is no particular preference, in that case, those types will be sorted by reading order. Indexes < 1 will be automatically set to -1, thus the chosen priority will be lost. This is because the first `type` **_MUST_** be the one capable of recognizing emojis.

<a name="emoticons-support"></a>

## Emoticons Support

> #### The emoji regex is made up by different sections, each composed by a list of characters. The sections are:

-   `Hat`
-   `Eye`
-   `Tear`
-   `Nose`
-   `Mouth`
-   `Reverse (to support reverse emoticons)`

### Emoticons Sections

Hat

```
< > | } 3 O ~ 0
```

Eye

```
: ; 8 = B x X % #
```

Tear

```
' \ "
```

Nose

```
- ^
```

Mouth

```
) ( 0 3 s S x X D c C p o O P E L Þ þ b / * \ # & $ > < } { [ ] @ |
```

Reverse

```
c C D > <
```

Ideal emoticons RegEx

```
hat? eye tear? nose? mouth || reverse nose? tear? && eye
```

<a name="emoji-support"></a>

## Emoji Support

> To grant Emoji Support, the tokenizer makes use of the python [emoji](https://pypi.org/project/emoji/) library, and the list of supported emojis can be found [here](https://carpedm20.github.io/emoji/)
