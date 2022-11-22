import re
import surrogates 
import emoji
import json

emoji_by_name = True

def read(filename):
    f = open(filename, 'r').read()
    return f

def print_emoji(token):
    global emoji_by_name
    return token if emoji_by_name else surrogates.decode(emoji.emojize(token))

def tokenize(text: str, regex: list = [], regex_start_pos: int = 0, call_emoji_by_name: bool = False):
    global emoji_by_name
    emoji_by_name = call_emoji_by_name

    regex_list = [
            (r":([a-z]*[_][a-z]*)*[-]?([a-z]*[_]?[a-z]*)*:",                    lambda scanner, token:('EMOJI', print_emoji(token))),
            # (r"([<|>}3O~0]?[:;8=BxX%#]['\"]?[-^]?[)(03sSxXDcCpoOPELÞþb/*\\#&$><}{\[\]@|])|([cCD><][-^]?['\"]?[:;8=BxX%#])",  
            #                                                                     lambda scanner, token:('EMOTICON', token)),
                                                                    
            # (r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]" +
            #     "|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"+
            #     "|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])"+
            #     "|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",    
            #                                                                     lambda scanner, token:('DOMAIN', token)),

            # (r"[-+]?[0-9]*(\.|\,)?[0-9]+([eE][-+]?[0-9]+)?(\%|\‰)?",            lambda scanner, token:('NUMBER', token)),
            # (r"=|\+|-|\*|/\%\‰",                                                lambda scanner, token:('OPERATOR', token)),
            # (r"([u][n]|[l]|[g][l]|[n]|[c]|[m]|[t]|[v]|[s]|[d]|[a][l][l])[']",   lambda scanner, token:('LITERAL CONTRACTION', token)),
            # (r"[.][.][.]",                                                      lambda scanner, token:('PUNCTUATION', token)),
            # (r"[.!?,:;/'‘‘’ˈː– `\"\(\)\[\]\{\}]",                               lambda scanner, token:('PUNCTUATION', token)),
            # (r"[A-zÀ-ú]+",                                                      lambda scanner, token:('LITERAL', token)),
            (r"\s+",                                                            None), # None == skip token.
        ]

    if regex_start_pos > 0:
        for index, item in enumerate(regex):
            regex_list.insert((index + regex_start_pos) if regex_start_pos < len(regex_list) else len(regex_list), item)
    else:
        for index, item in enumerate(regex):
            regex_list.insert(index, item)
    
    scanner = re.Scanner
    (regex_list)
    print(scanner)

    demojized_text = emoji.demojize(text) 
    results, unknown_chars = scanner.scan(demojized_text)

    return results, unknown_chars

def log(text):
    separator = '\t####\t'
    print('\n' + separator + text + separator + '\n')

def main():
    config_file = open('data/config/formatted.json')
    config_data = json.load(config_file)
    config_file.close()

    custom_regex_lst = []
    for item in config_data['config']:
        print(item)
        custom_regex_lst.append(
            (r"{}".format(item['regex']), lambda scanner,token:(item['name'], token))
        )


    print(custom_regex_lst)

    log('TOKENIZER')

    text = read('data/input/input.txt')

    # custom_regex_lst = [
    #     #(r"[.][.][.]", lambda scanner,token:('TESTONE', token))
    # ]

    tokenized, skipped = tokenize(text = text, regex = custom_regex_lst, regex_start_pos=1)

    log('TOKENIZED  ')
    print('text:\t' + text + '\n')


    file = open('data/output/output.txt', 'w')

    for item in tokenized:
        file.write(str(item) + '\n')
        print(item)

    file.close()

    log('SKIPPED')
    for item in skipped:
        print(item)
    
def test():
    pass

if __name__ == '__main__':
    main()
    #test()