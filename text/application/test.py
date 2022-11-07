from selenium import webdriver
#from msedge.selenium_tools import ChromeOptions

#options = ChromeOptions()
# Edge立ち上げ時の制約（Option）の定義


# これがエラーをなくすコードです。ブラウザ制御コメントを非表示化しています
import chromedriver_binary                  # パスを通すためのコード
from selenium.webdriver.chrome.options import Options  # オプションを使うために必要
from selenium.webdriver.common.by import By
import time
import os
import codecs
import subprocess
from config.settings import BASE_DIR
#import chromedriver_binary
#import chromedriver_binary


def sum():
    option = Options()                          # オプションを用意
    # option.add_argument('--headless')
    option.add_experimental_option(
        'excludeSwitches', ['enable-logging'])           # ヘッドレスモードの設定を付与
    option.use_chromium = True
    option.add_argument('--headless')
    chrome = webdriver.Chrome(
        executable_path=  # 'BASE_DIR' + 'text//application//
        'chromedriver.exe', options=option)
    #chrome = webdriver.Chrome(options=option)
    chrome.get("https://sitecreation.co.jp/tenkiyohou/")
    # chrome.find_element_by_class_name("p-postal-code").send_keys("9908570")
    # chrome.find_elements(
    # By.CLASS_NAME, "p-postal-code")[0].send_keys("9908570")
    #ans = 9908670
    # chrome.execute_script(
    #    'document.getElementsByClassName( "p-postal-code").value="%s";' % ans)
    chrome.find_element(
        By.CLASS_NAME, "p-postal-code").send_keys("9908570")

    # chrome.find_element_by_id("btn").click()
    chrome.find_element(By.ID, "btn").click()

    # chrome.find_element_by_id("btn-write").click()
    chrome.find_element(By.ID, "btn-write").click()
    time.sleep(5)
#chrome.find_element_by_class_name("fa fa-files-o").click()
    element = chrome.find_element(By.ID, "copy")
    valString = element.get_attribute("value")

    # print(valString)

    #path = 'tenki1.html'
    #f = codecs.open(path, 'w', 'utf-8')
# n=1
# m=1
# for i in range(10):
#	n=1000*i
#	m=n-1000
#	f.write(valString[m:n])

    # f.write(valString)  # 何も書き込まなくてファイルは作成されました

    # f.close()
    print(valString)
    return valString
    print(open('tenki1.html'))


if __name__ == "__main__":
    sum()
