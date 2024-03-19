"""
******************************************************************
*** File Name : InsertBoard.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : 掲示板に新しい書き込みを追加する
***
******************************************************************
"""

import sqlite3
import datetime

def InsertBoard(boardID, userID, c_date, messeage) :
    """************************************************************************
    *** Function Name : InsertBoard(boardID, userID, c_date, messeage)
    *** Designer : 内田 裕也
    *** Date : 2021.07.13
    *** Function : 掲示板に新しい書き込みを追加する
    ***************************************************************************
    """

    dbname = 'reminder_board.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    try :
        cur.execute('INSERT INTO reminder_board VALUES (?, ?, ?, ?)', (boardID, userID, c_date, messeage))
        conn.commit()
    except sqlite3.Error :
        return False
    finally :
        cur.close()
        conn.close()

"""
*** Revision :
*** V1.0 : 内田 裕也,2021.06.18
*** V1.1 : 内田 裕也,2021.07.19
"""