
# <bitbar.title>微博热搜</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Bboysoul</bitbar.author>
# <bitbar.author.github>bboysoul</bitbar.author.github>
# <bitbar.desc>微博热搜</bitbar.desc>
# <bitbar.image>https://github.com/nok/conda-envs/blob/master/themes/dark.png?raw=true</bitbar.image>
# <bitbar.dependencies>conda</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/nok/conda-envs</bitbar.abouturl>

from bs4 import BeautifulSoup
import requests
import json
import datetime


def get_resou():
    response = requests.get("https://s.weibo.com/top/summary?cate=realtimehot")
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all('a')
    resou = []
    id = 0
    for link in links:
        if "/weibo?" in str(link):
            name = link.string
            url = "https://s.weibo.com/" + link['href']
            item = dict(id = id ,name=name,url=url)
            resou.append(item)
            id = id + 1
    resou = resou[1:51]
    return resou
class Color:
    GREEN = '#3bb15c'
    BLUE = '#4a90f3'

def main():
    resou = get_resou()
    print("---")
    for i in resou:
        print(str(i["id"]) + ":" + i["name"] + " | href=" + i["url"] + " color=%s" % Color.BLUE)

if __name__ == "__main__":
    print("微博热搜 | color=%s " % Color.GREEN)
    main()
        
    
