import pyautogui
import time

lim = 7
pos_list=[]
input("【説明】\nクリックしてほしい座標(複数)と回数を入力するとプログラムがクリックしてくれます。")
while True:
    try:
        num = int(input("繰り返すクリック位置は何種類ですか？"))
        count = int(input("繰り返す回数は何回ですか?"))
        break
    except TypeError:
        print("数字を入力してください")
        continue

for i in range(num):
    print(str(i+1)+"つ目のクリック位置にマウスカーソルを置いてください("+str(lim)+"秒以内)")
    time.sleep(4)
    x, y = pyautogui.position()
    print(str(i+1)+"つ目のクリック位置は：x=",x,"y=",y)
    pos_list.append([])
    pos_list[i].append(x)
    pos_list[i].append(y)
print("取得した座標と順番は：\n",pos_list)
input("[Enter]で実行\n")

for i in range(count):
    print(str(i+1)+"回目：",end='')
    for j in pos_list:
        pyautogui.click(j[0], j[1])
        time.sleep(0.5)
    print("終了")
input("すべてのタスクを処理しました。\n[Enter]で終了")
print(pos_list)
