arr = [[1,2,3],[4,5,6],[7,8,9]]

for l in arr:
    print(l)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print("--전치행렬--")
for l in arr:
    print(l)
