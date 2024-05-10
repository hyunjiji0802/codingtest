def trapping_rain(heights):
    rains=0
    id=0
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            if heights[j]>=heights[i] and heights[i]>0 and i>=id :
                rains+= (j-i-1)*heights[i]
                for k in range(i+1,j):
                    rains-=heights[k]
                id=j
    return rains

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


