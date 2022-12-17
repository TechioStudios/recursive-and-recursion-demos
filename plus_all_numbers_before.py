def fanb(n):
    if n == 1:
        return 1
    else:
        return n + fanb(n-1)

print(fanb(100))