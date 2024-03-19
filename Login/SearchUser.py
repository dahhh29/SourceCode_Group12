"""
******************************************************************
*** File Name : SearchUser.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.007.19
*** Purpose : 入力されたIDに対する正しいパスワードを検索する。
***
******************************************************************
"""

import sqlite3

def SearchUser(id) :
    """************************************************************************
    *** Function Name : SearchUser(id)
    *** Designer : 内田 裕也
    *** Date : 2021.06.18
    *** Function : 入力されたIDに対する正しいパスワードを返す。
    *** Return : 正しいパスワード
                 IDに対応するパスワードが見つからなかった場合はFalse
    ***************************************************************************
    """

    dbname = 'reminder_user.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #IDに対応するパスワードを出力するSQL文
    cur.execute('SELECT パスワード FROM reminder_user WHERE ID LIKE (?)', (id,))

    #検索結果をtmpListに代入
    tmpList = cur.fetchall()
    if len(tmpList) == 1 :
        #リストから取り出す
        r_password = tmpList[0][0]
        cur.close()
        conn.close()
        return r_password
    else :
        cur.close()
        conn.close()
        return False

"""
*** Revision :
*** V1.0 : 内田 裕也,2021.06.18
*** V1.1 : 内田 裕也,2021.07.19
"""
