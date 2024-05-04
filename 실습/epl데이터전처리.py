import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('D:/Users/new/Desktop/데브코스/케글경연대회1차/epl우승/train.csv')
test = pd.read_csv('D:/Users/new/Desktop/데브코스/케글경연대회1차/epl우승/test.csv')


train = train.drop(['Season','DateTime','Referee'], axis=1)
test = test.drop(['ID','Season','DateTime','Referee'],axis=1)

train = train.replace({'FTR':'H'},0)
train = train.replace({'FTR':'A'},1)
train = train.replace({'FTR':'D'},2)

train = train.replace({'HTR':'H'},0)
train = train.replace({'HTR':'A'},1)
train = train.replace({'HTR':'D'},2)

test = test.replace({'HTR':'H'},0)
test = test.replace({'HTR':'A'},1)
test = test.replace({'HTR':'D'},2)

label_list = train["HomeTeam"].unique()
label_dic = {}

for i in range(len(label_list)):
  label_dic[label_list[i]] = i
print(label_dic)

for label in label_list:
  train = train.replace({'HomeTeam':label},label_dic[label])
  train = train.replace({'AwayTeam':label},label_dic[label])
  test = test.replace({'HomeTeam':label},label_dic[label])
  test = test.replace({'AwayTeam':label},label_dic[label])

train_data = train[['HomeTeam','AwayTeam','HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR','HTHG','HTAG','HTR','FTHG','FTAG']].to_numpy()
pred_input = test[['HomeTeam','AwayTeam','HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR','HTHG','HTAG','HTR','FTHG','FTAG']].to_numpy()
print(train_data[:10])

train_label = train['type'].to_numpy()
print(train_label[:5])

new = np.concatenate((train_data, pred_input), axis=0)

#StandardScaler 클래스를 이용해 표준화 전처리 수행하기
#객체 모델을 만들고 훈련시키기
ss= StandardScaler()
ss.fit(new)

#훈련 세트의 통계값으로 테스트 세트 변환하기
train_scaled = ss.transform(train_data)
pred_scaled = ss.transform(pred_input)

#로지스틱 회귀모델 객체를 만들고 훈련시키기
lr = LogisticRegression()
lr.fit(train_scaled, train_label)