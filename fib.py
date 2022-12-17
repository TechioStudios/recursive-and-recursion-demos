

def fib(n):#define function fib, n = number of nuumbers
    list = [0,1]#starting numbers
    if n == 1:#if we only need to print one nuumber
        return [0]#return a list with 0
    else:#else
        count = 2#starting at the third number
        while count < n:#with line 11, loop for the number of numbers we need
            list.append(list[count-1] + list[count-2])#add and caluculate the next fibunachi number
            count += 1
        return(list)#return the result

print(fib(1000))