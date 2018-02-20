import requests
from bs4 import BeautifulSoup

url = "http://dict.youdao.com/w/{0}/#keyfrom=dict2.top"

def Build(searchWord):
    # searchWord = input("Please enter you want to translate word: ")
    searchURL = url.format(searchWord)

    r = str(requests.get(searchURL).text)
    soup = BeautifulSoup(r, "html.parser")
    return soup


def Basic_Search(soup):
    # The basic word meaning
    preObject = soup.find("div", "trans-container").find_all("li")

    result_list = []
    for i in list(preObject):
        res = i.string
        result_list.append(res)

    # print("Base meaning: ")
    # print(result_list)

    return result_list


def Advanced_Search(soup):
    # The word's computer meaning
    preObject = list(soup.find_all("a", "p-type"))

    for i in preObject:
        res = i.string

        if res == '计算机科学技术':
            # print("The computer meaning:  ")
            snum = i.attrs["rel"][0]

            patten = snum + " types"

            resli = soup.find_all("li", patten)
            result = []

            for th in resli:
                title = list(th.find_all("span", "title"))
                for i in title:
                    tt = i.string
                    result.append(tt)
                # print(result)
                return result

            break











