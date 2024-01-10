def print_str(n):
    '''
    根据传入参数n，打印多个*
    :param n:
    :return: n个*
    '''
    s='*'*n
    print(s)
    return s
help(print_str)
#print(print_str.__doc__)
print_str(5)