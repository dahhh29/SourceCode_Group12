"""
*******************************************
*** File Name :Priority.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.07.07
*** Purpose   :課題の期日と重要度から優先度を算出する.
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.07.07
"""

import datetime
from sys import int_info
import time
import re
import sqlite3


def Priority(deadline, #課題の期日
             importance) : #重要度

    """
    ***********************************
    *** Function Name :Priority()
    *** Designer      :城谷拓身
    *** Date          :2021.07.07
    *** Function      :課題の期日と重要度から優先度を算出する.
    *** Return        :Priority (優先度)
    ***********************************
    """

    #現在時刻を取得
    c_time = str(datetime.datetime.now())
    #現在時刻をそれぞれ月、日、時、分の情報に分ける
    strList = re.compile(r"\d+").findall(c_time)
    #文字列の数字をint型に変換
    intList = [int(s) for s in strList] 
    c_year = intList[0]
    c_month = intList[1]
    c_day = intList[2]
    c_hour = intList[3]
    c_minute = intList[4]
    
    #取得した課題の期日から数字部分のみ取出し
    strList = re.compile(r"\d+").findall(deadline)
    #文字列の数字をint型に変換
    intList = [int(s) for s in strList] 
    #課題の期日をそれぞれ月、日、時、分の情報に分ける
    d_month = intList[0]
    d_day = intList[1]
    d_hour = intList[2]
    d_minute = intList[3]
    #期日が現在時刻より前だったら年をまたぐ
    if (d_month < c_month) or (d_day < c_day) or (d_hour < c_hour) :
        d_year = c_year +1
    else :
        d_year = c_year

    #優先度計算 =重要度/(期日-現在時刻)*10^6
    #c_time:現在時刻
    c_time = c_year * 100000000 + c_month * 1000000 + c_day * 10000 + c_hour * 100 + c_minute
    #d_time:課題の期日
    d_time = d_year * 100000000 + d_month * 1000000 + d_day * 10000 + d_hour * 100 + d_minute
    importance = int(importance)
    priority = (importance /(d_time - c_time))  * (10 ** 6)
    
    #小数第二位以下で四捨五入
    #priority = round(priority, 1)

    return(priority)
