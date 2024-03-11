from collections import deque
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

queue= deque(i+1 for i in range(N))