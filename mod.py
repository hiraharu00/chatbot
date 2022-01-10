from selenium import webdriver
import time
import os

driver = webdriver.Chrome('/Users/Akutaya/python3/CHATBOT/chromedriver')
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")
search_word =''

#メッセージからコマンドとスペースを除去する
def conversion(word,cmd):
    if word.startswith(cmd)==True:
        global search_word
        search_word=word.removeprefix(cmd)
        search_word=search_word.lstrip()
        

#スクリーンショットを取る
def screenshot(keyword):
    driver.get("https://www.google.com/")       # Googleを開く
    time.sleep(3)                               #3秒待機
    search = driver.find_element_by_name("q")   # 検索ボックス"q"を指定する
    search.send_keys(keyword)  # 検索ワードを送信
    search.submit()                             # 検索を実行
    driver.save_screenshot(filename)
    
#スクリーンショットをアップロードする


#スクリーンショットのURLを持ってくる

#test
conversion('search abcd','search')
print(search_word)
screenshot(search_word)

#aaa