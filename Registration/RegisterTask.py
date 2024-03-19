'''
*************************************************************************************************

*** File Name       :RegisterTask.py

*** Version         :V1.0

*** Designer        :植田 竜弘

*** Date            :2021.6.18

*** Purpose         :課題の基本情報を登録する。

*************************************************************************************************
'''

from flask import Flask, request, render_template, redirect
import Global # 外部変数を宣言しているファイル(Global.py)
from Registration import RequestRegistration as req
from datetime import datetime as dt

app = Flask(__name__)

@app.route('/register', methods = ["GET", "POST"])
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
            d_time = dt.strptime(Global.deadline, '%Y/%m/%d %H:%M')
            n_time = dt.strptime(Global.notice_time, '%Y/%m/%d %H:%M')
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

@app.route('/home/')
def home():
    return render_template('Home.html')

if __name__ == "__main__":
    app.run(port = 12345, debug = False)

'''

*** Revision    :
*** V1.0        :植田 竜弘, 2021.06.18

'''
