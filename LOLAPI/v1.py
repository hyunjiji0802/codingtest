import time

import requests
import pandas as pd
import scipy

api_key = 'RGAPI-481b401a-bafe-4e87-b900-ad6c9ac2981c'
sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +'hide on bush' +'?api_key=' + api_key
r = requests.get(sohwan)
print(r.json()['id']) #소환사의 고유 id 가져오기
#소환사 고유 id, 계정 고유 id, puu id, 닉네임, 프로필 아이콘id, 수정날짜, 레벨


tier_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + r.json()['id'] +'?api_key=' + api_key
r2  = requests.get(tier_url)
print(r2.json()[0]['summonerId'])
## 리그 고유 id, 큐타입, 티어, 랭크, 소환사 고유 id, 소환사 닉네임, 티어 포인트, 승, 패

grandmaster = 'https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key=' + api_key
r = requests.get(grandmaster)#그마데이터 호출
league_df = pd.DataFrame(r.json())
print(league_df)

league_df.reset_index(inplace=True)#수집한 그마데이터 index정리
league_entries_df = pd.DataFrame(dict(league_df['entries'])).T #dict구조로 되어 있는 entries컬럼 풀어주기
league_df = pd.concat([league_df, league_entries_df], axis=1) #열끼리 결합

league_df = league_df.drop(['index', 'queue', 'name', 'leagueId', 'entries', 'rank'], axis=1)
league_df.info()
league_df.to_csv('그마데이터.csv',index=False,encoding = 'cp949')#중간저장

for i in range(len(league_df)):
    try:
        sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[
            i] + '?api_key=' + api_key
        r = requests.get(sohwan)

        while r.status_code == 429:
            time.sleep(5)
            sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[
                i] + '?api_key=' + api_key
            r = requests.get(sohwan)

        account_id = r.json()['accountId']
        league_df.iloc[i, -1] = account_id

    except:
        pass
