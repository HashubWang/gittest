import requests
from bs4 import BeautifulSoup


url = "http://dict.youdao.com/w/{0}/#keyfrom=dict2.top"
searchWord = input("Please enter you want to translate: ")
searchURL = url.format(searchWord)

r = str(requests.get(searchURL).text)
soup = BeautifulSoup(r,"html.parser")

preObject = soup.find("div","trans-container").find_all("li")

result_list = []
# print(type(preObject))
for i in list(preObject):

    res = i.string
    result_list.append(res)


for i in result_list:
    print(i)

# print(result_list)



