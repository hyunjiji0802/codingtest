arr = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19]]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#index 범위 제한해야 에러 발생하지 않음.

for i in range(len(arr)):
    print(arr[i])
for x in range((len(arr))):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[x][y],":",arr[testX][testY],end=',')
        print("\n")
