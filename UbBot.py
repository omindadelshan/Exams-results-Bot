from telethon import TelegramClient, events
import json
import requests


APP_ID=3964155 #my.telegram.org
APP_HASH='95136f46ae1425c4272596ce27543e99' #my.telegram.org
BOTT=''#@botfather


bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOTT)


def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "URL Here",
    "caption": "Hello ! \n I'm Doenets.lk Bot \n\n What does I Know \n\n • G.C.E. (A/L) EXAMINATION - 2020 \n • G.C.E. (O/L) EXAMINATION (After Rescrutiny) - 2019 \n • GRADE 5 SCHOLARSHIP EXAMINATION (AFTER APPEALS) - 2020 \n\n ~ @Uvindu_Bro 🇱🇰 ",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": "➕ Add me to your Group",
                    "url": "https://t.me/DonentsLKBot?startgroup=new"
                }, 
                {
                    "text": "🔊 Channel",
                    "url": "https://t.me/UvinduBro"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)


def Al():
    r = requests.get('https://www.doenets.lk/result/service/AlResult/{ALID}')