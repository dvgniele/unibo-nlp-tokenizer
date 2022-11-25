# Tokenizer
> A simple Tokenizer for the Italian language

## Table of Contents
- [Regex Features](#regex) 
- [Emoticons Support](#emoticons-support)
- [Emoji Support](#emoji-support)
- [Custom Configuration Support](#custom-configuration-support)

###

<a name="regex"></a>
## Regex Features
> #### The tokenizer offers the following features

- todo: list of feaures 

<a name="emoticons-support"></a>
## Emoticons Support
> #### The emoji regex is made up by different sections, each composed by a list of characters. The sections are:
- ```Hat```
- ```Eye```
- ```Tear```
- ```Nose```
- ```Mouth```
- ```Reverse (to support reverse emoticons)```

### Emoticons Sections
Hat
```
< > | } 3 O ~ 0
```
```
[<>|}3O~0]
```

Eye
```
: ; 8 = B x X % #
```
```
[:;8=BxX%#]
```


Tear
```
' \ " 
```
```
['\"]
```

Nose
```
- ^ 
```
```
[-^]
```

Mouth
```
) ( 0 3 s S x X D c C p o O P E L Þ þ b / * \ # & $ > < } { [ ] @ |
```
```
[)(03sSxXDcCpoOPELÞþb/*\\#&$><}{\[\]@|]
```

Reverse
```
c C D > <
```
```
[cCD><]
```

Ideal emoticons RegEx
``` 
hat? eye tear? nose? mouth || reverse nose? tear? && eye 
```


<a name="emoji-support"></a>
## Emoji Support

> To grant Emoji Support, the tokenizer makes use of the python [emoji](https://pypi.org/project/emoji/) library, and the list of supported emojis can be found [here](https://carpedm20.github.io/emoji/)


<a name="custom-configuration-support"></a>
## Custom Configuration Support

> The tokenizer offers the possibility to insert a custom regex list, to increase (or to change) the recognition methods. To make use of this feature, the only necessary operation is to add a new rule inside of the file ```data/config/custom_config.json```, as shown:
```
{
    "config": [
        {
            "name":"3 CONSECUTIVE DOTS",
            "regex":"[.][.][.]"
        },
                {
            "name":"4 CONSECUTIVE DOTS",
            "regex":"[.][.][.][.]"
        }
    ]
}

```