a = int(input("항의 개수 입력 :"))
n = 3
fibo = [0, 1, 1]

while n<=a:
    if a == 1 or a == 2:
        break
    else:
        fibo.append(fibo[n-1] + fibo[n-2])
    n+=1

fibo.pop(0)
print('피보나치수열 : ', *fibo)