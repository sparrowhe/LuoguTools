import requests
def sendBenBen(content,client_id,uid):
	url="https://www.luogu.org/api/feed/postBenben"
	data={'content':str(content)}
	my_headers = {'origin': 'https://www.luogu.org','referer': 'https://www.luogu.org/','x-csrf-token': '1555681901:DP941gBQvP6BfQC2wH7yeGiMSeUARZ5Mgb7wA2TR9vw=','x-requested-with': 'XMLHttpRequest','User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2526.80 Safari/537.36 Core/1.45.933.400 QQBrowser/9.0.8699.400', 'Accept-Encoding' : 'gzip, deflate, sdch'}
	cookies = dict(__client_id=client_id,_uid=uid)
	response = requests.post(url, cookies=cookies,headers=my_headers,data=data)
	return(response.content.decode("utf-8"))
# sendBenBen(content,cookies_client_id,cookise_uid)