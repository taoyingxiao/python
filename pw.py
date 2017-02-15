#! /usr/bin/python3
password = {'email':'asdfghjkl',
            'qq':'qwertyu',
            'wechat':'fgbnmkiu'}
import sys
import pyperclip
if len(sys.argv)<2:
    print('Usage:python pw.py [account] -copy account password')
    sys.exit()
account=sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('password for '+account+' copy')
else:
    print('thereis no name '+account)