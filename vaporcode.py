import re

def vaporcode(s):
    stringUpper = re.sub(r"\s+", "", s).upper()
    vaporString = "  ".join(stringUpper)
    return vaporString

print(vaporcode("Why isn't my code working?"))