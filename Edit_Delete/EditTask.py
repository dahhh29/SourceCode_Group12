"""
*******************************************
*** File Name :EditTask.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.07.04
*** Purpose   :W4課題編集画面より課題情報を読み取り，
               +そのデータをサーバへ出す．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.07.04
"""

#flask取り込み
from flask import *
#外部変数取り込み
import Global
#Flaskオブジェクトの生成
app = Flask(__name__)

import sqlite3
#from Edit_Delete import CompleteRegistration #登録処理
from Edit_Delete import CompleteEdit #編集処理
from Edit_Delete import CompleteDelete #削除処理
from Edit_Delete import SearchTask #課題情報検索
from Edit_Delete import TaskUpdate #アプリ起動時

#サーバのルート（/）へアクセスがあった時 --- (*1)
@app.route("/", methods=["get","post"])
def root(): #テスト用ホーム画面
    #HTMLでWebフォームを記述 --- (*2)
    #ここまでのどこかのタイミングでuser_idを取得
    Global.user_id = "123456"
    #データベースの優先度を更新
    TaskUpdate(Global.user_id)
    #Task.dbにアクセスする.
    dbname = 'Task.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM task WHERE user_id = Global.user_id')
    for row in cur:
        Global.user_id = str(row[0])
        Global.task_name = str(row[1])
        Global.deadline = str(row[2])
        Global.importance = int(row[3])
        Global.notice_time = str(row[4])
        Global.priority = str(row[5])
        return render_template("home.html", 
                                task_name = Global.task_name, 
                                deadline = Global.deadline, 
                                priority = Global.priority)
    conn.close()
    
@app.route("/EditTask", methods=["post"])
def EditTask():
    """
    ***********************************
    *** Function Name :EditTask()
    *** Designer      :城谷拓身
    *** Date          :2021.07.04
    *** Function      :W4課題編集画面を表示する．
    *** Return        :EditTask.thml (W4課題編集画面)
    ***********************************
    """
    #W4課題編集画面表示
    return render_template("EditTask.html")#,#task_name = task_name,#deadline = deadline,#importance = importance) 
    
@app.route("/DoneEdit", methods=["POST"])
def DoneEdit():
    """
    ***********************************
    *** Function Name :DoneEdit()
    *** Designer      :城谷拓身
    *** Date          :2021.07.04
    *** Function      :W4課題編集画面から課題情報を取得する．
    *** Return        :登録 DoneEdit.html (課題編集完了画面)
                       削除 DoneDelete.html（課題削除完了画面）
    ***********************************
    """
    #M3 課題編集処理
    #W4課題編集画面から課題情報を取得
    Global.task_name = request.form.get('task_name')
    Global.deadline = request.form.get('deadline')
    Global.importance = request.form.get('importance')
    Global.notice_time = request.form.get('notice_time')

    #エラー処理
    if len(Global.task_name) >20:
        return render_template("EditTask.html",error1 = '20文字以内で入力してください')
    elif len(Global.task_name) <=0:
        return render_template("EditTask.html",error1 = '課題名を入力してください')
    if len(Global.deadline) >18:
        return render_template("EditTask.html",error2 = '18文字以内で入力してください')
    elif len(Global.deadline) <=0:
        return render_template("EditTask.html",error2 = 'MM月DD日HH時mm分で入力してください')
    if len(Global.importance) >4:
        return render_template("EditTask.html",error3 = '4文字以内で入力してください')
    elif len(Global.importance) <=0:
        return render_template("EditTask.html",error3 = '重要度を入力してください')
    if len(Global.notice_time) >18:
        return render_template("EditTask.html",error4 = '18文字以内で入力してください')
    if len(Global.notice_time) <= 0:
        return render_template("EditTask.html",error4 = 'MM月DD日HH時mm分で入力してください')

    #ここまでのどこかのタイミングでuser_idを取得
    Global.user_id = "123456"
    #M10 編集，削除要求
    #ユーザがW4課題編集画面で登録か削除を選択
    choice_edit = request.form["send"]
    if choice_edit == "登録":
        #M11 編集要求
        CompleteEdit(Global.user_id,Global.task_name,Global.deadline,Global.importance,Global.notice_time)
        #編集処理
        #編集するデータをデータベースに渡す.
        return render_template("DoneEdit.html",
                                task_name = Global.task_name,
                                deadline = Global.deadline,
                                priority = Global.importance,
                                notice_time = Global.notice_time)
    elif choice_edit == "削除":
        #M12 削除要求
        CompleteDelete(Global.user_id,Global.task_name)
        #削除処理
        #削除するデータをデータベースに渡す.
        return render_template("DoneDelete.html",
                                task_name = Global.task_name,
                                deadline = Global.deadline,
                                priority = Global.importance,
                                notice_time = Global.notice_time)

#サーバーを起動
if __name__ == "__main__":
    #app.run(debug=True, host='160.16.141.77', port=51280)
    app.run(debug=True,  port=8888)