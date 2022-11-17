# Tokenizer
> A simple Tokenizer for the Italian language

## Table of Contents
- [Regex Features](#regex) 
- [Emoticons Support](#emoticons-support)
- [Emoji Support](#emoji-support)

###

<a name="regex"></a>
## Features
> #### The tokenizer offers the following features

- Blablabla

<a name="emoticons-support"></a>
## Emoticons Support
> #### The emoji regex is made up by different sections, each composed by a list of characters. The sections are:
- ```Hat```
- ```Eye```
- ```Tear```
- ```Nose```
- ```Mouth```
- ```Reverse (to support reverse emoticons)```

### Sections
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