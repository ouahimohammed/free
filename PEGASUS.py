B = '''[1;30m'''
R = '''[1;31m'''
G = '''[1;32m'''
Y = '''[1;33m'''
Bl = '''[1;34m'''
P = '''[1;35m'''
Z = '''[1;36m'''
W = '''[1;37m'''
OB = '''[40m'''
OR = '''[41m'''
OG = '''[42m'''
OY = '''[43m'''
OBl = '''[44m'''
OP = '''[45m'''
OC = '''[46m'''
OW = '''[47m'''

import datetime
import codecs
import random
import time
import socket
import threading
import select
import re
import requests
from datetime import datetime
global roomretst

def gen_squad(clisocks, packet: str):
        header = packet[0:62]
        lastpacket = packet[64:]
        squadcount = "04"

        NewSquadData = header + squadcount + lastpacket
        clisocks.send(bytes.fromhex(NewSquadData))
import requests

import re
import random
import codecs
def fadai_msg(mess, data, clin):
    data = data[12:22]
    api_url = f"https://fadai-long-message.vercel.app/api?id={data}&txt={mess}&code=FADAI7700ki"
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        packet = response.text
        clin.send(bytes.fromhex(packet.strip('"')))
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
import requests
def info(go):
    pack = "في فريق"
    api_url = f"https://send-info-fadai.vercel.app/api?id={pack}&lop={go}&code=FADAI7700ki"
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        final = response.text
        return final
    except:
        pass
def gen_msg4(packet, content):
        content = content.encode("utf-8")
        content = content.hex()

        header = packet[0:8]
        packetLength = packet[8:10]
        packetBody = packet[10:32]
        pyloadbodyLength = packet[32:34]
        pyloadbody2 = packet[34:62]
        pyloadlength = packet[62:64]

        pyloadtext= re.findall(r"{}(.*?)28".format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+64):]

        NewTextLength = (hex((int(f"0x{pyloadlength}", 16) - int(len(pyloadtext)//2) ) + int(len(content)//2))[2:])
        if len(NewTextLength) == 1:
                NewTextLength = "0"+str(NewTextLength)

        NewpaketLength = hex(((int(f"0x{packetLength}", 16) - int((len(pyloadtext))//2) ) ) + int(len(content)//2) )[2:]
        NewPyloadLength = hex(((int(f"0x{pyloadbodyLength}", 16) - int(len(pyloadtext)//2)))+ int(len(content)//2) )[2:]
        NewMsgPacket = header + NewpaketLength + packetBody + NewPyloadLength + pyloadbody2 + NewTextLength + content + pyloadTile
        return str(NewMsgPacket)
import requests
import json
import requests
import secrets

import secrets
import requests

def byte_comunety(key, data):
    api_url = f"https://byte-cmunety-rdp.vercel.app/api?key={key}&data={data}&code=FADAI771op"
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        packet = response.text
        return packet
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
def color():
    # List of top 50 colors without #
    top_colors = ['[ff4500]', '[ffd700]', '[32cd32]', '[87ceeb]', '[9370db]', '[ff69b4]', '[8a2be2]', '[00bfff]', '[1e90ff]', '[20b2aa]', 
'[00fa9a]', '[008000]', '[ffff00]', '[ff8c00]', '[dc143c]', '[ff6347]', '[ffa07a]', '[ffdab9]', '[cd853f]', '[d2691e]', 
'[bc8f8f]', '[f0e68c]', '[556b2f]', '[808000]', '[4682b4]', '[6a5acd]', '[7b68ee]', '[8b4513]', '[c71585]', '[4b0082]', 
'[b22222]', '[228b22]', '[8b008b]', '[483d8b]', '[556b2f]', '[800000]', '[008080]', '[000080]', '[800080]', '[808080]', 
'[a9a9a9]', '[d3d3d3]', '[f0f0f0]']
    # Select a random index using secrets
    random_index = secrets.randbelow(len(top_colors))
    random_color = top_colors[random_index]
    return random_color

import random
import secrets
def dance(id):
    # List of top 50 colors without #
    top_colors = [f"050000002008{id}100520162a1408{id}1084fbb8b1032a0608{id}", f"050000002008*100520162a1408{id}10a2fbb8b1032a0608{id}", f"050000002008{id}100520162a1408{id}10edbabbb1032a0608{id}", f"050000002008{id}100520162a1408{id}10d6c2bbb1032a0608{id}", f"050000002008{id}100520162a1408{id}109684bbb1032a0608{id}", f"050000002008{id}100520162a1408{id}109e84bbb1032a0608{id}", f"050000002008{id}100520162a1408{id}10ca9bbbb1032a0608{id}", f"050000002008{id}100520162a1408{id}10b9cabbb1032a0608{id}", f"050000002008{id}100520162a1408{id}108bfbb8b1032a0608{id}", f"050000002008{id}100520162a1408{id}10fffab8b1032a0608{id}", "050000002008{id}100520162a1408{id}10ff8bbbb1032a0608{id}"]
    # Select a random index using secrets
    random_index = secrets.randbelow(len(top_colors))
    random_color = top_colors[random_index]
    return random_color
    

def gen_msgv3(packet , replay):

        replay = replay.encode('utf-8')
        replay = replay.hex()


        hedar = packet[0:8]
        packetLength = packet[8:10] #
        paketBody = packet[10:32]
        pyloadbodyLength = packet[32:34]
        pyloadbody2= packet[34:60]

        pyloadlength = packet[60:62]
        pyloadtext= re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+62):]


        NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
        if len(NewTextLength) == 1:
                NewTextLength = "0"+str(NewTextLength)

        NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
        NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)))+ int(len(replay)//2) )[2:]

        finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile

        return str(finallyPacket)
def send_packt(cheack,packet):
    port = 39699
    host = "98.98.162.21"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        message = cheack + packet
        print(R)
        print(message)
        s.sendall(message.encode())
        print(Y)
        print(s.sendall(message.encode()))
        data = s.recv(1024)
        print(C)
        print(data)
        return data
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

def send_msg(sock, packet, content, delay:int):
        time.sleep(delay)
        try:
                sock.send(bytes.fromhex(gen_msg4(packet, content)))
               
                sock.send(bytes.fromhex(gen_msgv3(packet, content)))
        except Exception as e:
                ##print(e)
                pass
roomretst = False
gameplayed= 0
listt =[]
serversocket =None
remotesockett = None
clienttsocket =None
istarted = False
start =None
stop =b'\x03\x15\x00\x00\x00\x10\t\x1e\xb7N\xef9\xb7WN5\x96\x02\xb0g\x0c\xa8'
increase =False
socktion =None
req = False
SOCKS_VERSION = 5
packet =b''
full = False
import requests
def shorten_url(long_url):
    api_url = "https://cleanuri.com/api/v1/shorten"
    data = {"url": long_url}
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        return response.json()["result_url"]
    else:
        return None
import datetime
import requests
def getreg(Id):
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://shop2game.com",
        "Referer": "https://shop2game.com/app",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "x-datadome-clientid": "10BIK2pOeN3Cw42~iX48rEAd2OmRt6MZDJQsEeK5uMirIKyTLO2bV5Ku6~7pJl_3QOmDkJoSzDcAdCAC8J5WRG_fpqrU7crOEq0~_5oqbgJIuVFWkbuUPD~lUpzSweEa",
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.status_code == 200:
            return response.json()['region']
        else:
            return(f"ERROR")
    except:
        return("Server unknown ??")
import requests

def enc(id):
    api_url = f"https://api-ghost.vercel.app/FFcrypto/{id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch data. Status code:", response.status_code)

def Encrypt_ID(data):
    # تشفير بسيط: تحويل كل حرف إلى هيكس والعكس (يمكن تعديلها لتناسب احتياجاتك)
    return ''.join([hex(ord(c))[2:].zfill(2) for c in data])
def GenResponsMsg(Msg, Enc_Id):
    try:
        hexmsg = Msg.encode("UTF-8").hex()
        bunner = "902000" + "306"
        bunner = Encrypt_ID(bunner)
        print(f"Encrypted bunner: {bunner}")
        
        msg_lenth = len(Msg.encode("UTF-8").hex()) // 2
        msg_lenth = Encrypt(msg_lenth)
        print(f"Encrypted message length: {msg_lenth}")
        
        packet = f"089583bab21f10{Enc_Id}180222{msg_lenth}{hexmsg}28bed88eaa064a180a0b536f756c38473651325f3220c9013802420437d8a3365202656e6a04100118017200"
        payload_lenth = len(packet) // 2
        payload_lenth = Encrypt(payload_lenth)
        print(f"Encrypted payload length: {payload_lenth}")
        
        packet = f"080112{payload_lenth}089583bab21f10{Enc_Id}180222{msg_lenth}{hexmsg}28bed88eaa064a180a0b536f756c38473651325f3220c9013802420437d8a3365202656e6a04100118017200"
        encrypted_packet = encrypt_packet(packet)
        header_lenth = len(encrypted_packet) // 2
        header_lenth = dec_to_hex(header_lenth)
        print(f"Header length: {header_lenth}")
        
        if len(header_lenth) == 2:
            final_packet = "1215000000" + header_lenth + encrypted_packet
        elif len(header_lenth) == 3:
            final_packet = "121500000" + header_lenth + encrypted_packet
        elif len(header_lenth) == 4:
            final_packet = "12150000" + header_lenth + encrypted_packet
        elif len(header_lenth) == 5:
            final_packet = "1215000" + header_lenth + encrypted_packet
        else:
            raise ValueError("Header length is not within expected range.")
        
        return bytes.fromhex(final_packet).hex()
    
    except:
        return bytes.fromhex(final_packet).hex()
        
def getname(Id):    
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://shop2game.com",
        "Referer": "https://shop2game.com/app",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "x-datadome-clientid": "10BIK2pOeN3Cw42~iX48rEAd2OmRt6MZDJQsEeK5uMirIKyTLO2bV5Ku6~7pJl_3QOmDkJoSzDcAdCAC8J5WRG_fpqrU7crOEq0~_5oqbgJIuVFWkbuUPD~lUpzSweEa",
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.status_code == 200:
            return response.json()['nickname']
        else:
            return("ERROR")
    except:
        return("Name unknown??")
def get_status(Id):
    r= requests.get('https://ff.garena.com/api/antihack/check_banned?lang=en&uid={}'.format(Id)) 
    a = "0"
    try : 
        if  a in r.text :
            return("Account is Not ban")
        else: 
            return("Account is ban")
    except:
        return("Status unknown")
def fadai_ghosts(id1, id2, name):
#    id2 = enc(id2)
    api_url = f"https://fadai-ghosts-ingroup.vercel.app/api/?id={id1}&text={name}&rok={id2}"
    response = requests.get(api_url)
    if response.status_code == 200:
        clientC.send(bytes.fromhex(response.text))
    else:
        return "error"
def get_inc(id):
    accountid = id
    url = 'https://vrxx1337.pythonanywhere.com/?id={}'.format(accountid)
    response = requests.get(url)
    if response.status_code == 200:
        long_text = response.text
    else:
        return("8c8d99a21b")
    ap = 'idenc":'
    dp = '","'
    start_link2 = long_text.find(ap) + len(ap) + 1
    end_link2 = long_text.find(dp, start_link2)
    iud = long_text[start_link2:end_link2]
    return(iud)
import os
#while True:
print(R)
print(" ============================= ==============")

print(R, "============================= ==============")
print(R)
#    time.sleep(6)
 #   os.system("clear")
def gen_msgv2_clan(replay  , packet):
    replay  = replay.encode('utf-8')
    replay = replay.hex()
    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:64]
    if "googleusercontent" in str(bytes.fromhex(packet)):
        pyloadlength = packet[64:68]#
        pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+68):]
    elif "https" in str(bytes.fromhex(packet)) and "googleusercontent" not in str(bytes.fromhex(packet)):
        ##("-------------------------")
        
        pyloadlength = packet[64:68]#
        pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+68):]
        ##(bytes.fromhex(pyloadlength))
        # #(bytes.fromhex(pyloadTile))

        ##("-------------------------")

    else:
        pyloadlength = packet[64:66]#
        pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+66):]
    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)
    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int(len(pyloadtext)//2) ) - int(len(pyloadlength))) + int(len(replay)//2) + int(len(NewTextLength)))[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)) -int(len(pyloadlength)) )+ int(len(replay)//2) + int(len(NewTextLength)))[2:]
    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
    return finallyPacket
import re

def api_fadai_time(key):
    url = f"https://lam-silk.vercel.app/api?key={key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        if "يوم" in response.text:
            return response.text
        else:
            return "[e80212]الكود خطأ او مستعمل او منتهي الصلاحية"
    except requests.exceptions.RequestException as e:
        
        return None
def gen_msgv2(replay  , packet):
    replay  = replay.encode('utf-8')
    replay = replay.hex()
    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:60]
    pyloadlength = packet[60:62]#
    pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
    pyloadTile = packet[int(int(len(pyloadtext))+62):]
    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)
    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2))  )+ int(len(replay)//2) )[2:]
    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
    return finallyPacket
def inret():
    global hidd,packet1
    try:
        hidd.send(packet1)
    except:
        pass
def nret():
    global vispacket,visback
    try:
        visback.send(vispacket)
    except:
        pass
def sendi():
    global snv,dataC
    while True:
        if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 900:
            for i in range(400):
                snv.send(dataC)
                for k in range(1):
                    time.sleep(0.001)
            break
error = None
preventlag = False
sqlag = False
st = False
serversocket = None
clientsocket =None
op = None
pekto =None
inviteD=False
spampacket= b''
recordmode= False
sendpackt=False
back = False

spy = False
resasa =False
id_view = None
rolp = False
comand =True
cheak = False
mess = False
msgs =False
plu_b = None
SOCKS_VERSION = 5
packet = b''
packet1 = b''
invite = None
invite = None
returntoroom = False
invit_spam = False
roomp = False
number = 0
def roompass():
    global roomp
    if roomp == True:
        return True
    else:
        return False
import requests

def likes_plus(uid):
    url = f'https://likes-garena-fadai.vercel.app/api?uid={uid}&code=FADAI1900mp'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #print(data)
        
        # تحقق من وجود المفتاح 'response'
        if 'response' in data:
            response_data = data['response']
            uid = response_data.get('UID', 'خطأ')
            nickname = response_data.get('PlayerNickname', 'خطأ')
            likes_before = response_data.get('LikesbeforeCommand', 'خطأ')
            likes_after = response_data.get('LikesafterCommand', 'خطأ')

            return (f"تم إرسال 100 لايك بنحاح\n"
                    f"اسم لاعب: {nickname}\n"
                    f"الايكات قبل: {likes_before}\n"
                    f"الايكات الآن: {likes_after}")
        elif 'message' in data:
            if "already" in data['message']:
                return "لقد تم إضافة 100 لايك بالفعل لهذا الآيدي اليوم يمكنك زيادة مرة أخرى غدا"
        
        return "لا توجد معلومات حاول لاحقا"
    else:
        return "لا توجد معلومات حاول لاحقا"


def roomst():
    if roompass() == True:
        try:
            return str(number)
            ##print(str(number))
        except:
            return "FOXY BOT"
def xmodz(xmod):

      for k in range(90000):
          xmod.send(b'\x0e\x15\x00\x00\x00P\xd6\xd5\x19\x00+\xdc\xc6M\xe8\xa4,\x1a\xae\xdf\\:\xaa\xcf|\xe6\x94\xef\xbf\xc1\xf1\x1f\x02h\t\xb6%\xe7\x93aM\xd1?\xfa8\xee\xccUO\xf3 \xa6\x1b\x8a\xc6\x96\x99\xa8\xeb^\xda\xb7;9\xe9\xd9\x10zP\xd5\xe0\x83\xa2\xbc\x8c\x01\xfb\xadd\xdb\xcek\x85\x81\xcdP')
          for l in range(1):
              time.sleep(0.05)
def lagroom(cli,lg):
            for I in range(10):
                
                time.sleep(1)
                cli.send(b'\x0e\x15\x00\x00\x00\x10\x02\x92L\xf4)[\xa9xk^\xca\xf6\x8a\x80~w')
                time.sleep(1)
                cli.send(lg)
from time import sleep
global cmode
cmode = False
def crmode(value7):
    global cmode
    cmode = value7
    return cmode
def crazymode(keam,printkt1,printkt):
        for i in range(7):
        	time.sleep(1.5)
        	keam.send(printkt)
        	time.sleep(2)
        	keam.send(printkt1)
def randm(keam,printkt1,printkt):
        for i in range(3):
        	time.sleep(1)
        	keam.send(printkt)
        	time.sleep(1)
        	keam.send(printkt1)
#--------------
def timr_sleep():
     global cheak
     cheak = False
     time.sleep(2)
     cheak = True
def stoplg(rsend,leg,resocket,clsocket):
   preventlag = False
   for i in range(1):
      time.sleep(2)
      for h in range(1):
         rsend.send(b'\x0e\x15\x00\x00\x00\x10\x02\x92L\xf4)[\xa9xk^\xca\xf6\x8a\x80~w')
         for t in range(1):
            time.sleep(2)
            for k in range(1):
               rsend.send(leg)
import requests

def adjust_text_length(text, target_length=22, fill_char="00"):
    # إذا كان النص أطول من العدد المستهدف من الأحرف
    if len(text) > target_length:
        return text[:target_length]
    # إذا كان النص أقصر من العدد المستهدف من الأحرف
    elif len(text) < target_length:
        # نحتاج لإضافة "20" كملء للنص
        fill_length = target_length - len(text)
        # نجمع النص الأصلي مع النص المضاف
        return text + (fill_char * (fill_length // len(fill_char)))[:fill_length]
    # إذا كان النص بالفعل بطول العدد المستهدف من الأحرف
    else:
        return text
global spprspm
def spprspm(server,packet):
        while True:
            time.sleep(0.014)
            server.send(packet)
            if msgs == False:
                break

fivesq = False
def fivepe(value23):
    global fivesq
    fivesq = value23
    return fivesq




def runsnv():
    threading.Thread(target=sendi).start()

SOCKS_VERSION = 5


class Port:
    def __init__(self):
        self.username = "username"
        self.password = "password"
        self.packet = b''
        self.sendmode = 'client-0-'
        global connection
    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2   in set(methods):
            if 2 in set(methods):
                connection.sendall(bytes([SOCKS_VERSION, 2]))
            else:
                connection.sendall(bytes([SOCKS_VERSION, 0]))

        if not self.verify_credentials(connection,methods):
            return
        version, cmd, _, address_type = connection.recv(4)

        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
            name= socket.gethostname()

        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        port2 = port
        try:

                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                ##(" connect to {} \n \n \n ".format(address))
                bind_address = remote.getsockname()

                addr = int.from_bytes(socket.inet_aton(
                    bind_address[0]), 'big', signed=False)
                port = bind_address[1]

                reply = b''.join([
                    SOCKS_VERSION.to_bytes(1, 'big'),
                    int(0).to_bytes(1, 'big'),
                    int(0).to_bytes(1, 'big'),
                    int(1).to_bytes(1, 'big'),
                    addr.to_bytes(4, 'big'),
                    port.to_bytes(2, 'big')

            ])
        except Exception as e:

            reply = self.generate_failed_reply(address_type, 5)


        connection.sendall(reply)


        self.botdev(connection, remote,port2)

    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])

    def verify_credentials(self, connection,methods):

        if 2 in methods:

            version = ord(connection.recv(1))
            username_len = ord(connection.recv(1))
            username = connection.recv(username_len).decode('utf-8')
            password_len = ord(connection.recv(1))
            password = connection.recv(password_len).decode('utf-8')
         #   #(username,password)
            if username == self.username and password == self.password:
                response = bytes([version, 0])
                connection.sendall(response)
                return True
            response = bytes([version, 0])
            connection.sendall(response)

            return True

        else:
            version =1
            response = bytes([version, 0])
            connection.sendall(response)
            return True




    def get_available_methods(self, nmethods, connection):
        methods = []
        for i in range(nmethods):
            methods.append(ord(connection.recv(1)))
        return methods

    def runs(self, host, port):
        var =  0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()

        while True:
            var =var+1
            conn, addr = s.accept()
            running = False
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()
  
    def botdev(self, client, remote, port):
        global clientC
        global remoteC
        global clientM
#        host = '98.98.162.21'
#        port = 39699
#        clientC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        clientC.connect((host, port))
        global op
        global back
        global pekto
        global x
        global o
        global k
        o = True
        k = False
        x = False
        global b
        b = False
        global c
        c = False
        idinfo = True

        yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F"
        yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![18ffff]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
        yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [18ffff]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
        yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
        yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[18ffff]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[18ffff]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e"
        yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[18ffff]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[18ffff]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03'
        yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[18ffff]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[18ffff]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>"
        yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[18ffff]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[18ffff]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026'
        yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[18ffff]HEROSHIIMA1[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
        yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
        yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
        yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
        yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
        yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[18ffff]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03'
        yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
        yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
        yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
        yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
        yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
        yout21= b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
        yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
        yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
        yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
        yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
        yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
        yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
        yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[18ffff]BM\xe3\x85\xa4ABDOU_YT[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16"
        yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[18ffff]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[18ffff]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
        yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [18ffff]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[18ffff]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03'
        yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[18ffff]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03"
        yout32 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xe0\xe1\xdeu\x1a\x1a[18ffff]P1\xe3\x85\xa4Fahad[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xd0&\xd8\x01\xea\xd6\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xe3\x85\xa4\xef\xbc\xb0\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xa5\xef\xbc\xae\xef\xbc\xa9\xef\xbc\xb8\xc2\xb9\xf0\x01\x01\xf8\x01\x9e\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02*'
        yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[18ffff]@EL9YSAR[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
        yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[18ffff]STRONG\xe3\x85\xa4CRONA[18ffff]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01'
        yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[18ffff]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03'
        yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[18ffff]ZAIN_YT_500K[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02('
        yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([18ffff]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[18ffff]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03'
        yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([18ffff]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q'
        yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[18ffff]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03'
        yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03'
        yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[18ffff]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q'
        yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[18ffff]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[18ffff]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03'
        yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[18ffff]BT\xe3\x85\xa4BadroTV[18ffff]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!'
        yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01"
        yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[18ffff]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k'
        yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[18ffff]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[18ffff]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
        yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [18ffff]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[18ffff]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
        yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[18ffff]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
        yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
        yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
        yout51 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x028c8d99a21bn\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'

        yout_list = [yout1,yout2,yout3,yout4,yout5,yout6,yout7,yout8,yout9,yout10,yout11,yout12,yout14,yout15,yout16,yout17,yout18,yout19,yout20,yout21,yout22,yout23,yout24,yout25,yout26,yout27,yout28,yout29,yout30,yout31,yout32,yout33,yout34,yout35,yout36,yout37,yout38,yout39,yout40,yout41,yout42,yout43,yout44,yout45,yout46,yout47,yout48,yout49,yout50,yout51]
        global cmodeinfo
        cmodeinfo = True

        global cmodeloop
        cmodeloop = False
        
        global random
        random = False
        global full


        global exitpacket
        global enterpacket
        exitpacket = b''
        enterpacket = b''
        idinfo = True
        global visible_ret
        global fivesq
        kema = False
        activation = True
        global roba
        packet0300 = True
        roba = 1
        stat = True
        global viback
        viback = False
        # 5 in group5
        restartsock = False
        ########
        global startspammsg
        startspammsg = False

        global lg_room
        lg_room = False

        global spam_invs
        spam_invs = False

        global fivesq
        fivesq = False
        global opns
        opns = False
        global id_user
        id_user = None
        global increaseL
        increaseL = False

        global inv_ret
        inv_ret = False

        global visible_ret
        visible_ret = False

        global add_yout
        add_yout = False
        global msg1
        msg1 = False
        ########

        while True:
            ######################################
            #spam messages

            global spamsg
            def spamsg(value):
                global startspammsg
                startspammsg = value
                return startspammsg
		    
            # lag room

#            global lagroomsw
#            def foxy( self , data_join):
#                global back
#                while back==True:
#                	self.op.send(data_join)
#                	time.sleep(9999.0)

            #spam invs

            global spam_invitations
            def spam_invitations(value3):
                global spam_invs
                spam_invs = value3
                return spam_invs


            # 5 in group5



            # crazymode



            # Level ++
            global level_increase
            def level_increase(value6):
                global increaseL
                increaseL = value6
                return increaseL





            global youtubers
            def youtubers(value42):
                global add_yout
                add_yout = value42
                return add_yout
                


            ######################################
            r, w, e = select.select([client, remote], [], [])
            global start
            global full
            global hidd
            if client in r or remote in r:
                global serversocket
                global remotesockett
                global clientsockett
                if client in r:
                    global team
                    global teams
                    global solo
                    global packett1
                    global levelplus
                    global packett
                    global spyN
                    global spy
                    global visback
                    global vispacket
                    global dataC
                    global xspy
                    dataC = client.recv(999999)

                    #####
                    global hide
                    hide =False
                    global id_view
                    global rolp
                    global mess
                    global req
                    global id_b
                    global plusdata
                    global cheak
                    cheak = False
                    global comand
                    global resasa
                    global msgs
                    global masag
                    global remasag
                    global masss
                    global recordmode
                    global payloadteam
                    global teamp
                    global mac
                    global mood 
                    mood = False 
                    global mool
                    mool = False


#                    host = '98.98.162.21'
#                    port = 39699
#                    clientC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                    clientC.connect((host, port))

                    if '0e15' in dataC.hex()[0:4] and len(dataC.hex()) == 44:
                        exitpacket = dataC
                    if '0e15' in dataC.hex()[0:4] and len(dataC.hex()) > 80 and len(dataC.hex()) < 180:
                        enterpacket = dataC
                        room = remote
                    if '0515' in dataC.hex()[0:4]:
                        f=12
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141:
                        hide = True
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141 and opns == True:
  
                            id = id_user
                            dor = "050000002008*100520162a1408*1098fbb8b1032a0608*"
                            
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                            
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141:
                    	if mool ==True:
                            try:
                                for i in range(10):
                                    remasag.send(masag)
                                    time.sleep(2)
                            except:
                                pass
                    	if mood ==True:
                    	    cm = f"050000002008{mac}100520162a1408{mac}1098fbb8b1032a0608{mac}"
                    	    clientC.send(bytes.fromhex(cm))
                    	self.data_join=dataC
                    	packett = dataC
                    	teams = remote
                    	teamp = client
                    	xspy = dataS
                    	
                    if '0515' in dataC.hex()[0:4] and len(dataC.hex()) < 50:   #ENTER TO SQUAD
                       ##(dataC)
                       ##(dataC.hex())
                       ##(len(dataC.hex()))
                       self.data_back=dataC
                       packett1 = dataC
                       team = remote
                 
                
                       ##("ENTER TO SQUAD Def")
                    

                    if '0515' in dataC.hex()[0:4] and 700 < len(dataC.hex()) < 1100:
                       solo = dataC          
                       print(R)
                       
                    if msgs ==True:
                        if '1215' in dataC.hex()[0:4]:
                            for i in range(10):
                                remote.send(dataC)
                            global spprspm
                            b = threading.Thread(target=spprspm, args=(remote,dataC))
                            b.start()
                    #####
                    if port == 39698:
                            levelplus = remote
                            clientC = client
                            clientM = remote
                    if port == 39800:
                             remoteC = client
                  
                    if  "39699" in str(remote) :
                    	self.op = remote
                    if '0515' in dataC.hex()[0:4] or '23.90.158.22' in str(remote) :
                        op = remote
                    if remote.send(dataC) <= 0:
                        break
                if remote in r:

                    ######
                    global hidr
                    global cliee
                    global lag
                    global invit_spam
                    global id_adm
                    global newdataS
                    global newdataSofspam
                    global newdataSoffspam
                    global clieee
                    global backto
                    global actcode
                    global returntoroom
                    global newbackdataS
                    global getin
                    global spaminv
                    global spammsg
                    global preventlag
                    global sqlag
                    
                    global ingroup5
                    global group5
                    global invite
                    global roomp
                    global number
                    global acctive
                    global invtoroom
                    global msgact
                    global lagscript
                    global lagmsg
                    global stoplag
                    global stopmsg
                    global cpy
                    global back
                   
                    ######
                    global full
                    #####
                    global listt
                    global C
                    global istarted
                    global gameplayed
                    global packet
                    global socktion
                    global increase
                    global roomp
                    global roomretst
                    global number
                    global invtoroom
                    global invtoroompacket
                    global snv
                    global newdataS2
                    global packet1
                    dataS = remote.recv(999999)
                    if '0e00' in dataS.hex()[:4] and '0e15' in dataC.hex()[:4] and preventlag == True:
                            pass
                            #print()
                    else:

                        if increaseL == True:
                            threading.Thread(target=xmodz,args=(levelplus,)).start()
                            increaseL = False

                        if full == True:               
                            ##("Send info")                    
                            
                            full = False

                        if '0e15' in dataC.hex()[:4] and returntoroom ==True:
                            remote.send(lag)
                            returntoroom =False
                            clieee = remote
                            st =False
                        if '0e15' in dataC.hex()[:4]:
                            remotesockett = remote
                            clientsockett = client
                        if '0e15' in dataC.hex()[0:4] and 75 < len(dataC.hex()) < 180:
                            ##(dataC)
                            ##(len(dataC.hex()))
                            clieee = remote
                            lag = dataC
  
                        if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >=900 and invit_spam==True:
                            for i in range(30):
                                remote.send(dataC)
                                print("send....")
                        if lg_room == True:
                            preventlag =True
                            threading.Thread(target=lagroom,args=(clieee,lag)).start()
                            restartsock = True
                        if lg_room == False:
                            preventlag = False
                            if restartsock == True:
                                try:
                                    remotesockett.close()
                                    clientsockett.close()
                                except:
                                    pass
                                restartsock = False

                        try:
                            if '1200' in dataS.hex()[0:4] and b'/info' in dataS and comand == True: #/back
                                backto = client
                                newbackdataS = dataS.hex()
                                full = True
                        except:
                            pass
                        if cmodeloop==True:
                            threading.Thread(target=crazymode,args=(team,packett1,packett)).start()
                        if cmode == False:
                            cmodeloop = False
                        if  port == 39699:
                            invite = client
                            snv = remote
                        if startspammsg == True:     #/spam
                           recordmode = True
                        if startspammsg == False: #/f
                            statues = False
                        if '0e15' in dataC.hex()[:4]:
                           print(Z)
                           
                        if '0e00' in dataS.hex()[0:4]:
                           print(dataC.hex())
                           for i in range(10):
                               pattern = fr"x0{str(i)}(\d+)Z"
                               match = re.search(pattern, str(dataS))
                               if match:
                                   number = match.group(1)
                                   global romcode
                                   romcode = number
                                   ##print(romcode)
                                   ##print("go")
                                   break
                           if match:
                               pass
                           else:
                               if "OPENATTRIBUTESEXT" in str(dataS):
                                    pass

                        if b"/join" in dataS and comand == True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'/join(\d+)'
                            match = re.search(pattern, text)
                            name = match.group(1)
                            id_admin = dataS.hex()[12:22]
                            my_id = "84e9a2d606"
                            #دخول اي فريق
                            if len(id_admin) > 8:
                                hex_name = name.encode('utf-8').hex()
                                hex_name = adjust_text_length(hex_name)
                                clientC.send(bytes.fromhex(f'05000003ff08{my_id}100520062af20708{id_admin}12024d451801200332cc0408{id_admin}12135b6564303930395d50454741e2808f535553201a024d4520a6e38baa0628443087cbd13038324218e0f38766e796a3618994e660f39ae061e5b7d064bfb8ce64480150ce01588e0c60f5d7d0ad0368c2dc8dae037a05d7d0cab00382012b08b3daf1eb041211d8b2d98ad988d98ad986d983d983e29cbf180620b687d4f0042a0808c49d85f30410038801ed89c5b00392010b0107090a0b1216191a20239801cd01a00111a80185fff5b103c00101c80101d001bace89af03e80101880203920207c20500a606e532aa020a080110c03e18f0602002aa0205080210b232aa0205080310e432aa020a080f10918a0118a09c01aa0205081710e750aa0205081810b768aa0205081a10da74aa0206081b10918a01aa0206081c10958c01aa02050820108b79aa0205082110eb7aaa0205082210a275aa0206082310dc8701aa0205082b10f476aa0205083110f476aa0206083910918a01aa0206083d10918a01aa0206084110918a01aa0205084910e432aa0205084d10e432aa0206083410918a01aa0205082810e432aa0205082910e432c2022112041a0201041a090848120501040506071a0508501201631a0508511201652200ea02520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3237373631373532363237343633352f706963747572653f77696474683d313630266865696768743d31363010011801f202090887cab5ee0110870a8a030808021003180528019203009803f3e78ea30ba20315e298afd986d8a7d8acd988d986d98ae298afe29c9432d00208{my_id}120b{hex_name}1a024d452096ed8baa0628043089cbd13038324214fa96e660b599a361c19de061aab9ce64abb9ce64480150c90158e80792010601090a1219209801c901c00101c80101e80101880204920206ee07ce010000aa0208080110ff34188064aa020b080f10fd3218b086012001aa0205080210e432aa0205081810fd32aa0205081a10fd32aa0205081c10fd32aa0205082010fd32aa0205082210fd32aa0205082110fd32aa0205081710e432aa0205082310fd32aa0205082b10fd32aa0205083110fd32aa0205083910fd32aa0205083d10fd32aa0205084110fd32aa0205084910d836aa0205084d10e432aa0205081b10fd32aa0205083410fd32aa0205082810e432aa0205082910e432c2022112041a0201041a090848120501040506071a0508501201631a0508511201652200ea0204100118018a03009203003a0101400150016801721e313639383838363035353130343733333939355f6a67386c37333431646688018090aefec3978fef17a20100b001e001ea010449444331'))
                        if b"/add" in dataS and comand == True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'/add(\d+)'
                            match = re.search(pattern, text)
                            number = match.group(1)
                            my_id = dataS.hex()[12:22]
                            id_admin = "84e9a2d606"
                            #دخول اي فريق
                            if len(id_admin) > 8:
                                name = getname(number)
                                hex_name = name.encode('utf-8').hex()
                                hex_name = adjust_text_length(hex_name)
                                clientC.send(bytes.fromhex(f'05000003ff08{my_id}100520062af20708{id_admin}12024d451801200332cc0408{id_admin}12135b6564303930395d50454741e2808f535553201a024d4520a6e38baa0628443087cbd13038324218e0f38766e796a3618994e660f39ae061e5b7d064bfb8ce64480150ce01588e0c60f5d7d0ad0368c2dc8dae037a05d7d0cab00382012b08b3daf1eb041211d8b2d98ad988d98ad986d983d983e29cbf180620b687d4f0042a0808c49d85f30410038801ed89c5b00392010b0107090a0b1216191a20239801cd01a00111a80185fff5b103c00101c80101d001bace89af03e80101880203920207c20500a606e532aa020a080110c03e18f0602002aa0205080210b232aa0205080310e432aa020a080f10918a0118a09c01aa0205081710e750aa0205081810b768aa0205081a10da74aa0206081b10918a01aa0206081c10958c01aa02050820108b79aa0205082110eb7aaa0205082210a275aa0206082310dc8701aa0205082b10f476aa0205083110f476aa0206083910918a01aa0206083d10918a01aa0206084110918a01aa0205084910e432aa0205084d10e432aa0206083410918a01aa0205082810e432aa0205082910e432c2022112041a0201041a090848120501040506071a0508501201631a0508511201652200ea02520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3237373631373532363237343633352f706963747572653f77696474683d313630266865696768743d31363010011801f202090887cab5ee0110870a8a030808021003180528019203009803f3e78ea30ba20315e298afd986d8a7d8acd988d986d98ae298afe29c9432d00208{my_id}120b{hex_name}1a024d452096ed8baa0628043089cbd13038324214fa96e660b599a361c19de061aab9ce64abb9ce64480150c90158e80792010601090a1219209801c901c00101c80101e80101880204920206ee07ce010000aa0208080110ff34188064aa020b080f10fd3218b086012001aa0205080210e432aa0205081810fd32aa0205081a10fd32aa0205081c10fd32aa0205082010fd32aa0205082210fd32aa0205082110fd32aa0205081710e432aa0205082310fd32aa0205082b10fd32aa0205083110fd32aa0205083910fd32aa0205083d10fd32aa0205084110fd32aa0205084910d836aa0205084d10e432aa0205081b10fd32aa0205083410fd32aa0205082810e432aa0205082910e432c2022112041a0201041a090848120501040506071a0508501201631a0508511201652200ea0204100118018a03009203003a0101400150016801721e313639383838363035353130343733333939355f6a67386c37333431646688018090aefec3978fef17a20100b001e001ea010449444331'))
                                
                        if b"@ADD" in dataS and comand == True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'@ADD(\d+)'
                            match = re.search(pattern, text)
                            number = match.group(1)
                            id_add = dataS.hex()[12:22]
                            id_admin = "84e9a2d606"
                            #دخول اي فريق
                            if len(id_admin) > 8:
                                name = getname(number)
                                hex_name = name.encode('utf-8').hex()
                                hex_name = adjust_text_length(hex_name)
                                clientC.send(bytes.fromhex(f'060000006808d4d7faba1d100620022a5c08{id_add}1a1b5b4646303030305d5b625de385a4424f542b2b5b3030464646465d32024d45404db00113b801a528d801d4d8d0ad03e00101b801e807f00101f8019a018002fd98a8dd03900201d0020cd8022ee002b2e9f7b103'))
                                
                                
                                
                        if "0515" in dataC.hex()[0:4] and 1400 > len(dataC.hex()) >= 900:
                            visback = remote
                            vispacket = dataC
                        if b"PEGS-MA91-A7QK-82QL" in dataS:
                            id = dataS.hex()[12:22]
                            mack = api_fadai_time(id)
                            if "fff64d" in mack:
                                comand = True
                                fadai_msg(f"{mack}", dataS.hex(), client)
                            else:
                                comand = False
                                fadai_msg(f"{mack}", dataS.hex(), client)
                        if b"/msg" in dataS and comand ==True:
                            for i in range (20):
                                time.sleep(1.5)
                                threading.Thread(target=send_msg, args=(client, dataS.hex(), "[cُ][bَ][00ff00ً]تطردني تندم لاتعبت معي", 0.2)).start()
                                time.sleep(1.5)
                                threading.Thread(target=send_msg, args=(client, dataS.hex(), "[cُ][bَ][ff0000ً]تطردني تندم لاتعبت معي", 0.2)).start()
                                time.sleep(1.5)
                                threading.Thread(target=send_msg, args=(client, dataS.hex(), "[cُ][bَ][00ffffَ]تطردني تندم لاتعبت معي", 0.2)).start()
                        if b"@/5s" in dataS and comand == True:
                            fadai_msg(f"""[b][c][ffe75c]تم التفعيل""", dataS.hex(), client)
                            id = dataS.hex()[12:22]
                            clientC.send(bytes.fromhex(f"05000001ff08{id}1005203a2af20308{id}12024d451801200432f70208{id}1209424c52585f4d6f642b1a024d4520d78aa5b40628023085cbd1303832421880c38566fa96e660c19de061d998a36180a89763aab9ce64480150c90158e80792010801090a12191a1e209801c901c00101e801018802039202029603aa0208080110e43218807daa0207080f10e4322001aa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710e432aa0205082310e432aa0205082b10e432aa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810e432aa0205082910e432c2022812041a0201041a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a03009203009803b7919db30ba20319c2b27854e19687e197a95fe191ade192aae197a95945e19687e20301523a011a403e50056801721e313732303237323231313638373535353930315f736f3278687a61366e347801820103303b30880180e0aecdacceba8e19a20100b00114ea010449444332fa011e313732303237323231313638373535383330335f71356f79736b3934716d"))

                        if b"@FDPL" in dataS and comand == True:
                            invit_spam =True
                        if b"/invi" in dataS and comand == True:
                            fadai_msg(f"""[b][c][ffe75c]تم التفعيل""", dataS.hex(), client)
                            invit_spam =True
                        if b"/info" in dataS and comand ==True:
                        	fadai_msg("[b][c][00ffff]جاري إستدعاء معلومات\n[0000FF]تنظيم معلومة \n[FF00FF]انتضار المتهم....", dataS.hex(), client)
                        	inf = info(dataS.hex())
                        	fadai_msg(f"{inf}", dataS.hex(), client)
                        	req = True
                        if req == True and "1200" in dataS.hex():
                            print("yep")
                            print(plu_b)
                            if plu_b in dataS.hex():
                               #print("yesssss")
                               fadai_plus(plusdata, dataS.hex(), client, id_b)
                               req = False
                            
                        if b'/spy' in dataS and comand ==True:
                            time.sleep(2)
                            clientC.send(xspy)
                        if b'/back' in dataS and comand ==True:
                            teams.send(packett)
                        if b"@FDRM" in dataS and comand == True:
                           try:
                           	threading.Thread(target=randm,args=(team,packett1,packett)).start()
                           except:
                           	pass
                        if b"/room" in dataS and comand ==True:
                        	try:
                        	    threading.Thread(target=send_msg, args=(client, dataS.hex(), f"""[b][c][F7FE2E]Room password :""", 0.31)).start()
                        	    threading.Thread(target=send_msg, args=(client, dataS.hex(), f"""[b][c][66FF00]{romcode}""", 0.31)).start()
                        	    threading.Thread(target=send_msg, args=(client, dataS.hex(), f"""[b][c][FF00FF]Foxy[00FFFF]bot Premium""", 0.31)).start()
                        	except:
                        		threading.Thread(target=send_msg, args=(client, dataS.hex(), f"""ERROR !""", 0.31)).start()
                        if b"/kick" in dataS and comand == True:
                            threading.Thread(target=lagroom,args=(clieee,lag)).start()

                        if b"/yout" in dataS and comand ==True:
                            add_yout =True
                        if b"@FT1" in dataS and comand ==True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10fffab8b1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                        if b"@FT2" in dataS and comand == True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10ff8bbbb1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                        if b"@FT3" in dataS and comand == True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*1095fbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                        if b"@FT4" in dataS and comand == True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*108bfbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                        if b"@FT5" in dataS and comand == True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10edbabbb1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                        if b"@FT6" in dataS and comand == True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10a2fbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))
                        if b"@FT7" in dataS and comand == True:
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*1084fbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            clientC.send(bytes.fromhex(raks))

                        if '0e00' in dataS.hex()[0:4] and roomretst == True and "http" in str(dataS):

                            invtoroom = client
                            invtoroompacket = dataS
                        try:
                            pass   
                        except:
                            pass
                        if add_yout == True:
                            add_yout = False
                            from time import sleep
                            try:
                                for h in yout_list:
                                    clientC.send(h)
                                    sleep(0.2)
                            except:
                                pass
                        if b"/me" in dataS and comand ==True:
                            number = dataS.hex()[12:22]
                            dan = dance(number)
                            fadai_msg(f"""[b][c]{color()}تم التفعيل""", dataS.hex(), client)
                            for i in range(10):
                                time.sleep(1.5)
                                clientC.send(bytes.fromhex(dan))
                        if b"/dance" in dataS and comand ==True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'/dance(\d+)'
                            match = re.search(pattern, text)
                            number = match.group(1)
                            number = enc(number)
                            dan = dance(number)
                            fadai_msg(f"""[b][c]{color()}تم التفعيل""", dataS.hex(), client)
                            clientC.send(bytes.fromhex(dan))
                        if b"/dg" in dataS and comand ==True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'/dg(\d+)'
                            match = re.search(pattern, text)
                            number = match.group(1)
                            number = enc(number)
                            dc = dance(number)
                            fadai_msg(f"""[b][c]{color()}تم التفعيل""", dataS.hex(), client)
                            for i in range(20):
                                time.sleep(0.5)
                                clientC.send(bytes.fromhex(dc))
                        if b"/ds" in dataS and comand ==True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'/ds(\d+)'
                            match = re.search(pattern, text)
                            number = match.group(1)
                            number = enc(number)
                            fadai_msg(f"""[b][c]{color()}تم التفعيل""", dataS.hex(), client)
                            for i in range(20):
                                time.sleep(0.5)
                                clientC.send(bytes.fromhex(dance(number)))
                        if b"/emotes" in dataS and comand ==True:

                            number = dataS.hex()[12:22]

                            fadai_msg(f"""[b][c]{color()}تم التفعيل""", dataS.hex(), client)
                            for i in range(20):
                                time.sleep(0.5)
                                clientC.send(bytes.fromhex(dance(number)))
                        if b"@FME" in dataS and comand ==True:

                            number = dataS.hex()[12:22]
                            fadai_msg(f"""[b][c]{color()}تم التفعيل""", dataS.hex(), client)
                            time.sleep(1)
                            clientC.send(bytes.fromhex(dance(number)))
                        if b"@FLK" in dataS and comand ==True:
                            text = str(bytes.fromhex(dataS.hex()))
                            pattern = r'@FLK(\d+)'
                            match = re.search(pattern, text)
                            number = match.group(1)
                            like = likes_plus(number)
                            fadai_msg(f"""[b][c]{color()}{like}""", dataS.hex(), client)
                        if b'@FCN' in dataS and comand ==True:
                            fadai_msg(f"""[b][c][ffe75c]تم التفعيل""", dataS.hex(), client)
                            id = dataS.hex()[12:22]
                            clientC.send(bytes.fromhex(f"080000001308{id}100820022a0708a6b10318fa01"))
                        if b'/dis' in dataS and comand ==True:
                            fadai_msg(f"""[b][c][ffe75c]تم التفعيل""", dataS.hex(), client)
                            id = dataS.hex()[12:22]
                            clientC.send(bytes.fromhex(f"080000001308{id}100820022a0708a6b10318fa01"))
                        if b'@FAL' in dataS and comand ==True:
                            id = dataS.hex()[12:22]
                            clientC.send(bytes.fromhex(f"050000002008{id}100520162a1408{id}1098fbb8b1032a0608{id}"))

                        if b"@FAN" in dataS and comand ==True:
                            text = str(dataS)
                            pattern = r'@FAN(\d+)'
                            match = re.search(pattern, text)
                            masss = match.group(1)
                            print(masss)
                            fadai_msg(f"""[b][c][f75cbe]تم تغيير شكل رسالتك """, dataS.hex(), client)
                            fadai_msg(f"""{color()}×_×{masss}""", dataS.hex(), client)

                        if b'/spam' in dataS and comand ==True:
                            text = str(dataS)
                            pattern = r'@/spam(\d+)'
                            match = re.search(pattern, text)
                            key = match.group(1)
                            fadai_msg(f"""[b][c]تم إضافةالفريق للمقبرة
[00ffff]{key}
\n
[f21344]لقد بدء التعديب 
[eff213][نصف ساعة] 
 """, dataS.hex(), client)
                            time.sleep(2)
                            client.send(bytes.fromhex(byte_comunety(key, dataS.hex())))
                            client.send(bytes.fromhex(byte_comunety(key, dataS.hex())))
                            client.send(bytes.fromhex(byte_comunety(key, dataS.hex())))
                            time.sleep(2)
                            

                            while True:
                                time.sleep(0.1)
                                add_yout = True
                                client.send(bytes.fromhex(byte_comunety(key, dataS.hex())))
                                

                        if b'@FRK' in dataS and comand ==True:
                            mood = True
                            mac = dataS.hex()[12:22]
                            fadai_msg(f"""[b][c][ffe75c]تم التفعيل""", dataS.hex(), client)
                        if b'@FMS' in dataS and comand ==True:
                            fadai_msg(f"""[b][c]أدخل للقائمة المهتم بها واجعلها ضمن قائمتك[00ffff]

اسلحة   7319471756
فخمة   9691989441
نادرة    9719822328
رقصات 6588980942
 """, dataS.hex(), client)

                        if b'/help' in dataS:
                            fadai_msg(f"""[b][c][1df055]أهلا بك في 

[d33de0]Foxybot Permian
[749cf7]نحن سعيدون لإستقبالك هنا ستستفاد من مجموعة من خدمات ذكية والمميزة

[f75cbe]ميزات :
 """, dataS.hex(), client)
                            fadai_msg(f"""[b][c] الاختراق :


مقبرة رسائل (/spam)
5 فريق (/5s)
معلومات الجهاز (/info)
سبام دعوات (/invi) """, dataS.hex(), client)
                            fadai_msg(f"""[b][c]متعة :[ff61f7]

عدم طرد رسالة (/msg)
يتيوبرز اصدقاء (/yout)
عرض كود روم (/room)
منع الطرد روم (/kick)
تصفير جواهر (/dis)
رجوع لسكواد (/back)
""", dataS.hex(), client)
                            fadai_msg(f"""[b][c]إبهار :[f5f120]

رقص لاعب (/dance+id)
سبام رقص لاعب (/ds+id)
سبام رقص واحدة سكواد (/dg+id)
سبام رقصاتك عشوائي (/emotes)
سبام رقصاتك واحدة (/me)
""", dataS.hex(), client)
                           

                            if comand == True:
                                fadai_msg(f"""[b][c]كود VIP :[eff213]تم تفعيل""", dataS.hex(), client)
                            if comand == False:
                                fadai_msg(f"""[b][c]كود VIP :[f21344]غير مفعل""", dataS.hex(), client)
                        if client.send(dataS) <= 0:
                            break
    def foxy( self , data_join):
        global back
        while back==True:
            self.op.send(data_join)
            time.sleep(9999.0)        


# Start the combined server
Port().runs('127.0.0.1',3000)