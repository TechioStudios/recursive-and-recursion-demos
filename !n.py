def fact(n):#define function fact
    if n == 1:#if n equals 1, we don't need to continue
        return 1#return 1
    else:#else
        return n * fact(n-1)#return n*fact(n-1)(recursion)

print(fact(10))