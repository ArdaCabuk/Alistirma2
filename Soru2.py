def toplama(x):
    if x == 0:
        return 0
    else:
        return x + toplama(x-1)
