import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriver 경로 설정
driver_path = "D:\Deeplearningprojects\실습\자동화\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service= service)

# 네이버 메인 페이지로 이동
driver.get("https://www.naver.com")

# 쿠키 로드 및 브라우저에 적용
cookies = pickle.load(open("naver_cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

# 새로고침 후 로그인 상태 확인
driver.refresh()
print("로그인 상태 유지")
