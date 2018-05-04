import os

def menu():

    print(""" 
#####...........#####...#####........
#....#..........#.......#...#...#####
#....#...#.#....#####...#...#.......#
#....#....#.........#...#...#...#####
#####....#.#....#####...#####...#####
========================================
全自動安裝環境 By 芮芮 台灣首發杜絕盜版
Facebook: fb.com/DxSOa
WeChat: DxSdzer
最初更新: 2018/05/05
最後更新: 2018/05/05 1.0
========================================
1. 安裝基礎環境
2. 安裝芮芮的已讀機
3. 待推薦
0. 退出
========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "1":
        print("========================================")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y python3")
        os.system("pkg install -y nodejs-current")
        os.system("pkg install -y nodejs-current-dev")
        os.system("pkg install -y coreutils")
        os.system("pkg install -y ruby")
        os.system("python2 -m pip install --upgrade pip")
        os.system("pip2 install rsa")
        os.system("pip2 install thrift==0.9.3")
        os.system("pip2 install requests")
        os.system("pip2 install bs4")
        os.system("pip2 install gtts")
        os.system("pip2 install beautifulsoup")
        os.system("pip2 install html5lib")
        os.system("pip2 install wikipedia")
        os.system("pip2 install pytz")
        os.system("pip2 install goslate")
        os.system("pip2 install googletrans")
        os.system("python3 -m pip install --upgrade pip")
        os.system("pip3 install rsa")
        os.system("pip3 install thrift")
        os.system("pip3 install requests")
        os.system("pip3 install linepy")
        os.system("pip3 install bs4")
        os.system("pip3 install gtts")
        os.system("pip3 install beautifulsoup")
        os.system("pip3 install html5lib")
        os.system("pip3 install wikipedia")
        os.system("pip3 install pytz")
        os.system("pip3 install goslate")
        os.system("pip3 install googletrans")
        print("基楚環境已安裝完成 :)")
        print("========================================")
        rmenu = input("是否返回主選單 (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    if what == "2":
        print("========================================")
        os.system("cd /data/data/com.termux/files/home")
        os.system("git clone https://github.com/DxSdzerLine/LINE")
        os.system("cd /data/data/com.termux/files/home/LINE")
        print("芮芮的已讀機已安裝完成 :)")
        print("========================================")
        rmenu = input("是否返回主選單 (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    if what == "3":
        print("========================================")
        print("待推薦 :)")
        print("========================================")
        rmenu = input("是否返回主選單 (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "0":
        print("Bye.")
        break
