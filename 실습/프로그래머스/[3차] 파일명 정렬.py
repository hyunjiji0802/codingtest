import re

def split_file(file):
    #첫 숫자가 나오는 것만 split 하기. maxsplit = 1 로 하면 한 번만 하고 나머진 tail로
    tmp = re.split(r"([0-9]+)",file, maxsplit=1)
    return tmp

def solution(files):
    split_list =[]
    for file in files:
        split_list.append(split_file(file))

    #x = ['img', '10', '.jpg']
    #x[0] = 'img'
    #x[1] = '10'

    #처음에 런타임 에러 난 코드 -> 숫자가 모두 000, 0인 경우에는 빈 문자열이 되어 에러가 남.
    #split_list.sort(key = lambda x:(str(x[0]).upper(), int(re.sub(r"^0+","",x[1]))))
    split_list.sort(key = lambda x:( x[0].upper(), int(x[1]) ))
    answer = []
    for splits in split_list:
        answer.append(''.join(splits))

    return answer

#print(solution(["F13.png", "f013", "F013.TXT", "F14", "F014"]))
#print(solution(["img000012345", "img1.png","img2","IMG02"]))
print(solution(["img0000.jpg", "img1.png","img2","IMG02"]))
