# python-慣れ/9.繰り返し.py
#
# ©  2018 やっプロ!製作委員会 cc by-sa 4.0

# 基礎概念その9: 繰り返し


# 同様の処理を何回も繰り返す場合、
# 同じコードを何度も書かなくて済むようになっている。

# 繰り返しは、whileを使う。

回数 = 0

while 回数 < 3:
  print('はじまり')
  # 回数を1増やす
  回数 = 回数 + 1
  print(回数)
  print('終わり')

# 無限ループにならないように、条件をちゃんと考えよう

