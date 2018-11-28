pyramid = []
with open("storage//67_pyramid.txt",'r') as f:
    for line in f:
        temp = line.replace("\n","").split(" ")
        for x in range(len(temp)):
            temp[x] = int(temp[x])
        pyramid.append(temp)

i = len(pyramid)
while i > 1:
    for j in range(len(pyramid[i-2])):
        if pyramid[i-1][j] > pyramid[i-1][j+1]:
            pyramid[i-2][j] += pyramid[i-1][j]
        else:
            pyramid[i-2][j] += pyramid[i-1][j+1]
    i -= 1
    pyramid = pyramid[:i]
    
print('Number:', pyramid[0][0])