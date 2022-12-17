
def duck(n):
    rl = []#list of sold ducks
    list = []#list of numbers
    remain = 2#remainder
    for i in range(n):#loop for how many numbers we need
        last = remain
        remain = remain +1
        remain = remain*2#set remain to (remain+1)*2
        rl.append(remain-last)#append the sold number
        list.append(remain)#append remain
    rl.reverse()
    list.reverse()#reverse the list
    return list,rl#return it
    

print(duck(7))