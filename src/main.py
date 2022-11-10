import re
import surrogates 
import emoji

emoji_by_name = True

def read(filename):
    f = open(filename, 'r').read()
    return f

def print_emoji(token):
    global emoji_by_name
    return token if emoji_by_name else surrogates.decode(emoji.emojize(token))

def tokenize(text: str, regex: list = [], call_emoji_by_name: bool = True):
    global emoji_by_name
    emoji_by_name = call_emoji_by_name

    re_list = [
            (r"[:][a-z_-]+[:]",                                     lambda scanner,token:('EMOJI', print_emoji(token))),
            (r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]" +
                "|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"+
                "|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])"+
                "|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",    
                                                                    lambda scanner,token:('DOMAIN', token)),
            (r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?",             lambda scanner,token:('NUMBER', token)),
            (r"=|\+|-|\*|/",                                        lambda scanner,token:('OPERATOR', token)),
            (r"[a-z_A-Z]+",                                         lambda scanner,token:('LITERAL', token)),
            (r"(?::|;|X|=)(?:-|')?(?:\)|\(|D|P)",                   lambda scanner,token:('EMOTICON', token)),
            (r"[.][.][.]",                                          lambda scanner,token:('PUNCTUATION', token)),
            (r"[.!?,:;/'‘‘’`\"]",                                   lambda scanner,token:('PUNCTUATION', token)),
            (r"\s+",                                                None), # None == skip token.
        ]

    scanner = re.Scanner(regex + re_list)

    demojized_text = emoji.demojize(text) 
    results, unknown_chars = scanner.scan(demojized_text)

    return results, unknown_chars

def log(text):
    separator = '\t####\t'
    print('\n' + separator + text + separator + '\n')

def main():
    log('TOKENIZER')

    text = read('data/input.txt')

    custom_regex_lst = [
        (r"[.][.][.]", lambda scanner,token:('PUNCTUATION', token))
    ]
    tokenized, skipped = tokenize(text = text, regex = custom_regex_lst)

    log('TOKENIZED  ')
    print('text:\t' + text + '\n')

    for item in tokenized:
        print(item)

    log('SKIPPED')
    for item in skipped:
        print(item)
    
def test():
    pass

if __name__ == '__main__':
    main()
    #test()