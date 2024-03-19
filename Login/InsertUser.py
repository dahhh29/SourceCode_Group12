"""
******************************************************************
*** File Name : InsertUser.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : IDとパスワードをデータベースに保存する。
***
******************************************************************
"""

import sqlite3

def InsertUser(id, password) :
    """************************************************************************
    *** Function Name : InsertUser(id,password)
    *** Designer : 内田 裕也
    *** Date : 2021.06.18
    *** Function : 入力されたIDとパスワードを新規にデータベースに追加する。
    ***************************************************************************
    """

    dbname = 'reminder_user.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    try :
        #入力されたIDとパスワードを新規にデータベースに挿入するSQL文
        cur.execute('INSERT INTO reminder_user VALUES (?, ?)', (id, password))
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