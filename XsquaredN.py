def sqrt(x,n):
    if n == 1:
        return x
    else:
        return x * sqrt(x,n-1)

print(sqrt(2,4))