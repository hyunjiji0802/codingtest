import random
class D():
    def __init__(self, n, c):
        self.n = n
        self.c = c

    def roll(self):
        score = random.randrange(self.n)+1
        if not self.c(score):
            raise 1
        return score
even_dice =D(6,lambda x:x%2==0)
try:
    total_score=0
    for _ in range(3):
        total_score+=even_dice.roll()
        print("Win!")
except:
    print('Lose!')
finally:
    print("Total:", total_score)

#주사위 세 번 굴려서 6이 나왔다
#두번째 줄이 win이었을 확률
#1.win win
#2.win false win
#3.win false false