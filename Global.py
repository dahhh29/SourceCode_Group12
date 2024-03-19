from datetime import datetime as dt

# 外部変数の宣言
c_datetime = dt.now() # 現在日時(年月日時分) 2021-07-18 10:35:05.189929
user_id = "" # ユーザID
task_name = [] # 課題名
deadline = [] # 課題の期日
importance = [] # 課題の重要度(0~100)
priority = [] # 優先度(期日と重要度から算出される数値)
notice_time = [] # 通知時刻

# 現在時刻を数値のみの表記に変換
current = c_datetime.strftime('%Y/%m/%d %H:%M')  # 2021/07/18 10:37
tmp1_c = current.replace('/','')                 # 20210718 10:37
tmp2_c = tmp1_c.replace(' ', '')                 # 2021071810:37
number_c = tmp2_c.replace(':','')                # 202107181037
