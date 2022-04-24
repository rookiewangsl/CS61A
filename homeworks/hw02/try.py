def invert(x):
    inverse = 1/x
    print('Never printed if x is 0')
    return inverse

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('Handled', e)
        return 0
    
if __name__ == '__main__':
    # invert_safe(1/0)
    try:
        invert_safe(0)
    except ZeroDivisionError as e:
        print('Handled')