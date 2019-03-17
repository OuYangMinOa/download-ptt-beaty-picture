import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve
import time
url="https://www.ptt.cc/bbs/Beauty/index.html"
name = 0
driver = webdriver.Chrome()
for _ in range(3):
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    articles = soup.select("div.title a")
    paging=soup.select("div.btn-group-paging a")
    next_url= "http://www.ptt.cc"+paging[1]["href"]
    url=next_url
    for article in articles:
        print(article.text,article["href"])
        driver.set_page_load_timeout(10)
        driver.get("http://www.ptt.cc"+article["href"])
        time.sleep(1)
        driver.refresh()
        soup = BeautifulSoup(driver.page_source,"html.parser")
        get_img = soup.find_all('img')
        if (get_img !=[]):
            for i in get_img:
                try:
                    html = i.get('src')
                    print(html)
                    name += 1
                    urlretrieve(html,str(name)+'.jpg')
                    print(str(name)+'.jpg')
                except Exception as e:
                    print(e)
        else:
            get_img_2 = soup.find_all('a',href=True)
            for j in get_img_2:
                html = j['href']
                if ('imgur' in html):
                    if ('gif' in html):
                        try:
                            name += 1
                            urlretrieve(html,str(name)+'.gif')
                            print(str(name)+'.gif')
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            name += 1
                            urlretrieve(html,str(name)+'.jpg')
                            print(str(name)+'.jpg')
                        except Exception as e:
                            print(e)
