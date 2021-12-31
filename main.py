from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
import ctypes
import pathlib

script_dir = f'{pathlib.Path(__file__).parent}'


def getScreenShotOfUrl(url):
    serv = Service(f'{script_dir}\\chromedriver.exe')
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--headless")
    chrome_option.add_argument("--start-maximized")
    chrome_option.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=serv, options=chrome_option)
    driver.get(url)
    width = 1920
    height = 1200
    driver.set_window_size(width, height)
    while True:
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body')))
            path = script_dir+'\\mypage.png'
            driver.save_screenshot(path)
            driver.close()
            driver.quit()
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
            break
        except:
            pass
    print('ok')


getScreenShotOfUrl(
    'https://sqa.stackexchange.com/questions/1941/how-do-i-close-the-browser-window-at-the-end-of-a-selenium-test')
# getScreenShotOfUrl('https://flexiple.com/python-get-current-directory/')
