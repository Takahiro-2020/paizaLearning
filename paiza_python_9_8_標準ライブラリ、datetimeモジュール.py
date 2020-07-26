# datetimeモジュールにあるdatetimeクラスをインポート
from datetime import datetime, timedelta, timezone

# nowはクラスメソッドなのでインスタンスいらない
# datetimeは協定世界時 : 日本時間 - 9時間
today = datetime.now()
print(today)

# timezoneクラスで日本日時のタイムゾーンをインスタンス化　aware
# timedeltaクラスで時差を表現
jst   = timezone(timedelta(hours=9))
today = datetime.now(jst)
print(today)
print(today.year)
print(today.month)
print(today.day)

# 日時を指定したdatetimeインスタンス
# 日付、書式
day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
print(day)