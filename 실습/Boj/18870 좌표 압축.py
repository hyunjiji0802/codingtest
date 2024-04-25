import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
sort_arr=sorted(list(set(arr)))

d = dict()

for i in range(len(sort_arr)):
    d[sort_arr[i]]=i

for id in arr:
    print(d[id],end=' ')


# import sys
#
# N=int(input())
# arr=list(map(int,sys.stdin.readline().rstrip().split()))
# sort_arr=sorted(list(set(arr)))
#
# def binary_search(i, sort_arr):
#     start = 0
#     end = len(sort_arr) - 1
#
#     while start <= end:
#         mid = (start+end) // 2
#         if i == sort_arr[mid]:
#             return mid
#
#         elif i < sort_arr[mid]:
#             end = mid - 1
#
#         else:
#             start = mid + 1
#
#     return None
#
# for i in range(N):
#     arr[i]=binary_search(arr[i],sort_arr)
#
# print(" ".join(map(str,arr)))