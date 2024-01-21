import requests
import os
import bs4
from bs4 import BeautifulSoup
import re
from lxml import etree
import numpy as np
# #Example 0.1
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "Abnormal detected"

# #Example 0.2
# url = "http://www.rtu.lv"
# #print(getHTMLText(url)[:400])
# payload = {'key1': 'value1', 'key2': 'value2'}
# hd = {'User-Agent': 'Chrome/10'}
# fs = {'file': open("one_txt_file.txt", 'rb')}
# px = {'https': 'http://10.10.10.1:4321'}
# r = requests.request('PUT', 'http://httpbin.org/put', data=payload, headers=hd, files=fs, proxies=px)
# print(r.text)


# #Example 1 - Crawling of goods web pages
# url = "https://www.euronics.lv/telefoni/viedtalruni/iphone/mpuf3pxfsa/apple-iphone-14-128-gb-melna-viedtalrunis"
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:2000])
# except:
#         print("Abdonormal Detected")

# print(r.status_code)
# print(r.encoding)


# # Example 2 - Shearch engine keyword submission interface
# try:
#     kv = {'tq':'Python'}
#     req = requests.get("https://www.google.com/search", params=kv)
#     print(req.request.url)
#     req.raise_for_status()
#     #print(req.text[:500])
# except:
#     print('Abnormal detected')

# print(req.status_code)
# print(req.encoding)


# #Example 3 Image crawling
# url = "https://www.traveller.ee/blog/wp-content/uploads/2016/07/RigaOldTown_Droneview03-1360x900.jpg"
# root = "/Users/letoumelintristan/Desktop/Riga/Telecommunication/Pratical_Exercise_4/python"
# path = root+url.split('/')[-1]  # Name of the file (last path of url)
# print("-----", path)
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             print("File save successfully")
#     else:
#         print("File already exists")
# except:
#     print('Abnormal detected')

# #Example 3.2
# path = root+url.split('/')

# #Example 4.0
# #r = requests.get("https://www.euronics.lv/telefoni/viedtalruni/iphone/mpuf3pxfsa/apple-iphone-14-128-gb-melna-viedtalrunis")
# #print(r.text)
# r = requests.get("https://www.rtu.lv")
# demo = r.text
# soup = BeautifulSoup(demo, 'html.parser')
# #print(soup.prettify()[4000:])
# print(soup.find_all("div"))


#Example 4.1
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return ""

# def fillUnivList(ulist, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[0].string, tds[4].string])

# def printUnivList(ulist, num):
#     tplt = "{!s:^10}\t{!s:^40}\t{!s:^40}"
#     print(tplt.format("rank", "university name", "total score"))
#     for i in range(num):
#         u = ulist[i]
#         print(tplt.format(u[0], u[1], u[2],))

# def main():
#     uinfo = []
#     url = "https://www.shanghairanking.com/rankings/arwu/2023"
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 5)

# main()


#Example 4.2

# r = requests.get("https://www.shanghairanking.com/rankings/arwu/2023")
# ulist = []
# soup = BeautifulSoup(r.text, 'html.parser')
# for tr in soup.find('tbody').children:
#     if isinstance(tr, bs4.element.Tag):
#         tds = tr('td')
#         ulist.append([tds[0].string, tds[1].string, tds[3].string])
#         #print(tds[1].find_all(string = re.compile('sity')))
#         a= list(tds[1].find_all(string = re.compile('sity')))
#         for l in a:
#             if type(l) == str:
#                 print(l)

# Example 4.3
kv = {'User-Agent':'Mozilla/5.0'}
url = "https://www.shanghairanking.com/rankings/arwu/2023"
page_text = requests.get(url, headers = kv).text
tree = etree.HTML(page_text)
uni = tree.xpath('//div[@class="rk-table-box"]/table/tbody/tr')
print(uni)
all = []
for u in uni:
    uni = u.xpath('./td[2]/div/div[2]/span/text')
    print("-------------------------")
    print(uni)
    all.append(uni)
all = np.reshape(all, (30, 1))
