import requests
from bs4 import BeautifulSoup

url = "http://dict.youdao.com/w/{0}/#keyfrom=dict2.top"
searchWord = input("Please enter you want to translate word: ")
searchURL = url.format(searchWord)

r = str(requests.get(searchURL).text)
soup = BeautifulSoup(r,"html.parser")

preObject=list(soup.find_all("a","p-type"))


for i in preObject:
    res = i.string
    if '计算机科学技术' not in preObject:
        print("no computer meaning")
        break

    if res == '计算机科学技术':
        print("has computer words meaning ")
        snum = i.attrs["rel"][0]

        patten=snum+" types"

        resli=soup.find_all("li",patten)
        result=[]

        for th in resli:
            title = list(th.find_all("span","title"))
            for i in title:
                tt = i.string
                result.append(tt)
            print(result)

        break



