import time

import requests
import pandas as pd
import scipy

api_key = "RGAPI-05dcfd6b-7028-4811-ad56-7f42beaea847"
sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +'귀살대 룰루' +'?api_key=' + api_key
r = requests.get(sohwan)
puuid=r.json()['puuid']
print(puuid)
#소환사 고유 id, 계정 고유 id, puu id, 닉네임, 프로필 아이콘id, 수정날짜, 레벨
#이중에서 puu id로 경기 기록 가져옴

start=str(1)
count=str(10)

match = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/-IsUfcovqFcwjyGjgiuBAl8Na4wsPJ_rkVnVFUBKauEOFhq3cf-ZUjyTHWCLk2FRq8Q5OCaf3hbhFg/ids?api_key="+api_key
r = requests.get(match)
print(r.json())
recent=r.json()[0]

print(recent)
'''
match_info_df = pd.concat([match_info_df, pd.DataFrame(r.json()['matches'])])
print(match_info_df)
'''

match_info_url =  "https://asia.api.riotgames.com/lol/match/v5/matches/"+recent+'?api_key='+api_key
print(match_info_url)
r = requests.get(match_info_url)

print(r.json())
match_data_DF=pd.DataFrame(r.json())
#match_data_DF.to_csv("match_DF.csv")
