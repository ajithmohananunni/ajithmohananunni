#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date
 
expirydate = datetime.date(2023, 12, 30)
#expirydate = datetime.date(2023, 12, 30)
today=date.today()
def hero():
 
    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')
 
        t = threading.Thread(target=animate)
        t.start()
 
        #long process here
        time.sleep(20)
        done = True
 
    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')
 
        t = threading.Thread(target=animate)
        t.start()
 
        #long process here
        time.sleep(20)
        done = True
 
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
 
    clear()
    y=1
    newperiod=period
    banner='figlet AMUSEBOX'
    m=0
    i=1
    thisway=[0,2,4,6,8]
    thatway=[1,3,5,7,9]
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @Hacker6363")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        #chalo()
        print("\n---------Successfully hacked the server-----------")
        #chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        def getSum(n):
            sum=0
            for digit in str(n):
                sum += int(digit)
            return sum
        if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1," : RED")
                else:
                    print(newperiod+1," : GREEN")
            else:
                if current in numbers:
                    print(newperiod+1," : GREEN")
                else:
                    print(newperiod+1," : RED")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1,": RED")
                else:
                    print(newperiod+1,": GREEN")
            else:
                if current in numbers:
                    print(newperiod+1,": GREEN")
                else:
                    print(newperiod+1,": RED")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>21):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @Hacker6363")
            #print(numbers)
 
 
if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=11, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=16, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=19, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=20, minute=35, second=0, microsecond=0)
 
    if (True):
            period=20230626445
            hero()
    elif(False):
            period=20230626342
            hero()
    elif(False):
            period=20230626343
            hero()
    elif(now>Final and now<Finalend):
            period=20230626480
            hero()
    else:
        banner='figlet AMUSEBOX'
 
else:
    banner='figlet AMUSEBOX'
    system(banner)
