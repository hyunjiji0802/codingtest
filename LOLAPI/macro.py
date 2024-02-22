from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys, os, time


def RunChrome(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome('D:\Deeplearningprojects\LOLAPI\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(1)
    driver.get(url)
    driver.implicitly_wait(1)
    return driver


def FocusScrollByElement(driver, element):
    scrollElementIntoMiddle = """var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
                                         var elementTop = arguments[0].getBoundingClientRect().top;
                                         window.scrollBy(0, elementTop-(viewPortHeight/2));"""
    driver.execute_script(scrollElementIntoMiddle, element)


def Menu():
    print("")
    print("1. Run Driver and Login")
    print("2. Find")
    print("3. Exit")
    menu = input("Select: ")

    if menu.isdigit():
        return int(menu)
    else:
        return 0


def RunDriver():
    url = 'https://www.duksung.ac.kr/main.do?isMaster=N&isLogined=N&viewPrefix=%2FWEB-INF%2Fjsp%2Fcms&urlRootPath=&siteResourcePath=%2Fsite%2Fduksung'
    driver = RunChrome(url)

    #Login(driver)
    #KaKaoLogin(driver)
    # PlayMusic(driver)
    # PauseMusic(driver)
    btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div/div/div[2]/div/div')
    btn.click()

    return driver


def Login(driver):
    btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[2]/button/span[1]')
    btn.click()

    btn = driver.find_element_by_xpath('//*[@id="btn-login-kakao"]')
    btn.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    return driver


def KaKaoLogin(driver):
    email = driver.find_element_by_xpath('//*[@id="id_email_2"]')
    email.send_keys('01038184174')

    pw = driver.find_element_by_xpath('//*[@id="id_password_3"]')
    pw.send_keys('BAPpl1211!qwer')

    btn = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]')
    btn.click()

    driver.implicitly_wait(time_to_wait=5)

    driver.switch_to.window(driver.window_handles[0])
    return driver


def FirstPlayMusic(driver):
    print("Play music!")
    btn = driver.find_element_by_xpath('//*[@id="main"]/div/section[1]/div[4]/span[1]')
    btn.click()
    btn = driver.find_element_by_xpath('//*[@id="main"]/div/section[1]/div[2]/ul/li[1]/button')
    btn.click()

    return driver


def PauseMusic(driver):
    print("Music paused")
    btn = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[2]/button[3]')
    btn.click()

    return driver


def PlayNextMusic(driver):
    print("Play next music")
    btn = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[2]/button[4]')
    btn.click()

    return driver


def PlayPrevMusic(driver):
    print("Play previous music")
    btn = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[2]/button[2]')
    btn.click()

    return driver


def PlayRepeatedly(driver):
    print("Play music repeatedly")
    btn = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[2]/button[1]')
    btn.click()

    return driver


def Shuffle(driver):
    print("Shuffle playlist")
    btn = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section[1]/div/div[2]/div[2]/button[5]')
    btn.click()

    return driver


def SearchSong(driver, arg):
    print("Search by song name")
    search = driver.find_element_by_xpath('//*[@id="searchKeywordInput"]')
    search.send_keys(arg)
    remove = driver.find_element_by_xpath('//*[@id="header"]/div/fieldset/button')
    remove.click()
    search.send_keys(arg)
    search.send_keys(Keys.RETURN)

    driver.implicitly_wait(time_to_wait=5)

    btn = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/button')
    btn.click()

    return driver


def VolumeControl(driver, arg):
    volbar = driver.find_element_by_class_name('volume_handle')
    print(volbar.value_of_css_property("left"))
    driver.execute_script("arguments[0].style.left=" + str(arg) + "; return arguments[0];", volbar)

    return driver


def SelectAllByKeyword(driver, _delayTime):
    keyword = input("Keyword: ")
    checker = True
    index = 1
    while checker:
        checker = SelectOneByKeyword(driver, keyword, index, _delayTime)
        index = index + 1
    print("Done")


def SelectOneByKeyword(driver, keyword, index, _delayTime):
    strIndex = str(index)
    xPath1 = '//*[@id="main"]/div/div[2]/div[2]/table/tbody/tr[' + strIndex + ']'
    xPath2 = 'td[3]/p/span[1]/span/span/a'
    xPath3 = xPath1 + '/td[1]'

    try:
        list1 = driver.find_element_by_xpath(xPath1)
        artist = list1.find_element_by_xpath(xPath2).text

        if artist.find(keyword) >= 0:
            ClickBtnWithFocus(driver, xPath3, _delayTime)

        return True
    except:
        return False


RunDriver()
while True:
    pass