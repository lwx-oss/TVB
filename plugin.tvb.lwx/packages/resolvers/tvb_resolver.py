import requests

def getTokenizedLink(ipAddress):
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://news.tvb.com/live/inews?is_hd',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('token', 'http://token.tvb.com/stream/live/hls/mobilehd_news_windows1.smil?app=news&feed&client_ip={}'.format(ipAddress)),
    )

    response = requests.get('http://news.tvb.com/ajax_call/getVideo.php', headers=headers, params=params, verify=False)

    jsonResp = response.json()
    return jsonResp['url']