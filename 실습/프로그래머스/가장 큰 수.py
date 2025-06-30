# def solution(numbers):
#     numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
#     len_num = 4 #원소 크기가 1000 이하이므로 최대 늘릴 수있는 문자열의 길이 4개
#     for _ in numbers:
#         num = numbers.pop(0)
#         numbers.append(num * len_num) #각 수를 연속해서 최대 3자리수로 만들기
#
#     numbers.sort(key=lambda x: x[:len_num], reverse=True)
#
#     for _ in numbers:
#         num = numbers.pop(0)
#         numbers.append(num[:len(num) // len_num]) #늘린 문자열의 길이를 다시 줄이기
#
#     answer = "".join(map(str, numbers))
#
#     if answer == '0' * len(answer): #0이면
#         return '0'
#     else:
#         return answer
#
# print(solution([6,10,2]))
# print(solution([3,30,34,5,9]))
# print(solution([0,0,0,0]))
#
# # def solution(numbers):
# #     numbers = list(map(str,numbers)) #숫자를 문자열로 변환
# #     print(numbers)
# #     for _ in numbers:
# #         num = numbers.pop(0)
# #         numbers.append(num*4)
# #
# #     bucket = [[] for _ in range(10)] #나머지 결과를 담을 버킷
# #     len_num = 4
# #     i = 0
# #
# #     while i < len_num:
# #         for num in numbers:   #각 수의 자리수 비교, 나머지 r 를 버킷에 append
# #             #뒤에서 i 번째 수를 꺼냄,  append
# #             tmp_num = num[:len_num]
# #             r = int(tmp_num[-1+(-i)])
# #             bucket[r].append(num)
# #
# #         numbers = []
# #
# #         for nums in bucket: #버킷의 숫자를 앞에서부터 꺼내서 numbers에 append
# #             while nums :
# #                 num = nums.pop(0)
# #                 numbers.append(num)
# #         i +=1
# #
# #     numbers.reverse()
# #     for _ in numbers:
# #         num = numbers.pop(0)
# #
# #         numbers.append(num[:len(num)//4])
# #
# #     answer = "".join(map(str,numbers))
# #
# #     if answer == '0'*len(answer):
# #         return '0'
# #     else:
# #         return answer

# def solution(numbers):
#     answer = []
#
#     while numbers:
#
#         # numbers.sort(key = lambda x:(-int(str(x)[0]), len(str(x))) )
#
#         numbers.sort(key = lambda x:x )
#
#         max_len_num = numbers[0]
#
#         # print('결과:',numbers)
#
#         if len(str(max_len_num)) == 1:
#             # numbers.sort(key=lambda x: (-int(str(x)[0]), len(str(x)), -sum(int(digit) for digit in str(x)) ))
#             numbers.sort(key=lambda x: (-int(str(x).ljust(4, str(x)[-1])),  -sum(int(digit) for digit in str(x).ljust(4, '9')), len(str(x)) ))
#
#             # print(numbers)
#
#         elif len(str(max_len_num)) == 2:
#             numbers.sort(key=lambda x: ( -int(str(x)[0]), -int(str(x)[1]), len(str(x))) )
#
#             # print(numbers)
#
#         elif len(str(max_len_num)) == 3:
#             numbers.sort(key=lambda x: ( (-int(str(x)[0])), -int(str(x)[1]), -int(str(x)[2]), len(str(x))) )
#
#             # print(numbers)
#
#         elif len(str(max_len_num)) == 4:
#             numbers.sort(key=lambda x: ( -int(str(x)[0]), -int(str(x)[1]), -int(str(x)[2]), -int(str(x)[3]), len(str(x))) )
#
#             # print(numbers)
#
#         answer.append(str(numbers.pop(0)))
#
#         # print('정답',answer)
#
#     return ''.join(answer)
#
#
# # numbers = [3,30,35,34,5,9, 3000]
# numbers = 	[3, 30, 34, 5, 9]
# # numbers = [9, 999, 998, 889, 887]
# print(solution(numbers))



def solution(numbers):
    numbers.sort(key=lambda x: (-int((str(x)*4)[:4])))

    result = ''.join(map(str,numbers))

    return '0' if result[0]=='0' else result


# numbers = [3,30,35,34,5,9, 3000]
# numbers = 	[3, 30, 34, 5, 9]
# numbers = [9, 999, 998, 889, 887]
# numbers = [8, 89, 887]
# numbers = [0,0,0,7,70]
# numbers = [240,240,22,1]
# numbers = [12,121]
# numbers = [21,212]
# numbers = [998,9,999] #-> 9999998
# numbers = [0,0,0,1000]
# numbers = [0,0,1000,0]
# numbers = [1000,0,0,0]
numbers = [40,403]

print(solution(numbers))


