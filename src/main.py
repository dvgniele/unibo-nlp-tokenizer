import re
import surrogates
import emoji
import json

emoji_by_name = True


def read(filename):
    f = open(filename, "r").read()
    return f


def print_emoji(token):
    global emoji_by_name
    return token if emoji_by_name else surrogates.decode(emoji.emojize(token))


def tokenize(
    text: str,
    default_regex: list = [],
    custom_regex: list = [],
    custom_regex_start_pos: int = 0,
    call_emoji_by_name: bool = False,
):
    global emoji_by_name
    emoji_by_name = call_emoji_by_name
    default_regex_start_pos = 1

    regex_list = [
        (
            r":([a-z]*[_][a-z]*)*[-]?([a-z]*[_]?[a-z]*)*:",
            lambda scanner, token: ("EMOJI", print_emoji(token)),
        ),
        (r"\s+", None),  # None == skip token.
    ]

    for index, item in enumerate(default_regex):
        regex_list.insert(
            (index + default_regex_start_pos)
            if default_regex_start_pos < len(regex_list)
            else len(regex_list),
            item,
        )

    if custom_regex_start_pos > 0:
        for index, item in enumerate(custom_regex):
            regex_list.insert(
                (index + custom_regex_start_pos)
                if custom_regex_start_pos < len(regex_list)
                else len(regex_list),
                item,
            )
    else:
        for index, item in enumerate(custom_regex):
            regex_list.insert(index, item)

    scanner = re.Scanner(regex_list)
    print(scanner)

    demojized_text = emoji.demojize(text)
    results, unknown_chars = scanner.scan(demojized_text)

    return results, unknown_chars


def log(text):
    separator = "\t####\t"
    print("\n" + separator + text + separator + "\n")


def main():
    # * Loading default config
    default_config_file = open("data/config/default_config.json")
    default_config_data = json.load(default_config_file)
    default_config_file.close()

    custom_config_file = open("data/config/custom_config.json")
    custom_config_data = json.load(custom_config_file)
    custom_config_file.close()

    default_regex_config = []
    for item in default_config_data["config"]:
        lambda_tokenizer = lambda scanner, token, item_name=item["name"]: (
            item_name,
            token,
        )
        # *	I need to assign @lambda_tokeizer to get rid of late binding problems for @item['name']`
        default_regex_config.append((r"{}".format(item["regex"]), lambda_tokenizer))

    log("TOKENIZER")

    custom_regex_config = []
    for item in custom_config_data["config"]:
        lambda_tokenizer = lambda scanner, token, item_name=item["name"]: (
            item_name,
            token,
        )
        # *	I need to assign @lambda_tokeizer to get rid of late binding problems for @item['name']`
        custom_regex_config.append((r"{}".format(item["regex"]), lambda_tokenizer))

    # custom_regex_lst = [
    #     #(r"[.][.][.]", lambda scanner,token:('TESTONE', token))
    # ]

    text = read("data/input/input.txt")

    tokenized, skipped = tokenize(
        text=text,
        default_regex=default_regex_config,
        custom_regex=custom_regex_config,
        custom_regex_start_pos=1,
    )

    log("TOKENIZED  ")
    print("text:\t" + text + "\n")

    file = open("data/output/output.txt", "w")

    for item in tokenized:
        file.write(str(item) + "\n")
        print(item)

    file.close()

    log("SKIPPED")
    for item in skipped:
        print(item)


def test():
    pass


if __name__ == "__main__":
    main()
    # test()
