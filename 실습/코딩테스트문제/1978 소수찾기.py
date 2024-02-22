'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
출력
주어진 수들 중 소수의 개수를 출력한다.
'''
import sys

num=int(sys.stdin.readline().rstrip())
line=list(map(int,sys.stdin.readline().rstrip().split()))
count = 0
for i in line:
    if i==1 :  #1은 소수가 아님'''
        count+=1
    for k in range(2,i): #2부터 i-1까지 확인
        if i%k==0:
            count+=1
            break
print(num-count)