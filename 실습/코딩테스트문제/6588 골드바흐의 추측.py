import sys

def prime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
def primeList(n):
    for i in range(n):
        arr = []
        for k in range(1, n + 1):
            if prime(k):
                arr.append(k)
        return arr


while True:
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        break
    arr2 = primeList(n)
    a = 1
    b = len(arr2) - 1
    while True:
        if n == arr2[a] + arr2[b]:
            print(str(n) + " = " + str(arr2[a]) + " + " + str(arr2[b]))
            break
        elif n >= arr2[a] + arr2[b]:
            a += 1
        elif n <= arr2[a] + arr2[b]:
            b -= 1
        else:
            print("Goldbach's conjecture is wrong.")