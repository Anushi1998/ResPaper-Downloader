import os
import config
from robobrowser import RoboBrowser
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.request
from PIL import Image

timeout=20 #20 Seconds timeout

def createBrowser():
    option = webdriver.ChromeOptions()
    option.add_argument('—incognito')
    browser = webdriver.Chrome(options=option)
    return browser


def loginPage(browser):
    browser.get(config.loginPage)
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_all_elements_located);
    except:
        print("Slow Internet?")
        browser.quit()

    browser.find_element_by_xpath('//*[@id="ui"]').send_keys(config.user)
    browser.find_element_by_xpath('//*[@id="pw"]').send_keys(config.password)
    browser.find_element_by_xpath('//*[@id="pw"]').submit()
    browser.get(config.homePage)


def getData(browser):
    numPages = browser.execute_script('return numPages')
    where = 'https://'+browser.execute_script('return window.pCachePath')+browser.execute_script('return gifFileName')+'/'
    all = []
    for i in range(numPages):
        serverPath = where + str(i) + '.gif'
        localPath = '/Users/anumahes/Documents/ResPaperDownloader/' + str(i) + '.gif'
        urllib.request.urlretrieve(serverPath, localPath)
        all.append(Image.open(localPath))
    fileName = '/Users/anumahes/Documents/ResPaperDownloader/test.pdf'
    all[0].save(fileName, resolution=100, save_all=True, append_images=all[1:])


if __name__=="__main__":
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser = createBrowser()
    loginPage(browser)
    browser.get('https://www.respaper.com/aayush25/3848-pdf.html')
    getData(browser)

