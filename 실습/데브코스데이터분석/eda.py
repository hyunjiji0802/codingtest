import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product


# 데이터 로드
file_path = 'D:/Users/new/Desktop/데브코스/1차프로젝트/airline_passenger_satisfaction(age_group)2.csv'

data = pd.read_csv(file_path)

# 데이터 확인
# print(data.head())

# # 나이 범주화 함수 정의
# def categorize_age(age):
#     if age < 10:
#         return 'Under 10'
#     elif 10 <= age <= 19:
#         return '10-19'
#     elif 20 <= age <= 29:
#         return '20-29'
#     elif 30 <= age <= 39:
#         return '30-39'
#     elif 40 <= age <= 49:
#         return '40-49'
#     elif 50 <= age <= 59:
#         return '50-59'
#     else:
#         return '60+'
#
# # 나이 범주화 적용
# data['age_group'] = data['Age'].apply(categorize_age)

# 범주형 데이터를 숫자로 변환
# Gender 열의 값을 숫자로 변환
data['Gender'] = data['Gender'].replace({'F': 0, 'M': 1})
# Customer Type 열의 값을 숫자로 변환
data['Customer_Type'] = data['Customer_Type'].replace({'Loyal': 1, 'disloyal': 0})
# Type of Travel 열의 값을 숫자로 변환
data['Type_of_Travel'] = data['Type_of_Travel'].replace({'P': 0, 'B': 1})
# Class 열의 값을 숫자로 변환
data['Class'] = data['Class'].replace({'Business': 2, 'Eco': 1, 'Eco Plus': 0})
# age_group 범주 값 숫자로 변환
data['age_group'] = data['age_group'].replace({'10~19': 0, '20~29': 1, '30~39': 2, '40~49':3, '50~59':4, '60+':5})
#satisfaction 변환
data['Satisfaction'] = data['Satisfaction'].replace({'D': 0, 'S': 1})

# 만족도 관련 컬럼들
satisfaction_columns = [
    'Inflight_wifi_service', 'Departure_Arrival_time_convenient', 'Ease_of_Online_booking',
    'Gate_location', 'Food_and_drink', 'Online_boarding', 'Seat_comfort', 'Inflight_entertainment',
    'Onboard_service', 'Legroom_service', 'Baggage_handling', 'Checkin_service', 'Inflight_service',
    'Cleanliness', 'Satisfaction'
]


# 가능한 모든 조합을 생성
genders = [0, 1]
age_groups = [0, 1, 2, 3, 4, 5]
customer_types = [0, 1]
travel_types = [0, 1]
classes = [0, 1, 2]

# 자동화된 세그먼트 분석
for gender, age_group, customer_type, travel_type, travel_class in product(genders, age_groups, customer_types,
                                                                           travel_types, classes):
    segment = data[(data['Gender'] == gender) &
                   (data['age_group'] == age_group) &
                   (data['Customer_Type'] == customer_type) &
                   (data['Type_of_Travel'] == travel_type) &
                   (data['Class'] == travel_class)]

    if not segment.empty:
        print(
            f'\nSegment - Gender: {gender}, Age Group: {age_group}, Customer Type: {customer_type}, Type of Travel: {travel_type}, Class: {travel_class}')

        # 기초 통계 출력
        print("Descriptive Statistics:")
        print(segment[satisfaction_columns].describe())

        # 상관 관계 출력
        correlation_matrix = segment[satisfaction_columns].corr(method='spearman')
        print("Correlation Matrix:")
        print(correlation_matrix)

        # 상관 관계 히트맵 시각화
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title(
            f'Spearman Correlation Matrix for Satisfaction Attributes\nSegment: Gender={gender}, Age Group={age_group}, Customer Type={customer_type}, Type of Travel={travel_type}, Class={travel_class}')
        plt.show()
