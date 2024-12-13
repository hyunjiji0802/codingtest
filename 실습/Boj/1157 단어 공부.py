# word = str(input()).upper()
# dic = {}
# for s in word:
#     if s in dic:
#         dic[s] += 1
#     else:
#         dic[s] = 1
#
# #정답, 최대값 초기화
# max_num = 0
# answer = ''
# for k, v in dic.items():
#     if max_num < v:
#         max_num = v
#         answer = k
#     elif max_num != 0 and max_num == v: #동일하면
#         answer = '?'
# print(answer)

from collections import Counter

word = str(input()).upper()
word_counts = Counter(word)
print(word_counts)

