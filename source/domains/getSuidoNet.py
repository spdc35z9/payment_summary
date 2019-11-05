# coding: UTF-8
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def getSuidoNet(url,id,password):
    # ヘッドレスモードの設定。
    # True => ブラウザを描写しない。
    # False => ブラウザを描写する。
    options = Options()
    options.add_argument('--headless')
    # Chromeを起動
    driver = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe', chrome_options=options)
    # ログインページを開く
    driver.get(url)
    # ログオン処理
    # ユーザー名入力
    driver.find_element_by_id('userName').send_keys(id)
    # パスワード入力
    driver.find_element_by_id('password').send_keys(password)
    # ログインボタン押下
    driver.find_element_by_xpath("//input[@value='ログイン']").send_keys(Keys.ENTER);
    # soupオブジェクトを作成
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # ログイン後のトップページのソースを表示
    print(soup)
    # ドライバーをクローズ
    driver.close()
    driver.quit()

    now = datetime.datetime.now()
    target_date = '{0:%Y%m}'.format(now)
    receipt_amount = 0
    return target_date,receipt_amount
