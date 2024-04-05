def s(v):
    x_c,y_c=0,0
    x_l=[]
    y_l=[]

    for i in range(len(v)):
        x,y = v[i]
        x_l.append(x)
        y_l.append(y)

    for x,y in zip(x_l,y_l):
        if x_l.count(x)==1:
            x_c = x
        if y_l.count(y)==1:
            y_c = y
    answer =[x_c, y_c]
    return answer


print(s([[1,4],[3,4],[3,10]]))