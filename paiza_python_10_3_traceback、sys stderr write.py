# coding: utf-8
# Your code here!

# tracebackスタックトレース提供
import traceback, sys
print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    # 例外情報を文字列として取得できる
    # print(traceback.format_exc())

    # 実行時エラーにエラー詳細を出力
    # 標準エラー出力write ★出力先は色々変えられる
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)