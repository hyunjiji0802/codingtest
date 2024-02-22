import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

def step(N):
    i = 0
    step = 1
    while i < N-1:
        print(i,step,arr)
        if arr[i] + arr[i + 1] > arr[i] + arr[i + 2] or i == N - 1:
            arr[i + 1] = arr[i] + arr[i + 1]
            i += 1
            step += 1
        if arr[i] + arr[i + 1] < arr[i] + arr[i + 2] or step == 2:
            arr[i + 2] = arr[i] + arr[i + 2]
            i += 2
            step = 0
    print(i,step,arr)
    return arr[N-1]

print(step(N))
