# Function that takes as argument a sequence and returns a list of items without any repeated element
# next to each other, preserving the original order of elements. (6 kyu)

def unique_in_order(sequence):
    list = []
    previous = None
    for char in sequence:
        if char != previous:
            list.append(char)
            previous= char
    return list
