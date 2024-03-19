"""
******************************************************************
*** File Name : ReadBoard.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : 掲示板から書き込み情報を読み込む
***
******************************************************************
"""

import sqlite3

def ReadBoard() :
    """************************************************************************
    *** Function Name : ReadBoard()
    *** Designer : 内田 裕也
    *** Date : 2021.07.13
    *** Function : 掲示板から書き込み情報を読み込む
    ***************************************************************************
    """

    dbname = 'reminder_board.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    
    cur.execute('SELECT * FROM reminder_board order by date limit 100')

    #検索結果をtmpListに代入
    tmpList = cur.fetchall()

    cur.close()
    conn.close()

    #recordリストに一つ一つ保存する
    count = int(CountRecord())
    record = []
    for i in range(count) :
        record.append([tmpList[i][1], tmpList[i][2], tmpList[i][3]])

    return record

def CountRecord() :
    """************************************************************************
    *** Function Name : CountRecord()
    *** Designer : 内田 裕也
    *** Date : 2021.07.13
    *** Function : 掲示板の書き込み数を取得
    ***************************************************************************
    """
    dbname = 'reminder_board.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    
    cur.execute('SELECT COUNT (*) FROM reminder_board')

    #検索結果をtmpListに代入
    tmpList = cur.fetchall()
    
    if len(tmpList) == 1 :
        #リストから取り出す
        count = tmpList[0][0]
        cur.close()
        conn.close()
        return count
    else :
        cur.close()
        conn.close()
        return False

#print(ReadBoard())
#print(CountRecord())

"""
*** Revision :
*** V1.0 : 内田 裕也,2021.07.13
*** V1.1 : 内田 裕也,2021.07.19
"""
