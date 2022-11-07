from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from config.settings import BASE_DIR


class LoginTest(LiveServerTestCase):
    # @classmethod
    # def setUpClass(cls):
    #   super().setUpClass()
    #   cls.selenium = WebDriver(
    #      executable_path='BASE_DIR' + 'text//application//chromedriver.exe')

    # @classmethod
    # def tearDownClass(cls):
    #   cls.selenium.quit()
    #   super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        super().setUpClass()
        # self.selenium = WebDriver(
        # executable_path='BASE_DIR' + 'text//application//chromedriver.exe')

        # self.selenium.get('http://127.0.0.1:8000/admin')

        # ログイン
        #username_input = self.selenium.find_element_by_name("username")
        # username_input = self.selenium.find_element(
        #    By.NAME, "username")
        # username_input.send_keys('admin')
        #password_input = self.selenium.find_element_by_name("password")
        # password_input = self.selenium.find_element(
        #    By.NAME, "password")
        # password_input.send_keys('adminadmin')
        #self.selenium.find_element(By.CLASS_NAME, 'login').click()

        # ページタイトルの検証
        #self.assertEquals('ログイン後ページ', self.selenium.title)
        option = Options()                          # オプションを用意
    # option.add_argument('--headless')
        option.add_experimental_option(
            'excludeSwitches', ['enable-logging'])           # ヘッドレスモードの設定を付与
        option.use_chromium = True
        option.add_argument('--headless')
        self.chrome = WebDriver(
            executable_path='BASE_DIR' + 'text//application//chromedriver.exe', options=option)
        self.chrome.get("https://sitecreation.co.jp/tenkiyohou/")
    # chrome.find_element_by_class_name("p-postal-code").send_keys("9908570")
    # chrome.find_elements(
    # By.CLASS_NAME, "p-postal-code")[0].send_keys("9908570")
    #ans = 9908670
    # chrome.execute_script(
    #    'document.getElementsByClassName( "p-postal-code").value="%s";' % ans)
        self.chrome.find_element(
            By.CLASS_NAME, "p-postal-code").send_keys("9908570")

    # chrome.find_element_by_id("btn").click()
        self.chrome.find_element(By.ID, "btn").click()

    # chrome.find_element_by_id("btn-write").click()
        self.chrome.find_element(By.ID, "btn-write").click()
        time.sleep(5)
#chrome.find_element_by_class_name("fa fa-files-o").click()
        element = self.chrome.find_element(By.ID, "copy")
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
