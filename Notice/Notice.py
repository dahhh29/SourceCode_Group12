"""
******************************************************************
*** File Name : Notice.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : 通知を行う。
***
******************************************************************
"""

import Global
import re
import datetime
from plyer import notification

def Notice(c_datetime,notice_time,task_name,deadline) :
    """************************************************************************
    *** Function Name : Notice(c_datetime,notice_time,task_name,deadline)
    *** Designer : 内田 裕也
    *** Date : 2021.06.20
    *** Function : 通知時間が来たら通知を行う。
    *** Return : Ture 通知
                 False 処理続行
    ***************************************************************************
    """

    c_datetime = datetime.datetime.now()
    #現在時刻をそれぞれ月、日、時、分の情報に分けて保存
    c_month = c_datetime.month
    c_day = c_datetime.day
    c_hour = c_datetime.hour
    c_minute = c_datetime.minute
    #print(c_month,c_day,c_hour,c_minute)

    tmpList = re.findall(r"\d+", notice_time) #文字列から数字部分のみ取出し
    intList = [int(s) for s in tmpList] #数字の文字列をint型に変換
    n_month = intList[1]
    n_day = intList[2]
    n_hour = intList[3]
    n_minute = intList[4]
    #print(n_month,n_day,n_hour,n_minute)

    if (n_month <= c_month
        and n_day <= c_day
        and n_hour <= c_hour
        and n_minute <= c_minute) :
        notification.notify(
            title = "課題リマインダー",
            message = task_name + "の提出" + "\n" + deadline + "まで",
            timeout = 10
        )
        return True
    else :
        return False

"""
#テスト用データ
c=datetime.datetime.now()
print(c)
print("通知時刻:")
n = input()
t = "数学"
d = "2021年12月31日23時"

while Notice(c,n,t,d) == False :
    time.sleep(1)
    c=datetime.datetime.now()
    print(c)
"""



"""
*** Revision :
*** V1.0 : 内田 裕也,2021.06.20
*** V1.1 : 内田 裕也,2021.07.19
"""
