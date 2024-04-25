import pandas as pd

# 데이터 불러오기
data = pd.read_csv('high_diamond_ranked_10min.csv')

# 블루팀 데이터 분석
blue_avg_gold = data['blueTotalGold'].mean()
blue_kd_ratio = data['blueKills'].sum()/data['blueDeaths'].sum()
blue_ward_count = data['blueDeaths'].mean()

# 블루팀 데이터 분석
red_avg_gold = data['redTotalGold'].mean()
red_kd_ratio = data['redKills'].sum()/data['redDeaths'].sum()
red_ward_count = data['redDeaths'].mean()

# 리포트 생성 함수
def generate_report(blue_avg_gold, blue_kd_ratio, red_avg_gold, red_kd_ratio,blue_ward_count,red_ward_count):
    report = pd.DataFrame({
        'Team': ['Blue Team', 'Red Team'],
        'Average Gold': [blue_avg_gold, red_avg_gold],
        'KD Ratio': [blue_kd_ratio, red_kd_ratio],
        'Average Ward': [blue_ward_count,red_ward_count]
    })
    return report

# 리포트 생성
game_report_df = generate_report(blue_avg_gold, blue_kd_ratio, red_avg_gold, red_kd_ratio,blue_ward_count,red_ward_count)

# 엑셀 파일로 저장
game_report_df.to_excel('game_report.xlsx', index=False)