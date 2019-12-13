def square_digits(num):
    list_num = [int(x)**2 for x in str(num)]
    num = ""
    for x in list_num:
        num += str(x)
    return int(num)
