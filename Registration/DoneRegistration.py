'''
********************************************************************************************

*** File Name     :DoneRegistration.py

*** Version       :V1.0

*** Designer      :植田 竜弘

*** Date          :2021.6.24

*** Purpose       :データベースに格納された課題データをリストとして画面出力する。

*******************************************************************************************
'''

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/home")

def DoneRegistration(db_name):

    '''
    ********************************************************************************************

    *** File Name     :DoneRegistration(db_name)

    *** Version       :V1.0

    *** Designer      :植田 竜弘

    *** Date          :2021.6.24

    *** Function      :リスト化された課題を画面出力する。

    *******************************************************************************************
    '''

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # 以下データベースから情報を取り出し整理する
    t_name_list = []
    deadline_list = []
    importance_list = []
    priority_list = []
    i = 0

    for array_task in c.execute('SELECT * FROM TASK_LIST'):
        t_name_list[i] = array_task[1]
        deadline_list[i] = array_task[2]
        importance_list[i] = array_task[3]
        priority_list[i] = array_task[4]
        i += 1
    
    conn.close()

    task_list = [[]]

    for j in range(i - 1):    
        task_list[j][0] = t_name_list[j]
        task_list[j][1] = deadline_list[j]
        task_list[j][2] = importance_list[j]
        task_list[j][3] = priority_list[j]

    # 以下優先度が高い順に課題をリスト化し画面出力する
    sorted_task_list = sorted(task_list, reverse = True, key = lambda x: x[3])

    for j in range(i - 1):
        return render_template('Home.html', name = sorted_task_list[j][0], deadline = sorted_task_list[j][1], importance = sorted_task_list[j][2], priority = sorted_task_list[j][3])

    if __name__ == "__main__":
        app.run(port = 12345, debug = False)
        