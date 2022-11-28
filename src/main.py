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
    ]

    for index, item in enumerate(default_regex):
        regex_list.insert(
            (index + default_regex_start_pos)
            if default_regex_start_pos < len(regex_list)
            else len(regex_list),
            item,
        )

    with_index = []
    for item in custom_regex:
        if item["position"] > -1:
            with_index.append(item)

    no_index = [item["function"] for item in custom_regex if item["position"] == -1]

    print(with_index)

    for index, item in enumerate(no_index):
        regex_list.insert(index + 1, item)

    for item in with_index:
        regex_list.insert(
            1 if item["position"] < 1 else item["position"], item["function"]
        )

    regex_list.append((r"\s+", None))  # None == skip token.

    scanner = re.Scanner(regex_list)

    demojized_text = emoji.demojize(text)
    results, unknown_chars = scanner.scan(demojized_text)

    return results, unknown_chars


def log(text):
    separator = "\t####\t"
    print("\n" + separator + text + separator + "\n")


def export_tokens(output, text):
    output.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
    output.write("<tokenized>\n")

    for item in text:
        output.write("\t<item>\n")
        output.write("\t\t<type>")
        output.write(f"{item[0].lower()}")
        output.write("</type>\n")
        output.write("\t\t<token>")
        output.write(f"{item[1]}")
        output.write("</token>\n")
        output.write("\t</item>\n")

    output.write("</tokenized>\n")


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
        position = item["index"] if "index" in item else -1
        position = -1 if position < 0 else position
        custom_regex_config.append(
            {
                "position": position,
                "function": (r"{}".format(item["regex"]), lambda_tokenizer),
            }
        )

    text = read("data/input/input.txt")

    tokenized, skipped = tokenize(
        text=text, default_regex=default_regex_config, custom_regex=custom_regex_config
    )

    log("TOKENIZED  ")
    print("text:\t" + text + "\n")

    file = open("data/output/output.xml", "w")

    export_tokens(file, tokenized)

    for item in tokenized:
        print(item)

    file.close()

    log("SKIPPED")
    for item in skipped:
        print(item)


def test():
    pass


if __name__ == "__main__":
    main()
