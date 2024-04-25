import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 데이터 불러오기
data = pd.read_csv('high_diamond_ranked_10min.csv')

# 데이터 확인
print(data.head())

# 블루팀 데이터 분석
blue_avg_gold = data['blueTotalGold'].mean()
blue_kd_ratio = data['blueKills'].sum()/data['blueDeaths'].sum()
blue_ward_count = data['blueDeaths'].mean()

# 블루팀 데이터 분석
red_avg_gold = data['redTotalGold'].mean()
red_kd_ratio = data['redKills'].sum()/data['redDeaths'].sum()
red_ward_count = data['redDeaths'].mean()

# 로그 스케일 적용
blue_avg_gold_log = np.log(blue_avg_gold)
red_avg_gold_log = np.log(red_avg_gold)

# 그래프 생성
fig, axes = plt.subplots(1, 2, figsize=(8, 6))

# 블루팀 그래프
bar_width = 0.3  # 막대 너비
blue_positions = [1, 2, 3]  # 각 항목의 x 위치
blue_bars = axes[0].bar([pos - bar_width/2 for pos in blue_positions], [blue_avg_gold, blue_kd_ratio, blue_ward_count], color=['blue', 'green', 'orange'], width=bar_width, label='Blue Team')
axes[0].set_title('Blue Team Statistics')
axes[0].set_xticks(blue_positions)
axes[0].set_xticklabels(['Average Gold', 'K/D Ratio', 'Ward Count'])
axes[0].set_ylabel('Value')

# 레드팀 그래프
red_positions = [pos + bar_width/2 for pos in blue_positions]  # 블루팀과 겹치지 않도록 위치 조정
red_bars = axes[1].bar([pos - bar_width/2 for pos in red_positions], [red_avg_gold, red_kd_ratio, red_ward_count], color=['red', 'purple', 'yellow'], width=bar_width, label='Red Team')
axes[1].set_title('Red Team Statistics')
axes[1].set_xticks(blue_positions)
axes[1].set_xticklabels(['Average Gold', 'K/D Ratio', 'Ward Count'])
axes[1].set_ylabel('Value')

# 각 막대 위에 값을 표시
def autolabel(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom')

autolabel(blue_bars, axes[0])
autolabel(red_bars, axes[1])

# 로그 스케일로 y 축 설정 (평균 골드만)
axes[0].set_yscale('log')
axes[1].set_yscale('log')

# 범례 설정
blue_legend = plt.Line2D([], [], color='blue', label='Blue Team')
green_legend = plt.Line2D([], [], color='green', label='Green Team')
orange_legend = plt.Line2D([], [], color='orange', label='Orange Team')
red_legend = plt.Line2D([], [], color='red', label='Red Team')
purple_legend = plt.Line2D([], [], color='purple', label='Purple Team')
yellow_legend = plt.Line2D([], [], color='yellow', label='Yellow Team')

axes[0].legend(handles=[blue_legend, green_legend, orange_legend], labels=['Average Gold', 'K/D Ratio', 'Ward Count'], loc='upper right', title='Blue Team')
axes[1].legend(handles=[red_legend, purple_legend, yellow_legend], labels=['Average Gold', 'K/D Ratio', 'Ward Count'], loc='upper right', title='Red Team')


plt.tight_layout()
plt.show()