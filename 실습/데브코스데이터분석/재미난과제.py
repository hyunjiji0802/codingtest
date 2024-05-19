'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# 데이터 생성
data_cover = {
    '시각': ['1:29', '1:30', '1:31', '1:32', '1:33', '1:34', '1:35', '1:36', '1:37', '1:38', '1:39'],
    '온도': [-5.7, -5.7, -5.6, -5.4, -4.9, -4.2, -3.5, -2.6, -1.7, -0.6, 0.4]
}

data_no_cover = {
    '시각': ['1:29', '1:30', '1:31', '1:32', '1:33', '1:34', '1:35', '1:36', '1:37', '1:38', '1:39'],
    '온도': [-12.8, -12.6, -11.9, -9.9, -7.2, -4.0, -0.9, 2.1, 4.8, 7.2, 9.1]
}

df_cover = pd.DataFrame(data_cover)
df_no_cover = pd.DataFrame(data_no_cover)

# 온도 변화율 계산 함수
def calculate_temp_change_rate(df):
    temp_changes = []
    times = list(range(len(df['온도'])))
    for i in range(1, len(df['온도'])):
        delta_t = times[i] - times[i-1]
        delta_temp = df['온도'][i] - df['온도'][i-1]
        temp_changes.append(float(delta_temp / delta_t))
    return temp_changes

# 온도 변화율 계산
cover_change_rate = calculate_temp_change_rate(df_cover)
no_cover_change_rate = calculate_temp_change_rate(df_no_cover)

# 기술통계량 계산
print(cover_change_rate)
print(no_cover_change_rate)

cover_stats = pd.Series(cover_change_rate).describe()
se = pd.Series(cover_change_rate).std()/np.sqrt(10)
print('se:',se)
no_cover_stats = pd.Series(no_cover_change_rate).describe()
print("Cover Change Rate Statistics:\n", cover_stats)
print("No Cover Change Rate Statistics:\n", no_cover_stats)

# # 온도 변화율 비교 - 박스플롯
# plt.figure(figsize=(10, 6))
# plt.boxplot([cover_change_rate, no_cover_change_rate], labels=['Cover', 'No Cover'])
# plt.ylabel('Temperature Change Rate (°C per minute)')
# plt.title('Temperature Change Rate Comparison')
# plt.show()




# 가설 검정 (t-test)
t_stat, p_value = ttest_ind(cover_change_rate, no_cover_change_rate)
print(f't-statistic: {t_stat}, p-value: {p_value}')

# 결과 해석
alpha = 0.05
if p_value < alpha:
    print("The difference in temperature change rates is statistically significant.")
else:
    print("The difference in temperature change rates is not statistically significant.")'''

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, shapiro, levene


# 데이터 생성
data_cover = {
    '시각': ['1:29', '1:30', '1:31', '1:32', '1:33', '1:34', '1:35', '1:36', '1:37', '1:38', '1:39'],
    '온도': [-5.7, -5.7, -5.6, -5.4, -4.9, -4.2, -3.5, -2.6, -1.7, -0.6, 0.4]
}

data_no_cover = {
    '시각': ['1:29', '1:30', '1:31', '1:32', '1:33', '1:34', '1:35', '1:36', '1:37', '1:38', '1:39'],
    '온도': [-12.8, -12.6, -11.9, -9.9, -7.2, -4.0, -0.9, 2.1, 4.8, 7.2, 9.1]
}

df_cover = pd.DataFrame(data_cover)
df_no_cover = pd.DataFrame(data_no_cover)

# 분당 온도 변화율 계산
df_cover['온도 변화율'] = df_cover['온도'].diff().fillna(0)
df_no_cover['온도 변화율'] = df_no_cover['온도'].diff().fillna(0)

print("보냉 커버 적용 데이터:")
print(df_cover)

print("\n보냉 커버 미적용 데이터:")
print(df_no_cover)

# 보냉 커버 적용 그룹
n_cover = len(df_cover['온도 변화율'])
mean_cover = df_cover['온도 변화율'].mean()
std_dev_cover = df_cover['온도 변화율'].std()
se_cover = std_dev_cover / np.sqrt(n_cover)

# 보냉 커버 미적용 그룹
n_no_cover = len(df_no_cover['온도 변화율'])
mean_no_cover = df_no_cover['온도 변화율'].mean()
std_dev_no_cover = df_no_cover['온도 변화율'].std()
se_no_cover = std_dev_no_cover / np.sqrt(n_no_cover)

print(f"보냉 커버 적용 - 표본 크기: {n_cover}, 표본 평균: {mean_cover}, 표본 표준편차: {std_dev_cover}, 표준 오차: {se_cover}")
print(f"보냉 커버 미적용 - 표본 크기: {n_no_cover}, 표본 평균: {mean_no_cover}, 표본 표준편차: {std_dev_no_cover}, 표준 오차: {se_no_cover}")

# 정규성 검정
shapiro_cover = shapiro(df_cover['온도 변화율'])
shapiro_no_cover = shapiro(df_no_cover['온도 변화율'])
print(f"보냉 커버 그룹 정규성 검정 p-value: {shapiro_cover.pvalue}")
print(f"보냉 커버 없음 그룹 정규성 검정 p-value: {shapiro_no_cover.pvalue}")

# 등분산성 검정
levene_test = levene(df_cover['온도 변화율'], df_no_cover['온도 변화율'])
print(f"등분산성 검정 p-value: {levene_test.pvalue}")

# T 검정 (등분산 가정)
t_stat, p_value = ttest_ind(df_cover['온도 변화율'], df_no_cover['온도 변화율'], equal_var=True)
print(f"T 검정 결과 (등분산 가정) - t-statistic: {t_stat}, p-value: {p_value}")

# Welch's T 검정 (등분산 가정하지 않음)
welch_t_stat, welch_p_value = ttest_ind(df_cover['온도 변화율'], df_no_cover['온도 변화율'], alternative="less", equal_var=False)
print(f"Welch's T 검정 결과 (등분산 가정하지 않음) - t-statistic: {welch_t_stat}, p-value: {welch_p_value}")

# 결과 해석
alpha = 0.05
if p_value < alpha:
    print("귀무가설을 기각합니다. 보냉 커버 적용 방식과 미적용 방식의 분당 평균 온도 상승률은 통계적으로 유의미한 차이가 있습니다.")
else:
    print("귀무가설을 기각할 수 없습니다. 보냉 커버 적용 방식과 미적용 방식의 분당 평균 온도 상승률은 통계적으로 유의미한 차이가 없습니다.")
