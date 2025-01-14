import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ChromeDriver 경로 설정
driver_path = "D:\Deeplearningprojects\실습\자동화\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service= service)

# 네이버 로그인 페이지로 이동
driver.get("https://nid.naver.com/nidlogin.login")
input("수동으로 로그인한 후 Enter를 누르세요...")

# 로그인 후 쿠키 저장
pickle.dump(driver.get_cookies(), open("D:\Deeplearningprojects\실습\자동화\\naver_cookies.pkl", "wb"))
print("쿠키 저장 완료")
driver.quit()
