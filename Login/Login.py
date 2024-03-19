"""
******************************************************************
*** File Name : Login.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : ログイン処理を行う。
***
******************************************************************
"""

from flask import Flask, render_template, request,Response, abort, redirect
from Login import SearchUser
from Login import InsertUser

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


@app.route('/home/')
def home():
    return render_template("Home.html")
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)


"""
*** Revision :
*** V1.0 : 内田 裕也,2021.06.20
*** V1.1 : 内田 裕也,2021.07.19
"""