import re, requests, os, threading, sys
from bs4 import BeautifulSoup

url = "https://www.dominos.bg/stores"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
store = sys.argv[1] if len(sys.argv) > 1 else 'Студентски град'
interval = 30 # seconds

def check_open():
    # reschedule the event
    threading.Timer(interval, check_open).start()

    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    regex = re.compile(r'.*%s.*' % store, re.IGNORECASE)
    img = html.find('h3', text=regex).parent.img

    if 'open' in img['src'].lower():
        print('\a')
        os.system('notify-send "Dominos are opeeeeen!"')

if __name__ == '__main__':
    check_open()
