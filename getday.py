# -*- coding: utf8 -*-
import json
import requests

# 填入glados账号对应cookie
cookie = '_ga=GA1.2.210030062.1649495814; __stripe_mid=b26a1675-6450-47a1-adf6-37d5f7712d503519e1; ' \
         '_gid=GA1.2.1171778301.1654863376; _gat_gtag_UA_104464600_2=1; ' \
         'koa:sess=eyJ1c2VySWQiOjk3NTA4LCJfZXhwaXJlIjoxNjgwODQ5ODY4OTY5LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; ' \
         'koa:sess.sig=4egFvMtShDRNiXTJ0JfYOYoNFJg '

referer = 'https://glados.rocks/console/checkin'


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                "Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39 "
    payload = {
        'token': 'glados.network'
    }
    checkin = requests.post(url,
                            headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent,
                                     'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
    state = requests.get(url2,
                         headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
    print(checkin.text)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']

        time = time.split('.')[0]
        print(time + "天后过期")
    #     if sever == 'on':
    # requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + mess + '，you have ' + time + ' days left')
    # else:
    #     requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
