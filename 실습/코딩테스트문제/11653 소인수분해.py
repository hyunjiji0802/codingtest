N=int(input())
i=2
while True:
  if N==1:
      break
  if N%i!=0:
      i+=1
  else:
      print(i)
      N//=i