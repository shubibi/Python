##数値3.1.1 P10
print("Hello Ver3")
print (2+2)
print(17/3)
print(17//3)
print(17%3)
print(5*3+2)
print(5**2)
print(2**7)

################
width = 20
height = 5*9
print(width * height)
################
print(3*3.75/1.5)
print(7.0/2)
################
tax = 12.5/100
price = 100.50
print(price*tax)
flee = price*tax
print(price+flee)
flee2 = price+flee
print (round(flee2,2))

##文字列3.1.2 P12
print ('spam eggs')
print('doesn\'t')#シングルクォート
print("doesn't")#ダブルクォート
print('Yes,he said.')
print("\"Yes,\"he said.")
print("Isn\'t, she said")
print('"Isn\'t,"she said.')
s = 'Firstline.\nSecondline'#\nは改行の意味
print(s)
print('C:\some\name')#\nは改行なので・・・
print(r'C:\some\name')#引用符の前のrに注目

##文字リテラルを複数行に書く
print("""\
Usage: thingy[OPTIONS]
    -h                  Display this usage message
    -H                  Hostname to connect to
""")

##文字列を演算子で連結
print(3*'un'+'ium')

##文字リテラルの自動連結
print('Py''thon')

text = ('abc''def')
print(text)

##変数とリテラルの連結
prefix = 'Py'
print(prefix+'thon')#変数とリテラルの連結には+を使用

##インデックス指定
word = 'Python'
print(word[0])#位置0のキャラクタを指定
print(word[5])#位置5のキャラクタを指定
print(word[-1])#最後のキャラクタを指定
print(word[-2])#最後から2番目のキャラクタを指定
print(word[-6])#位置0のキャラクタを指定
print(word[0:2])#位置0から2までの文字(0を含み2を含まない)
print(word[2:5])#位置2から5までの文字(2を含み5を含まない)
print(word[:2])#最初の位置から位置2までの文字
print(word[2:])#位置2から最後までの文字
print(word[-2:])#位置-2から最後までの文字
print(word[:2]+word[2:])
print(word[4:42])#スライジングでは範囲外の数値でも処理する

##文字列の改変
print('J'+word[1:])
print(word[:2]+'py')

##文字列の長さ　len()関数
s = 'asdfghjkqwertyuio'
print(len (s))

##リスト 3.1.3 P17
squares = [1,4,9,16,25]
print(squares)
print(squares[0])#インデクシングではアイテムを返す
print(squares[-1])
print(squares[-3:])#スライジングでは新たなリストを返す
print(squares[:])
print(squares+[31,15,12,29,40])#リストの連結

##リスト内の変更
cube = [1,2,4,8,17]#2の乗数だが間違いがある
print(2**4)#2の4乗は16
cube[4] = 16
print(cube)

##append()を利用し末尾にリストの追加
cube.append(216)#6の3乗を追加
cube.append(7**3)#7の3乗を追加
print(cube)

##スライジングへの代入
letter = ['a','b','c','d','e','f','g']
print(letter)
letter[2:5] = ['C','D','E']#リスト内の置換
print(letter)
letter[2:5] = []#リスト内の該当部分の削除
print(letter)
letter[:] = []#リストを空にする
print(letter)

##リストに対するlen()の使用
letter = ['a','b','c','d']
print(len(letter))
##リストを入れ子として使用
a = ['a','b','c']
b = [1,2,3]
x = [a,b]
print(x)
print(x[0])
print(x[0][1])#位置0内の位置1を参照
#####
