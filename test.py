import requests
from bs4 import BeautifulSoup

# 发送HTTP请求时的HEAD信息，用于伪装为浏览器,不然可能被察觉到是爬虫脚本
headersParameters = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

httpRsp = requests.get("http://www.baidu.com/s?wd={}".format('英荔'), headers=headersParameters)
# httpResult = requests.get("https://www.zxxblog.cn", headers=headersParameters)
# print(httpRsp.text)
if httpRsp.status_code != 200:
    print("数据获取失败")
else:
    soup = BeautifulSoup(httpRsp.text, "lxml")
    results = soup.select(".c-container")
    print(len(results))
    # 用于保存提取的数据
    resultArr = []
    for index in range(len(results)):
        # 获取标题所在的a标签
        aTag = results[index].select("h3 a")[0]
        # 获取标题的文本
        title = aTag.get_text()
        # 获取网页的真实URL
        href = aTag.attrs["href"]
        resultArr.append({
            "title": title,
            "href": href,
        })

    # 输出前两个看看
    print(resultArr[: 2])
