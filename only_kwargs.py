def foo(a, b, *, c=None):
    print(a, b, c)


if __name__ == '__main__':
    foo(1, 2, c=3)
    
