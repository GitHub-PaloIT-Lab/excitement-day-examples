import timeit



## Addition of 2 numbers
def add(x, y):
    if y == 0:
        return x
    else:
        return add(x ^ y, (x & y) << 1)


def find_max(list):
    max_val = list[0]
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[j] > max_val:
                max_val = list[j]
    return max_val

def reverse_string(string):
    reversed_string = ""
    index = len(string) - 1
    while index >= 0:
        reversed_string += string[index]
        index -= 1
    return reversed_string

def to_lower_case(string):
    result = ""
    for char in string:
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90:
            result += chr(ascii_value + 32)
        else:
            result += char
    return result

def is_even(n):
    binary_repr = bin(n)
    return binary_repr[-1] == '0'

def sort_list(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def find_element(list, element):
    try:
        list.index(element)
        return True
    except ValueError:
        return False

def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True






