import base64
import requests
from bs4 import BeautifulSoup
from urllib import parse


class PcStoreCrawler():
    def fetchIt(self, inputText):
        searchText = base64.b64encode(
            str.encode(parse.quote(inputText))).decode()
        url = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word=" + \
            searchText + "&slt_k_option=1"

        res = requests.get(url)
        res.encoding = 'big5'
        soup = BeautifulSoup(res.text, 'html.parser')
        item = soup.select("div.pic2t_bg > a")
        titleArray = []
        for i in item:
            titleArray.append(i.get_text())
        return titleArray
