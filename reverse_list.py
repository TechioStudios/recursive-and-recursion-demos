result = []

def reverse(list):
    if list:
        tmp = list.pop()
        result.append(tmp)
        reverse(list)
        
    else:
        pass

reverse([10,9,8,7,6,5,4,3,2,1])
print(result)