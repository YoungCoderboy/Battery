import psutil
import requests
import json
import time
import os

cnt=0
flag=False
usID=0
usName=""

while(True):
    cnt+=1

    battery_percent,var,battery_status=psutil.sensors_battery()

    api_id = 28606519
    api_hash = 'ae8c46ac5df19f9095b9362090f8cdf1'
    token = '6277211477:AAGLcuNMvzTmPThOBkpM2H66j6Xl9CqOAx0'


    message = ""
    url= "https://api.telegram.org/bot6277211477:AAGLcuNMvzTmPThOBkpM2H66j6Xl9CqOAx0/getUpdates"
    res=requests.get(url)

    user_id=0
    user_name=""

    if flag==False:
        flag=True
        user_id = -1
        user_name=input("tere telegram ki user id bata @")
        data=json.loads(res.text)
        for i in data['result']:
             dic=i.get('message')
             if(dic!=None):
                dic2=dic.get('from')
                # print(dic2)
                if(dic2.get('username')==user_name):
                     user_id=dic2.get('id')
             else:
                dic=i.get('my_chat_member')
                dic2=dic.get('from')
                # print(dic2)
                if(dic2.get('username')==user_name):
                     user_id=dic2.get('id')

        if user_id==-1:
             print("NOT FOUND")
             exit(-1)

        usId=user_id
        user_name=usName

    else:
         user_id=usID
         user_name=usName
   
    
    user_id=str(user_id)
    battery_needed=int(input("tuza kitna charge karna he "))


    message="Charging chalu he"

    if(((int(battery_percent)))>=battery_needed):
        message="kya mazak kar raha he battery phale he target: "+str(battery_needed)+" se jada he"
        url= "https://api.telegram.org/bot"+ token +"/sendMessage?chat_id="+ user_id+ "&parse_mode=MarkdownV2&text=" + message
        res=requests.get(url)
        exit()
    # charging is not started

    if(battery_status==False):
        message="Laptop ko phale charging ko laga"
    url= "https://api.telegram.org/bot"+ token +"/sendMessage?chat_id="+ user_id+ "&parse_mode=MarkdownV2&text=" + message
    res=requests.get(url)
    print(message)
    # waiting for charging to start
    waitvar=battery_status
    while(waitvar==False):
        os.system('cls')
        print("waiting.",battery_percent)
        time.sleep(1)
        os.system('cls')
        print("waiting..",battery_percent)
        time.sleep(1)
        os.system('cls')
        print("waiting...",battery_percent)
        time.sleep(1)
        os.system('cls')
        print("waiting....",battery_percent)
        time.sleep(1)
        os.system('cls')
        battery_percent,var,battery_status=psutil.sensors_battery()
        waitvar=battery_status
        continue;
    
    message="charging suru ho gaye he target: "+ str(battery_needed)
    url= "https://api.telegram.org/bot"+ token +"/sendMessage?chat_id="+ user_id+ "&parse_mode=MarkdownV2&text=" + message
    res=requests.get(url)
    # battery has start charging


    battery_percent,var,battery_status=psutil.sensors_battery()
    print(battery_status,battery_percent)
    while((battery_status==True) and (int(battery_percent))<=(99)):
        os.system('cls')
        print("charging.",battery_percent)
        time.sleep(1)
        os.system('cls')
        print("charging..",battery_percent)
        time.sleep(1)
        os.system('cls')
        print("charging...",battery_percent)
        time.sleep(1)
        os.system('cls')
        print("charging....",battery_percent)
        time.sleep(1)
        os.system('cls')
        battery_percent,var,battery_status=psutil.sensors_battery()
        if(((int(battery_percent)))>=(battery_needed)):
                message="tari battery charge ho gaye he to charger band kar de"
                print(message)
                url= "https://api.telegram.org/bot"+ token +"/sendMessage?chat_id="+ user_id+ "&parse_mode=MarkdownV2&text=" + message
                res=requests.get(url)
                exit()



    if(((int(battery_percent)))<battery_needed):
        message="charging ku band kar di wapas laga"
    else:
         exit()
 
    url= "https://api.telegram.org/bot"+ token +"/sendMessage?chat_id="+ user_id+ "&parse_mode=MarkdownV2&text=" + message
    res=requests.get(url)

    if(cnt>5):
         exit();



