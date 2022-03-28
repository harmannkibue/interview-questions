import re

input = "1203x."


def group_match(input: str) -> bool:
    """
    :param input:
    :return:
    """
    Regex_Pattern = r'[1|2|3]{3}'
    re_exp = re.search(Regex_Pattern, input)
    return re_exp


print(group_match(input))
