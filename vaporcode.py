import re


def vaporcode(s):
    string_upper = re.sub(r"\s+", "", s).upper()
    vapor_string = "  ".join(string_upper)
    return vapor_string


print(vaporcode("Why isn't my code working?"))