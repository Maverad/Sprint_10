

def digit_checker(st):
    result = ''
    for i in st:
        if i.isdigit():
            result += i
    return result