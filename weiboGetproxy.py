import requests
from bs4 import BeautifulSoup

#indexUrl='http://www.xicidaili.com/nn'

#从西刺获取代理服务器地址
def get_proxy(indexUrl):
    Hostreferer = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': 'http://www.xicidaili.com'
    }
    Picreferer = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': 'http://www.xicidaili.com'
    }
    proxyList = ['101.37.79.125:3128','120.198.67.93:63000','114.113.126.82:80','47.105.149.57:80','47.105.161.159:80']
    #start_html = requests.get(indexUrl, headers=Hostreferer)
    #soup = BeautifulSoup(start_html.text, "html.parser")
    #iDiv = soup.find_all('tr', class_='odd')
    #for n in range(5):
        #iTd = iDiv[n].find_all('td')
        #iTd1 = iTd[1]
        #iTd2 = iTd[2]
        #iTd1 = str(iTd1).replace('<td>', '').replace('</td>', '')
        #iTd2 = str(iTd2).replace('<td>', '').replace('</td>', '')
        #proxyList.append(str(iTd1) + ':' + str(iTd2))
    return proxyList