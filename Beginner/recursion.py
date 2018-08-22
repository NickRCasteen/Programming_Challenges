

def rec(x):
    if x == 0:
        return x
    else:
        print(x)
        return rec(x-1)


print(rec(12))
