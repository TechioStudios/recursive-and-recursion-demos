def yhtri(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    else:
        triangle = [[1],
                    [1,1]]
        count = 1
        
        while count<n-1:

            layer = []
            
            for i in range(count):
                layer.append(triangle[count][i]+triangle[count][i+1])
            layer.append(1)
            layer.insert(0,1)
            triangle.append(layer)
            count += 1
        return triangle
tri = yhtri(10)
for i in tri:
    print(i)