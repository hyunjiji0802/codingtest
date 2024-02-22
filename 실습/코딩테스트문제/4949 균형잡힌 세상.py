from collections import deque
import sys
while True:
    pair = True
    arr = sys.stdin.readline().rstrip()
    st= deque()
    num = 0

    if arr == '.': break

    for i in arr:
        if i == '(' or i == '[':
            st.append(i)
            num+=1
        elif i == ')' and len(st) != 0:
            num += 1
            if st.pop() != '(':
                pair=False
                break
        elif i == ']' and len(st) != 0 :
            num += 1
            if st.pop() != '[':
                pair=False
                break
        elif (i == ']' and len(st) == 0) or (i == ')' and len(st) == 0) :
            num += 1
            pair = False
            break

    if (pair == True or num==0) and len(st)==0 :
        print('yes')
    else:
        print('no')


