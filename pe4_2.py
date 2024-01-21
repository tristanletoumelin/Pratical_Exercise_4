import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Abnormal detected"

if __name__ == "__main__":

    url = "http://www.rtu.lv"
    #print(getHTMLText(url)[:400])
    payload = {'key1': 'value1', 'key2': 'value2'}
    hd = {'User-Agent': 'Chrome/10'}
    fs = {'file': open("one_txt_file.txt", 'rb')}
    px = {'http': 'http://user:pass@10.10.10.1:1234',
          'https': 'http://10.10.10.1:4321'}
    r = requests.request('PUT', 'http://httpbin.org/put', data=payload, headers=hd, files=fs)
    print(r.text)

    # Example 2 - Shearch engine keyword submission interface
    # keyword = 'Python'
    # try:
    #     kv = {'q':keyword}
    #     r = requests.url("https://gogole.com", params=kv)
    #     print(r.requests.url)
    #     r.raise_for_status()
    #     print(r.text[:500])
    # except:
    #     print('Abnormal detected')

    # print(r.status_code)
    # print(r.encoding)

    #Example 3 Image crawling
    # url = " "
    # root = "/home/tristanletoumelin/home"
    # path = root+url.split('/')[-1]
