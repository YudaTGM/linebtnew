# -*- coding: utf-8 -*-
from DEKSTOPWIN import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
import time, random, sys, json, codecs,  threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz

botStart = time.time()

#client = LineClient()
client = LineClient(authToken="Ep8N1xDxkPuKX5JwerOf.1xIRKYKgYZl1yKjTdP8yhW.m3SJ06mxBEQRGDDAPB5rXbYpAYQyNbEFWMdvWJhz/jM=")
client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = LinePoll(client)
clientMID = client.profile.mid

contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#==============================================================================#
settings = {
    "autoAdd":True,
    "autoJoin":True,
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus
admin=["u1d86967da5fb13fad2bc422a51b963ce"]
#==============================================================================#

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = client.getProfile().mid
    if myid in nm:    
        nm.remove(myid)
    for mm in nm:
        akh = akh + 6
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 7
        akh = akh + 1
        bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
    try:
        client.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        print(error)
#==============================================================================#
while True:
    try:
        ops=clientPoll.singleTrace(count=50)
        
        for op in ops:
            if op.type == 5:
                if settings["autoAdd"] == True: 
                    client.findAndAddContactsByMid(op.param1)
                    xname = client.getContact(op.param1).displayName
                    client.sendMessage(op.param1, "Halo " + xname + " boleh minta bantuan subscribe YouTube.com/yudathegoldmine")
            if op.type == 13:
                print ("[NOTIFIED_INVITE_INTO_GROUP]")
                if clientMID in op.param3:
                    G = client.getGroup(op.param1)
                    if settings["autoJoin"] == True:
                        client.acceptGroupInvitation(op.param1)
                    else:
                        pass              
            if op.type == 26:
                print ("[ 26 ] READ MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'kcpt':
                                start = time.time()
                                client.sendMessage(receiver, "Tunggu sebentar")
                                elapsed_time = time.time() - start
                                client.sendMessage(receiver, "%sdetik" % (elapsed_time))
                            elif text.lower() == 'restart':
                                client.sendMessage(msg.to, "Bot Program has been restarted")
                                restartBot()
#----------------------------------------------------------------------------------------
                            elif "Add all" in msg.text:
                                ap = client.getGroups([msg.to])
                                semua = [contact.mid for contact in ap[0].members]
                                nya = ap[0].members
                                for a in nya:
                                    Mi_d = str(a.mid)
                                    client.findAndAddContactsByMid(Mi_d)
                            elif msg.text in ["Gurl"]:
                                if msg.toType == 2:
                                    x = client.getGroup(msg.to)
                                    if x.preventJoinByTicket == True:
                                        x.preventJoinByTicket = False
                                        client.updateGroup(x)
                                        gurl = client.reissueGroupTicket(msg.to)
                                        client.sendText(msg.to,"line://ti/g/" + gurl)
                                    else:
                                            if wait["lang"] == "JP":
                                                client.sendText(msg.to,"Can't be used outside the group")
                                            else:
                                                client.sendText(msg.to,"Not for use less than group")
                            elif "Group bc " in msg.text:
                                bctext = msg.text.replace("Group bc ", "")
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    client.sendText(manusia, (bctext))
                            elif "CloneeGc " in msg.text:
                                gName = msg.text.replace("CloneeGc ","")
                                ap = client.getGroups([msg.to])
                                semua = [contact.mid for contact in ap[0].members]
                                client.createGroup(gName, semua)
                            elif "Pict group " in msg.text:
                                saya = msg.text.replace('Pict group ','')
                                gid = client.getGroupIdsJoined()
                                for i in gid:
                                    h = client.getGroup(i).name
                                    gna = client.getGroup(i)
                                    if h == saya:
                                        client.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                            elif text.lower() == 'anime':
                                si = ("1","2","3","4","5","6","7","8","9","0")
                                ie = ("1","2","3","4","5","6","7","8","9","0")
                                bi = ("01","02","00")
                                bs = random.choice(bi)
                                io = random.choice(ie)
                                ss = random.choice(si)
                                bis = bs + io + ss
                                oew = "gan/" + bis + ".png"
                                client.sendImage(msg.to, oew)
#-------------------------------------------------
                            elif "bicara id " in msg.text:
                                say = msg.text.replace("bicara id ","")
                                lang = 'id'
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(msg.to,"hasil.mp3")
#------------------------------------------------
                            elif "bicara en " in msg.text:
                                say = msg.text.replace("bicara en ","")
                                lang = 'en'
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(msg.to,"hasil.mp3")
#--------------------------------------------------------
                            elif 'carilagu ' in msg.text.lower():
                                try:
                                    songname = msg.text.lower().replace('carilagu ','')
                                    params = {'songname': songname}
                                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    for song in data:
                                        hasil = 'This is Your Music\n'
                                        hasil += 'Judul : ' + song[0]
                                        hasil += '\nDurasi : ' + song[1]
                                        hasil += '\nLink Download : ' + song[4]
                                        client.sendText(msg.to, hasil)
                                        client.sendText(msg.to, "Please Wait for audio...")
                                        client.sendAudioWithURL(msg.to, song[4])
                                except Exception as njer:
                                    client.sendText(msg.to, str(njer))
#-------------------------------------------------------- 
                            elif "bicara jp " in msg.text:
                                say = msg.text.replace("bicara jp ","")
                                lang = 'ja'
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(msg.to,"hasil.mp3")
                            elif 'cekig ' in msg.text.lower():
                                try:
                                    instagram = msg.text.lower().replace("cekig ","")
                                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                    soup = BeautifulSoup(html.text, 'html5lib')
                                    data = soup.find_all('meta', attrs={'property':'og:description'})
                                    text = data[0].get('content').split()
                                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                    text1 = data1[0].get('content').split()
                                    user = "Name: " + text[-2] + "\n"
                                    user1 = "Username: " + text[-1] + "\n"
                                    followers = "Followers: " + text[0] + "\n"
                                    following = "Following: " + text[2] + "\n"
                                    post = "Post: " + text[4] + "\n"
                                    link = "Link: " + "https://www.instagram.com/" + instagram
                                    detail = "========INSTAGRAM INFO USER========\n"
                                    details = "\n========INSTAGRAM INFO USER========"
                                    client.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                                    client.sendImageWithURL(msg.to, text1[0])
                                except Exception as njer:
                                    client.sendText(msg.to, str(njer))
#-----------
                            elif msg.text.lower() == 'runtime':
                                client.sendAudioWithURL(msg.to, mus)
#-----------
#-----------
                            elif msg.text.lower() == 'pap':
                                client.sendImage(msg.to,"me.png")
#-----------
                            elif msg.text.lower() == 'runtime':
                            	eltime = time.time() - botStart
                            	timerun = "Bot has been active "+waktu(eltime)
                            	client.sendMessage(msg.to,timerun)
#==============================================================================#
                            elif text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'mymid':
                                client.sendMessage(msg.to,"[MID]\n" +  clientMID)
                            elif text.lower() == 'myname':
                                me = client.getContact(clientMID)
                                client.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                            elif text.lower() == 'mybio':
                                me = client.getContact(clientMID)
                                client.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                            elif text.lower() == 'mypicture':
                                me = client.getContact(clientMID)
                                client.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            elif text.lower() == 'myvideoprofile':
                                me = client.getContact(clientMID)
                                client.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            elif text.lower() == 'mycover':
                                me = client.getContact(clientMID)
                                cover = channel.getProfileCoverURL(clientMID)    
                                client.sendImageWithURL(msg.to, cover)
                            elif "stealmid" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}" + ls
                                    client.sendMessage(msg.to, str(ret_))
                            elif "stealpicture" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line.naver.jp/" + client.getContact(ls).pictureStatus
                                        client.sendImageWithURL(msg.to, str(path))
                            elif "stealcover" in msg.text.lower():
                                if channel != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = channel.getProfileCoverURL(ls)
                                            client.sendImageWithURL(msg.to, str(path))
                            elif "stealname" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            elif "stealbio" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            elif "stealprofile" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        cu = channel.getProfileCoverURL(ls)
                                        path = str(cu)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        client.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage)
                                        client.sendImageWithURL(msg.to,image)
                                        client.sendImageWithURL(msg.to,path)
                            elif "stealcontact" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        mi_d = contact.mid
                                        client.sendContact(msg.to, mi_d)
                            elif "cloneprofile" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        client.cloneContactProfile(contact)
                                        client.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                    except:
                                        client.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == 'restoreprofile':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    client.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    client.sendMessage(msg.to, "Gagal restore profile")
                            elif "checkmid" in msg.text.lower():
                                separate = msg.text.split(" ")
                                saya = msg.text.replace(separate[0] + " ","")
                                client.sendMessage(receiver, None, contentMetadata={'mid': saya}, contentType=13)
                                
                            elif text.lower() == 'friendlist':
                                contactlist = client.getAllContactIds()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="═════════List Friend═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)
                                
                            elif text.lower() == 'blocklist':
                                blockedlist = client.getBlockedContactIds()
                                kontak = client.getContacts(blockedlist)
                                num=1
                                msgs="═════════List Blocked═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)
                            elif text.lower() == 'mention':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    mention(msg.to, nm5)             
                                client.sendMessage(receiver, "Members :"+str(jml))
                            elif text.lower() == 'lurking on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            client.sendMessage(msg.to,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        client.sendMessage(msg.to, "Set reading point:\n" + readTime)
                                        
                            elif text.lower() == 'lurking off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    client.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    client.sendMessage(msg.to, "Delete reading point:\n" + readTime)
                
                            elif text.lower() == 'lurking reset':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    client.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif text.lower() == 'lurking':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking has not been set.")
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except:
                    pass
            clientPoll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
