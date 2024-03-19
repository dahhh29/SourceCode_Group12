'''
********************************************************************************************

*** File Name     :RequestRegistration.py

*** Version       :V1.0

*** Designer      :植田 竜弘

*** Date          :2021.6.20

*** Purpose       :入力された課題の情報をサーバに渡す。

*******************************************************************************************
'''

import sqlite3
import Global
from Registration import DoneRegistration as done

def RequestRegistration(user_id, t_name, deadline, importance, n_time, number_d):

    '''
    ***************************************************************************************************

    *** Function Name     :RequestRegistration(user_id, t_name, d_time, number_d, importance, n_time)

    *** Designer          :植田 竜弘

    *** Date              :2021.6.20

    *** Function          :課題情報をデータベースに追加する。

    ***************************************************************************************************57
    '''

    Global.priority = (int(importance) * (10 ** 6)) / (int(number_d) - int(Global.number_c))

    db_name = 'reminder_task.sqlite3'
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    #c.execute('CREATE TABLE IF NOT EXISTS TASK_LIST (課題ID　TEXT PRIMARY KEY, 課題名 TEXT, 期日 TEXT, 重要度 INTEGER, 優先度 REAL, 通知日時 TEXT)')
    #c.execute('SELECT count(*)')
    #number = c.fetchall()
    #number_of_data = number[0][0]
    #c.execute(f'INSERT INTO TASK_LIST VALUES ({id} - {str(int(number_of_data + 1))}, {t_name}, {d_time}, {importance}, {Global.priority}, {n_time})')
    c.execute('INSERT INTO TASK_LIST VALUES (?, ?, ?, ?, ?, ?)', (user_id, t_name, deadline, importance, n_time, Global.priority))
    conn.commit()
    conn.close()

    #done.DoneRegistration(db_name)

'''

*** Revision    :
*** V1.0        :植田 竜弘, 2021.06.20
*** V1.1 : 内田 裕也,2021.07.19
'''
