# Tokenizer

### Components
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
) ( 0 3 s S x X D p o O P E L Þ þ b / * \ # & $ > < } { [ ] @ |
```
```
[)(03sSxXDpoOPELÞþb/*\\#&$><}{\[\]@|]
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