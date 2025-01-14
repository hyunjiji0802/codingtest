from sys import stdin
N, S = map(int,stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))
arr.sort(reverse=True)
print(arr)
answer = 0
left , right = 0, 0
sum = arr[0]
while right < N:
    if sum == S: #합이 만들어지면
        print(right - left)
        break
    elif sum > S: #크면 오른쪽으로 이동

    else: #작으면
        if left <= right: #같으면
            sum -= arr[right]
            right += 1
            sum += arr[right]
            left