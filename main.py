"""
******************************************************************
*** File Name : main.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : 実行用ファイル
***
******************************************************************
"""

from flask import *
import Global  #外部変数
import datetime as dt
import time
import re
from plyer import notification
import sqlite3
from Login import SearchUser
from Login import InsertUser
from Registration import RequestRegistration as req  #登録処理
from Edit_Delete import CompleteEdit #編集処理
from Edit_Delete import CompleteDelete #削除処理
from Edit_Delete import SearchTask #課題情報検索
from Edit_Delete import TaskUpdate #アプリ起動時
from Notice import Notice
from Board import InsertBoard
from Board import ReadBoard


app = Flask(__name__)


@app.route('/login/', methods=["GET", "POST"])
def login():
    """************************************************************************
    *** Function Name : login()
    *** Designer : 内田 裕也
    *** Date : 2021.06.20
    *** Function : ログインの認証処理を行う。
    *** Return : 認証が成功したら/home/にリダイレクト
                 認証が失敗したらもう一度idとパスワードを要求する画面を表示
    ***************************************************************************
    """
    input_id = request.form.get('id') 
    input_password = request.form.get('password')

    if request.method == "POST" :
        if SearchUser.SearchUser(input_id) == input_password :
            Global.user_id = input_id
            return redirect("/home/")
        else :
            return render_template("LoginFault.html")
    else :
        return render_template("Login.html")


@app.route('/signup/', methods=["GET", "POST"])
def signup():
    """************************************************************************
    *** Function Name : signup()
    *** Designer : 内田 裕也
    *** Date : 2021.06.20
    *** Function : id、パスワードの新規登録を行う。
    *** Return : 登録が成功したら/login/にリダイレクト
                 登録が失敗したらもう一度idとパスワードを要求する画面を表示
    ***************************************************************************
    """

    input_id = request.form.get('id')
    input_password = request.form.get('password')

    if request.method == "POST" :
        if InsertUser.InsertUser(input_id, input_password) == False :
            return render_template("DupFault.html")
        else :
            InsertUser.InsertUser(input_id, input_password)
            return redirect("/login/")
    else :
        return render_template("SignUp.html")


@app.route("/home/")
def home():
    """

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

    for array_task in c.execute('SELECT * FROM TASK_LIST WHERE user_id = (?)', Global.user_id):
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
   """

    dbname = 'reminder_task.sqlite3'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM TASK_LIST WHERE user_id = (?) ORDER BY deadline', (Global.user_id,))
    c_datetime = Global.c_datetime
    task_name = []
    deadline = []
    importance = []
    notice_time = []
    priority = []
    
    for row in cur:
        #Global.user_id = str(row[0])
        task_name.append(str(row[1]))
        deadline.append(str(row[2]))
        importance.append(int(row[3]))
        notice_time.append(str(row[4]))
        priority.append(str(row[5]))

    r_len = len(task_name)

    for i in range(r_len) :
        Notice.Notice(c_datetime, notice_time[i], task_name[i], deadline[i])
    
    conn.close()

    return render_template("Home.html", 
                            task_name = task_name, 
                            deadline = deadline, 
                            importance = importance, count = r_len)

    return render_template("Home.html")
    

@app.route('/register/', methods = ["GET", "POST"])
def RegisterTask():
    '''
    *********************************************************************************************
    *** Function Name       :RegisterTask()
    *** Designer            :植田 竜弘
    *** Date                :2021.6.18
    *** Function            :課題情報の入力を受け付ける。
    *** Return              :登録に成功したら/homeにリダイレクト
    ***                      登録に失敗したらもう一度，課題情報を入力する画面を表示
    ********************************************************************************************
    '''

    render_template('register.html')    

    if request.method == 'POST':

        Global.task_name = request.form['task_name']
        Global.deadline = request.form['deadline']
        Global.importance = request.form['importance']
        Global.notice_time = request.form['notice_time']

        # 以降のif文，try文は情報が正しく入力されているか判別するためのもの

        if len(Global.task_name) == 0 or len(Global.task_name) > 20:
            return render_template('registerFault.html')
        
        try:
            d_time = dt.datetime.strptime(Global.deadline, '%Y/%m/%d %H:%M')
            n_time = dt.datetime.strptime(Global.notice_time, '%Y/%m/%d %H:%M')
            int_importance = int(Global.importance)
        except ValueError:
            return render_template('registerFault.html')
        
        # 期日及び通知日時を数値のみの表記に変換
        # 期日～
        tmp1_d = Global.deadline.replace('/','')
        tmp2_d = tmp1_d.replace(' ','')
        number_d = tmp2_d.replace(':','')
        # 通知日時～
        tmp1_n = Global.notice_time.replace('/','')
        tmp2_n = tmp1_n.replace(' ','')
        number_n = tmp2_n.replace(':','')

        if int(Global.number_c) > int(number_n) or int(number_n) > int(number_d):
            return render_template('registerFault.html')

        req.RequestRegistration(Global.user_id, Global.task_name, Global.deadline, Global.importance, Global.notice_time, number_d)

        return redirect('/home/')
    
    else:
        return render_template('register.html')


@app.route("/EditTask/", methods = ["GET", "POST"])
def EditTask():
    """
    ***********************************
    *** Function Name :EditTask()
    *** Designer      :城谷拓身
    *** Date          :2021.07.04
    *** Function      :W4課題編集画面から課題情報を取得する．
    *** Return        :登録 DoneEdit.html (課題編集完了画面)
                       削除 DoneDelete.html（課題削除完了画面）
    ***********************************
    """

    if request.method == 'POST':
        

        #ここまでのどこかのタイミングでuser_idを取得
        #Global.user_id = "123456"

        #M10 編集，削除要求
        #ユーザがW4課題編集画面で登録か削除を選択
        choice_edit = request.form["send"]
        if choice_edit == "登録":
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
            #M11 編集要求
            CompleteEdit.CompleteEdit(Global.user_id,Global.task_name,Global.deadline,Global.importance,Global.notice_time)
            #編集処理
            #編集するデータをデータベースに渡す.
            return render_template("DoneEdit.html",
                                    task_name = Global.task_name,
                                    deadline = Global.deadline,
                                    priority = Global.importance,
                                    notice_time = Global.notice_time)
        elif choice_edit == "削除":
            Global.task_name = request.form.get('task_name')
            if len(Global.task_name) >20:
                return render_template("EditTask.html",error1 = '20文字以内で入力してください')
            elif len(Global.task_name) <=0:
                return render_template("EditTask.html",error1 = '課題名を入力してください')
            #M12 削除要求
            CompleteDelete.CompleteDelete(Global.user_id,Global.task_name)
            #削除処理
            #削除するデータをデータベースに渡す.
            return render_template("DoneDelete.html",
                                    task_name = Global.task_name,
                                    deadline = Global.deadline,
                                    priority = Global.importance,
                                    notice_time = Global.notice_time)
    else :
        #W4課題編集画面表示
        return render_template("EditTask.html") #task_name = task_name,#deadline = deadline,#importance = importance) 


@app.route('/board/', methods=["GET", "POST"])
def board():
    """************************************************************************
    *** Function Name : board()
    *** Designer : 内田 裕也
    *** Date : 2021.07.13
    *** Function : 掲示板を表示する
    *** Return : 掲示板情報
    ***************************************************************************
    """

    userid = Global.user_id

    input_message = request.form.get('message')
    i = int(ReadBoard.CountRecord()) + 1 
    c_date = dt.datetime.now()
    tmp_record = ReadBoard.ReadBoard()

    if request.method == "POST" :
        InsertBoard.InsertBoard(i, userid, c_date, input_message)
        tmp_record.append([userid,c_date,input_message])
        i = int(ReadBoard.CountRecord()) + 1 
        return render_template("Board.html", record = tmp_record, count = i-1)
    else :
        tmp_record = ReadBoard.ReadBoard()
        return render_template("Board.html", record = tmp_record, count = i-1)



if __name__ == '__main__':
    app.run(debug=False, port=8888)


"""
*** Revision :
*** V1.0 : 内田 裕也,2021.07.18
*** V1.1 : 内田 裕也,2021.07.19
"""