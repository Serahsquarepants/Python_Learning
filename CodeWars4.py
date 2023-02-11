# Given a String of space separaed numbers, return the highest and lowest number. (7 kyu)

def high_and_low(numbers):
    list = numbers.split(" ")
    max_num = -1000000
    min_num = 10000000
    for i in list:
        i= int(i)
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i 
    return "{} {}".format(max_num, min_num)

print(high_and_low("5 0 1 10"))