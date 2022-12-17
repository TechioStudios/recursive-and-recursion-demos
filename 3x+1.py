import numbers


def get_steps(n):
    step = 0
    num = [n]
    while n != 1:
        if n%2 == 0:
            n = n//2
            num.append(n)
        else:
            n = 3*n+1
            num.append(n)
        step += 1
    return(num,step)
print(get_steps(1000))