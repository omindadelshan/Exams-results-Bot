from telethon import TelegramClient, events
import json
import requests


APP_ID=3964155 #my.telegram.org
APP_HASH='95136f46ae1425c4272596ce27543e99' #my.telegram.org
BOTT='1931650651:AAHksSqz-nijtj9HbKhv8yjqKkIsgU6PZ64'#@botfather


bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOTT)


def stat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://telegra.ph/file/e72876540a3af9e382f43.jpg",
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
    jsondata = json.loads(r.text)
    alexamination    = str(jsondata['examination'])
    alyear           = str(jsondata['year'])
    alname           = str(jsondata['name'])
    alindex          = str(jsondata['indexNo'])
    alnic            = str(jsondata['nic'])
    aldrank          = str(jsondata['districtRank'])
    alirank          = str(jsondata['islandRank'])
    alzscore         = str(jsondata['zScore'])
    alstream         = str(jsondata['stream'])
    alsyllabus       = str(jsondata['studentInfo'][2]['value'])
    sub1name         = str(jsondata['subjectResults'][0]['subjectName'])
    sub1result       = str(jsondata['subjectResults'][0]['subjectResult'])
    sub2name         = str(jsondata['subjectResults'][1]['subjectName'])
    sub2result       = str(jsondata['subjectResults'][1]['subjectResult'])
    sub3name         = str(jsondata['subjectResults'][2]['subjectName'])
    sub3result       = str(jsondata['subjectResults'][2]['subjectResult'])
    sub4name         = str(jsondata['subjectResults'][3]['subjectName'])
    sub4result       = str(jsondata['subjectResults'][3]['subjectResult'])
    sub5name         = str(jsondata['subjectResults'][4]['subjectName'])
    sub5result       = str(jsondata['subjectResults'][4]['subjectResult'])

    textt = str(

        '<b>G.C.E (A/L) Examination</b>' + '\n' + '\n' + '<b>' + 'Examination' + '</b>' + alexamination + '\n' + 
        '<b>' + 'Year' + '</b>' + alyear + '\n' + '<b>' + 'Index No.' + '</b>' + alindex + '\n' +
        '<b>' + 'Name' + '</b>' + alname + '\n' + '<b>' + 'NIC' + '</b>' + alnic + '\n' + 
        '<b>' + 'District Rank' + '</b>' + aldrank + '\n' + '<b>' + 'Island Rank' + '</b>' + alirank + '\n' +
        '<b>' + 'Z Score' + '</b>' + alzscore + '\n' +  '<b>' + 'Stream' + '</b>' + alstream + 
        '<b>' + 'Syllabus' + '</b>' + alsyllabus + '\n' + '\n' + 
        '<b>' + 'Results' + '</b>' +  '\n' + '\n' + '<b>' + sub1name + '</b>' + sub1result + '\n' + 
        '<b>' + sub2name + '</b>' + sub2result + '\n' + '<b>' + sub3name + '</b>' + sub3result + '\n' + 
        '<b>' + sub4name + '</b>' + sub4result + '\n' + '<b>' + sub5name + '</b>' + sub5result + '\n' + 
        '✅ All the Data Verified by the Government' + '\n' +'~ @UvinduBro 🇱🇰 ~')

    return textt

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    stat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/al {ALID}'))
async def AL(event):
    await event.respond(Al(),parse_mode='html')
    raise events.StopPropagation

def main():
    """Start the bot. \n \n ~ @UvinduBro"""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
