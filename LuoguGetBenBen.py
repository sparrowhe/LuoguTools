from pyquery import PyQuery as pq
import requests
def getBenBen(uid):
    requests.packages.urllib3.disable_warnings()
    url='https://www.luogu.org/feed/user/'+str(uid)
    headers = {'origin': 'https://www.luogu.org','referer': 'https://www.luogu.org/','x-csrf-token': '1555681901:DP941gBQvP6BfQC2wH7yeGiMSeUARZ5Mgb7wA2TR9vw=','x-requested-with': 'XMLHttpRequest','User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2526.80 Safari/537.36 Core/1.45.933.400 QQBrowser/9.0.8699.400', 'Accept-Encoding' : 'gzip, deflate, sdch'}
    r=str(requests.get(url,headers=headers,verify=False).content)
    d = pq(str(r))
    d('.feed-comment p')
    return(d('.feed-comment p'))