"""
******************************************************************
*** File Name : Board.py
*** Version : V1.1
*** Designer : 内田 裕也
*** Date : 2021.07.19
*** Purpose : 掲示板処理を行う
***
******************************************************************
"""

from flask import Flask, render_template, request,Response, abort, redirect
from Board import ReadBoard
from Board import InsertBoard
import datetime

userid = 'test1' #テスト用

app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template("Home.html")

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

    input_message = request.form.get('message')
    i = int(ReadBoard.CountRecord()) + 1 
    c_date = datetime.datetime.now()
    tmp_record = ReadBoard.ReadBoard()

    if request.method == "POST" :
        InsertBoard.InsertBoard(i, userid, c_date, input_message)
        tmp_record.append([userid,c_date,input_message])
        return render_template("Board.html", record = tmp_record, count = i-1)
    else :
        tmp_record = ReadBoard.ReadBoard()
        return render_template("Board.html", record = tmp_record, count = i-1)

if __name__ == '__main__':
    app.run(debug=False,port=8888)


"""
*** Revision :
*** V1.0 : 内田 裕也,2021.07.13
*** V1.1 : 内田 裕也,2021.07.19
"""