"""
*******************************************
*** File Name :CompleteDelete.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.06.25
*** Purpose   :課題情報をデータベースから削除する．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.06.25
"""

import sqlite3

def CompleteDelete(user_id, #使用者のID
                   task_name) : #課題名
    """
    ***********************************
    *** Function Name :CompleteDelete()
    *** Designer      :城谷拓身
    *** Date          :2021.6.25
    *** Function      :課題情報をデータベースから削除する.
    ***********************************
    """
    #reminder_task.sqlite3にアクセスする.
    dbname = 'reminder_task.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #入力された課題情報をデータベースから削除する.
    cur.execute('DELETE FROM TASK_LIST where (user_id = ?) AND (task_name = ?)',(user_id,task_name))
    conn.commit()
    conn.close()

