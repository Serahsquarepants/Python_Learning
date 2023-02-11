#Return masked string. (8 kyu)

def maskify(cc):
    replacement = ""
    size = len(cc) - 4
    values = cc[-4:]
    for x in range(size):
        replacement = replacement + "#"
    result = replacement + values
    return result