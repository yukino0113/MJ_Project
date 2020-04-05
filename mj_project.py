from tkinter import *
from tkinter import messagebox
import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials as Sac

# main_main_window settingsy
main_window = Tk()
main_window.title("日麻程式")
main_window.geometry("800x750")
main_window.resizable(0, 0)

# googleSheet connect
scope = ['https://spreadsheets.google.com/feeds']
credentials = Sac.from_json_keyfile_name('key.json', scope)
gs = gspread.authorize(credentials)
gs_key = '1vCn5Huyn3g4QrG3-hPQi9TJLSetr1qungEgwT2tEZSw'
spreadSheets = gs.open_by_key(gs_key)

# googleSheet vars define

user_ws = spreadSheets.worksheet("註冊名單")
score_ws = spreadSheets.worksheet("個人成績整理")
data_ws = spreadSheets.worksheet("資料")

app = Frame(main_window)

# var init
up_point = IntVar()
down_point = IntVar()
left_point = IntVar()
right_point = IntVar()

# images
tenbo = PhotoImage(file = r"pic\tenbo.png")
tenbo_ud = PhotoImage(file = r"pic\tenbo_ud.png")
# oya_pic = PhotoImage(file = r"pic\oya.png")


# 開始使用
def start():
    global startbtn, signupbtn, pointbtn, statbtn, staffbtn, quitbtn
    global btnrichi_up, btnrichi_down, btnrichi_left, btnrichi_right
    global up_point, down_point, left_point, right_point
    global rounds, rounds_now, bonba, oya, nega_richi

    # btn hide
    startbtn.place_forget()
    signupbtn.place_forget()
    pointbtn.place_forget()
    statbtn.place_forget()
    staffbtn.place_forget()
    quitbtn.place_forget()

    # init player stats
    # 0=dataCount, 1=name, 2=rounds, 3=rank, 4=endPoints
    # 5=points, 6=hitPoints, 7=ronTimes, 8=tsumoTimes, 9=gunTimes, 10=richiTimes
    stat_up = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stat_down = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stat_left = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stat_right = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # init settings
    long = "half"
    init_point = 25000
    negative = "0"
    nega_richi = "0"
    rounds = ["東一局", "東二局", "東三局", "東四局",
             "南一局", "南二局", "南三局", "南四局",
             "西一局", "西二局", "西三局", "西四局"]
    rounds_now = 0
    bonba = 0
    oya = 1

    # var set
    up_point.set(init_point)
    down_point.set(init_point)
    left_point.set(init_point)
    right_point.set(init_point)

    def option_change(new_long, new_up, new_down, new_left, new_right, new_negative, new_nega_richi, new_oya):
        long = new_long
        up_point.set(new_up)
        down_point.set(new_down)
        left_point.set(new_left)
        right_point.set(new_right)
        negative = new_negative
        nega_richi = new_nega_richi
        oya = new_oya

    def btn_up_cancel_richi():
        global btnrichi_up, up_bow, up_point
        up_point.set(up_point.get()+1000)
        up_bow.place_forget()
        btnrichi_up.place(x=350, y=150)

    def up_richi():
        global up_point, up_bow, tenbo_ud

        if up_point.get() < 1000 and nega_richi == 0:
            messagebox.showerror("立直錯誤", "點數不足，無法立直")
        else:
            up_point.set(up_point.get()-1000)
            btnrichi_up.place_forget()
            up_bow = Button(main_window, image=tenbo_ud, command=btn_up_cancel_richi)
            up_bow.place(x=275, y=200)

    def btn_down_cancel_richi():
        global btnrichi_down, down_bow, down_point
        down_point.set(down_point.get()+1000)
        down_bow.place_forget()
        btnrichi_down.place(x=350, y=600)

    def down_richi():
        global down_point, down_bow, tenbo_ud
        if down_point.get() < 1000 and nega_richi == 0:
            messagebox.showerror("立直錯誤", "點數不足，無法立直")
        else:
            down_point.set(down_point.get() - 1000)
            btnrichi_down.place_forget()
            down_bow = Button(main_window, image=tenbo_ud, command=btn_down_cancel_richi)
            down_bow.place(x=275, y=520)

    def btn_left_cancel_richi():
        global btnrichi_left, left_bow, left_point
        left_point.set(left_point.get()+1000)
        left_bow.place_forget()
        btnrichi_left.place(x=125, y=375)

    def left_richi():
        global left_point, left_bow, tenbo
        if left_point.get() < 1000 and nega_richi == 0:
            messagebox.showerror("立直錯誤", "點數不足，無法立直")
        else:
            left_point.set(left_point.get() - 1000)
            btnrichi_left.place_forget()
            left_bow = Button(main_window, image=tenbo, command=btn_left_cancel_richi)
            left_bow.place(x=230, y=250)

    def btn_right_cancel_richi():
        global btnrichi_right, right_bow, right_point
        right_point.set(right_point.get()+1000)
        right_bow.place_forget()
        btnrichi_right.place(x=600, y=375)

    def right_richi():
        global right_point, right_bow, tenbo
        if right_point.get() < 1000 and nega_richi == 0:
            messagebox.showerror("立直錯誤", "點數不足，無法立直")
        else:
            right_point.set(right_point.get() - 1000)
            btnrichi_right.place_forget()
            right_bow = Button(main_window, image=tenbo, command=btn_right_cancel_richi)
            right_bow.place(x=550, y=250)

    def option():
        def opt_confirm():
            new_oya = varDealer.get()
            new_long = varRound.get()
            new_negative = varNegative.get()
            new_nega_richi = varNegaRichi.get()
            new_up = up_en.get()
            new_down = down_en.get()
            new_left = left_en.get()
            new_right = right_en.get()

            option_change(new_long, new_up, new_down, new_left, new_right, new_negative, new_nega_richi, new_oya)
            opt_window.destroy()


        opt_window = Toplevel(main_window)
        opt_window.geometry("500x450")
        opt_window.title("設定")
        opt_window.resizable(0, 0)

        labelRemind = Label(opt_window, text="※更改選項會重新開始牌局※", font=("jf-openhuninn-1.0", 20), anchor="n")
        labelRemind.grid(row=0, column=0, columnspan=12)

        # start dealer
        labelDealer = Label(opt_window, text="起家", font=("jf-openhuninn-1.0", 15), anchor="nw")
        labelDealer.grid(row=2, column=3)
        varDealer = IntVar()
        varDealer.set(1)
        Radiobutton(opt_window, text="↑", font=("jf-openhuninn-1.0", 15), variable=varDealer, value=1).grid(row=2, column=5)
        Radiobutton(opt_window, text="←", font=("jf-openhuninn-1.0", 15), variable=varDealer, value=2).grid(row=2, column=6)
        Radiobutton(opt_window, text="↓", font=("jf-openhuninn-1.0", 15), variable=varDealer, value=3).grid(row=2, column=7)
        Radiobutton(opt_window, text="→", font=("jf-openhuninn-1.0", 15), variable=varDealer, value=4).grid(row=2, column=8)

        varRound = StringVar()
        varRound.set("half")
        Radiobutton(opt_window, text="東風戰", font=("jf-openhuninn-1.0", 15), variable=varRound, value="quarter").grid(row=3, column=5)
        Radiobutton(opt_window, text="半莊戰", font=("jf-openhuninn-1.0", 15), variable=varRound, value="half").grid(row=3, column=7)

        # negative
        labelNegative = Label(opt_window, text="負點續行", font=("jf-openhuninn-1.0", 15), anchor="nw")
        labelNegative.grid(row=5, column=3)

        varNegative = StringVar()
        varNegative.set("0")
        Radiobutton(opt_window, text="採用", font=("jf-openhuninn-1.0", 15), variable=varNegative, value=1).grid(row=5, column=5)
        Radiobutton(opt_window, text="不採用", font=("jf-openhuninn-1.0", 15), variable=varNegative, value=0).grid(row=5, column=7)

        # nega richi
        labelNegaRichi = Label(opt_window, text="盒聽", font=("jf-openhuninn-1.0", 15), anchor="nw")
        labelNegaRichi.grid(row=6, column=3)

        varNegaRichi = StringVar()
        varNegaRichi.set("0")
        Radiobutton(opt_window, text="採用", font=("jf-openhuninn-1.0", 15), variable=varNegaRichi, value="1").grid(row=6, column=5)
        Radiobutton(opt_window, text="不採用", font=("jf-openhuninn-1.0", 15), variable=varNegaRichi, value="0").grid(row=6, column=7)

        # start points
        labelStartPoint = Label(opt_window, text="設定起始點數", font=("jf-openhuninn-1.0", 15), anchor="nw")
        labelStartPoint.grid(row=7, column=3)

        upPoint_text = Label(opt_window, text="↑", font=("jf-openhuninn-1.0", 15), anchor="nw").grid(row=8, column=5)
        up_en = IntVar()
        up_en.set(25000)
        up_entry = Entry(opt_window, width=6, font=("jf-openhuninn-1.0", 14), textvariable=up_en).grid(row=8, column=6)

        leftPoint_text = Label(opt_window, text="←", font=("jf-openhuninn-1.0", 15), anchor="nw").grid(row=9, column=5)
        left_en = IntVar()
        left_en.set(25000)
        left_entry = Entry(opt_window, width=6, font=("jf-openhuninn-1.0", 14), textvariable=left_en).grid(row=9, column=6)

        downPoint_text = Label(opt_window, text="↓", font=("jf-openhuninn-1.0", 15), anchor="nw").grid(row=10, column=5)
        down_en = IntVar()
        down_en.set(25000)
        down_entry = Entry(opt_window, width=6, font=("jf-openhuninn-1.0", 14), textvariable=down_en).grid(row=10, column=6)

        rightPoint_text = Label(opt_window, text="→", font=("jf-openhuninn-1.0", 15), anchor="nw").grid(row=11, column=5)
        right_en = IntVar()
        right_en.set(25000)
        right_entry = Entry(opt_window, width=6, font=("jf-openhuninn-1.0", 14), textvariable=right_en).grid(row=11, column=6)

        # none label
        labelNone = Label(opt_window, text=" ", font=("jf-openhuninn-1.0", 15), anchor="nw")
        labelNone.grid(row=12)

        # confirm button
        confirm = Button(opt_window, text="確認", font=("jf-openhuninn-1.0", 14), command=opt_confirm)
        confirm.grid(row=13, column=5)

        # close button
        close = Button(opt_window, text="關閉", font=("jf-openhuninn-1.0", 14), command=opt_window.destroy).grid(row=13, column=7)

    # def ron():

    # def tsumo():

    def water():
        water_window = Tk()
        water_window.title("日麻程式")
        water_window.geometry("300x250")
        water_window.resizable(0, 0)

    # info show
    round_text = Label(main_window, text = rounds[rounds_now], font=("jf-openhuninn-1.0", 40))
    round_text.place(x=320, y=300)
    bonba_text = Label(main_window, text = str(bonba) + "本場" , font=("jf-openhuninn-1.0", 40))
    if 1 >= bonba < 10:
        bonba_text.place(x=330, y=375)
    elif bonba >= 10:
        bonba_text.place(x=315, y=375)


    # option change
    option_change(long, init_point, init_point, init_point, init_point, negative, nega_richi, oya)

    # richi button
    btnrichi_up = Button(main_window, text="立直", font=("jf-openhuninn-1.0", 20), command=up_richi)
    btnrichi_up.place(x=350, y=150)

    btnrichi_down = Button(main_window, text="立直", font=("jf-openhuninn-1.0", 20), command=down_richi)
    btnrichi_down.place(x=350, y=600)

    btnrichi_left = Button(main_window, text="立直", font=("jf-openhuninn-1.0", 20), command=left_richi)
    btnrichi_left.place(x=125, y=375)

    btnrichi_right = Button(main_window, text="立直", font=("jf-openhuninn-1.0", 20), command=right_richi)
    btnrichi_right.place(x=600, y=375)

    # points text
    up_p_show = Label(main_window, textvariable=up_point, font=("jf-openhuninn-1.0", 30))
    up_p_show.place(x=325, y=100)

    down_p_show = Label(main_window, textvariable=down_point, font=("jf-openhuninn-1.0", 30))
    down_p_show.place(x=325, y=550)

    left_p_show = Label(main_window, textvariable=left_point, font=("jf-openhuninn-1.0", 30))
    left_p_show.place(x=100, y=325)

    right_p_show = Label(main_window, textvariable=right_point, font=("jf-openhuninn-1.0", 30))
    right_p_show.place(x=575, y=325)

    # ron button
    ronbtn = Button(main_window, text="榮和", font=("jf-openhuninn-1.0", 20))
    ronbtn.place(x=20, y=600)

    # tsumo button
    tsumobtn = Button(main_window, text="自摸", font=("jf-openhuninn-1.0", 20))
    tsumobtn.place(x=120, y=600)

    # water button
    waterbtn = Button(main_window, text="流局", font=("jf-openhuninn-1.0", 20), command=water)
    waterbtn.place(x=120, y=675)

    # option button
    optionbtn = Button(main_window, text="設定", font=("jf-openhuninn-1.0", 20), command=option)
    optionbtn.place(x=20, y=675)

    # reset button
    resetbtn = Button(main_window, text="reset", font=("jf-openhuninn-1.0", 20))
    resetbtn.place(x=700, y=10)


# 用戶註冊
def signup():
    # 註冊資料查詢
    def check_signup():
        username = new_name.get()
        counter = 0
        for user in user_ws.col_values(2):
            counter += 1
            if user == username:
                messagebox.showerror("註冊錯誤", "此名稱(暱稱)已註冊")
                window_signup.destroy()
                break
            if user == 'None':
                user_ws.update_cell(counter, 2, username)
                messagebox.showinfo("註冊成功", str(username) + "  已註冊成功")
                window_signup.destroy()
                break

    # signup window settings
    window_signup = Toplevel(main_window)
    window_signup.geometry('300x200')
    window_signup.title("用戶註冊")
    window_signup.resizable(0, 0)

    # label settings
    signup_name = Label(window_signup, text="請輸入名字(或暱稱)", font=("jf-openhuninn-1.0", 20))
    signup_name.pack(side=TOP)

    # entry settings
    new_name = StringVar()
    signup_entry = Entry(window_signup, font=("jf-openhuninn-1.0", 14), textvariable=new_name)
    signup_entry.pack(side=TOP, pady=10)

    # entry confrim button
    signup_quitbtn = Button(window_signup, text="確認", font=("jf-openhuninn-1.0", 16), command=check_signup)
    signup_quitbtn.pack(side=LEFT, pady=10, padx=40)

    # entry quit button
    signup_quitbtn = Button(window_signup, text="取消", font=("jf-openhuninn-1.0", 16), command=window_signup.destroy)
    signup_quitbtn.pack(side=RIGHT, pady=10, padx=40)


# 點數查詢
def point():
    def check_point():
        han = han_en.get()
        fu = fu_en.get()

        if fu % 10 != 0:
            fu = math.ceil(fu / 10) * 10

        points = fu * 2 ** (han + 2)

        if points > 2000 and han >= 4:
            if han == 5 or han == 4 and points > 2000:
                points = 2000
            elif han == 6 or han == 7:
                points = 3000
            elif 8 <= han <= 10:
                points = 4000
            elif 11 <= han <= 12:
                points = 6000
            else:
                points = 8000

        # show oya ron
        oya_ron = Label(window_point, text="親家和牌：" + str(math.ceil(points * 6 / 100) * 100) + "點",
                        font=("jf-openhuninn-1.0", 14))
        oya_ron.place(x=70, y=180)

        # show oya tsumo
        oya_tsumo = Label(window_point, text="親家自摸：" + str(math.ceil(points * 2 / 100) * 100) + " 點all",
                          font=("jf-openhuninn-1.0", 14))
        oya_tsumo.place(x=70, y=220)

        # show ko ron
        ko_ron = Label(window_point, text="子家和牌：" + str(math.ceil(points * 4 / 100) * 100) + " 點",
                       font=("jf-openhuninn-1.0", 14))
        ko_ron.place(x=70, y=260)

        # show ko tsumo
        ko_tsumo = Label(window_point, text="子家自摸：", font=("jf-openhuninn-1.0", 14))
        ko_tsumo.place(x=100, y=300)
        ko_tsumo_point = Label(window_point, text="莊家：" + str(math.ceil(points * 2 / 100) * 100) + "點\n子家：" + str(
            math.ceil(points / 100) * 100) + "點", font=("jf-openhuninn-1.0", 14))
        ko_tsumo_point.place(x=80, y=330)

    # point window settings
    window_point = Toplevel(main_window)
    window_point.geometry('300x400')
    window_point.title("點數查詢")
    window_point.resizable(0, 0)

    # han label
    han_text = Label(window_point, text="飜數", font=("jf-openhuninn-1.0", 14))
    han_text.place(x=10, y=10)

    # han entry
    han_en = IntVar()
    han_entry = Entry(window_point, font=("jf-openhuninn-1.0", 14), textvariable=han_en)
    han_entry.place(x=80, y=10, width=150)

    # fu label
    fu_text = Label(window_point, text="符數", font=("jf-openhuninn-1.0", 14))
    fu_text.place(x=10, y=50)

    # fu entry
    fu_en = IntVar()
    fu_entry = Entry(window_point, font=("jf-openhuninn-1.0", 14), textvariable=fu_en)
    fu_entry.place(x=80, y=50, width=150)

    # point warning text
    point_warn = Label(window_point, text="僅限輸入數字", font=("jf-openhuninn-1.0", 14))
    point_warn.place(x=80, y=90)

    # point confrim button
    point_quitbtn = Button(window_point, text="確認", font=("jf-openhuninn-1.0", 16), command=check_point)
    point_quitbtn.place(x=30, y=130)

    # point quit button
    point_quitbtn = Button(window_point, text="取消", font=("jf-openhuninn-1.0", 16), command=window_point.destroy)
    point_quitbtn.place(x=200, y=130)


# 數據查詢
def data():
    def data_show():
        name = name_en.get()

        # data copy from gs
        row_data = score_ws.find(name).row
        gs_data = score_ws.row_values(row_data)

        # 場數資料
        data_round = Label(window_data, text="總場數：", font=("jf-openhuninn-1.0", 14))
        data_round.place(x=10, y=50)
        round_data = Label(window_data, text=gs_data[5], font=("jf-openhuninn-1.0", 14))
        round_data.place(x=90, y=50)

        # 得點資料
        data_score = Label(window_data, text="得點：", font=("jf-openhuninn-1.0", 14))
        data_score.place(x=10, y=90)
        score_data = Label(window_data, text=gs_data[4], font=("jf-openhuninn-1.0", 14))
        score_data.place(x=90, y=90)

        # 名次資料
        data_rank = Label(window_data, text="名次：", font=("jf-openhuninn-1.0", 14))
        data_rank.place(x=10, y=130)
        score_data = Label(window_data, text=gs_data[2], font=("jf-openhuninn-1.0", 14))
        score_data.place(x=90, y=130)

        # 一位率資料
        data_first = Label(window_data, text="一位率：", font=("jf-openhuninn-1.0", 14))
        data_first.place(x=150, y=10)
        first_data = Label(window_data, text=gs_data[6], font=("jf-openhuninn-1.0", 14))
        first_data.place(x=230, y=10)

        # 二位率資料
        data_second = Label(window_data, text="二位率：", font=("jf-openhuninn-1.0", 14))
        data_second.place(x=150, y=50)
        second_data = Label(window_data, text=gs_data[7], font=("jf-openhuninn-1.0", 14))
        second_data.place(x=230, y=50)

        # 三位率資料
        data_third = Label(window_data, text="三位率：", font=("jf-openhuninn-1.0", 14))
        data_third.place(x=150, y=90)
        third_data = Label(window_data, text=gs_data[8], font=("jf-openhuninn-1.0", 14))
        third_data.place(x=230, y=90)

        # 四位率資料
        data_fourth = Label(window_data, text="四位率：", font=("jf-openhuninn-1.0", 14))
        data_fourth.place(x=150, y=130)
        fourth_data = Label(window_data, text=gs_data[9], font=("jf-openhuninn-1.0", 14))
        fourth_data.place(x=230, y=130)

        # 平均打點資料
        data_avghit = Label(window_data, text="平均打點：", font=("jf-openhuninn-1.0", 14))
        data_avghit.place(x=330, y=10)
        avghit_data = Label(window_data, text=gs_data[10], font=("jf-openhuninn-1.0", 14))
        avghit_data.place(x=430, y=10)

        # 平均順位
        data_avgrank = Label(window_data, text="平均順位：", font=("jf-openhuninn-1.0", 14))
        data_avgrank.place(x=330, y=50)
        avgrank_data = Label(window_data, text=gs_data[11], font=("jf-openhuninn-1.0", 14))
        avgrank_data.place(x=430, y=50)

        # 起飛率
        data_fly = Label(window_data, text="起飛率：", font=("jf-openhuninn-1.0", 14))
        data_fly.place(x=330, y=90)
        fly_data = Label(window_data, text=gs_data[12], font=("jf-openhuninn-1.0", 14))
        fly_data.place(x=430, y=90)

        # 平均得點資料
        data_score = Label(window_data, text="平均得點：", font=("jf-openhuninn-1.0", 14))
        data_score.place(x=330, y=130)
        score_data = Label(window_data, text=gs_data[3], font=("jf-openhuninn-1.0", 14))
        score_data.place(x=430, y=130)

        # 和了率
        data_ron = Label(window_data, text="和了率：", font=("jf-openhuninn-1.0", 14))
        data_ron.place(x=500, y=10)
        ron_data = Label(window_data, text=gs_data[13], font=("jf-openhuninn-1.0", 14))
        ron_data.place(x=580, y=10)

        # 自摸率
        data_tsumo = Label(window_data, text="自摸率：", font=("jf-openhuninn-1.0", 14))
        data_tsumo.place(x=500, y=50)
        tsumo_data = Label(window_data, text=gs_data[14], font=("jf-openhuninn-1.0", 14))
        tsumo_data.place(x=580, y=50)

        # 放銃率
        data_gun = Label(window_data, text="放銃率：", font=("jf-openhuninn-1.0", 14))
        data_gun.place(x=500, y=90)
        gun_data = Label(window_data, text=gs_data[15], font=("jf-openhuninn-1.0", 14))
        gun_data.place(x=580, y=90)

        # 立直率
        data_richi = Label(window_data, text="立直率：", font=("jf-openhuninn-1.0", 14))
        data_richi.place(x=500, y=130)
        richi_data = Label(window_data, text=gs_data[16], font=("jf-openhuninn-1.0", 14))
        richi_data.place(x=580, y=130)

    # 輸入檢查
    def data_show_check():
        name = name_en.get()
        if name is not '':
            data_show()
        else:
            messagebox.showerror("輸入錯誤", "輸入不應為空白\n請重新輸入")

    # data window settings
    window_data = Toplevel(main_window)
    window_data.geometry('680x250')
    window_data.title("數據查詢")
    window_data.resizable(0, 0)

    # data_name
    data_name = Label(window_data, text="名稱", font=("jf-openhuninn-1.0", 14))
    data_name.place(x=10, y=10)
    name_en = StringVar()
    data_name_entry = Entry(window_data, font=("jf-openhuninn-1.0", 14), textvariable=name_en)
    data_name_entry.place(x=60, y=10, width=80)

    # data confirm button
    data_quitbtn = Button(window_data, text="確認", font=("jf-openhuninn-1.0", 14), command=data_show_check)
    data_quitbtn.place(x=170, y=190)

    # data quit button
    data_quitbtn = Button(window_data, text="取消", font=("jf-openhuninn-1.0", 14), command=window_data.destroy)
    data_quitbtn.place(x=430, y=190)


# 開發人員
def dis():
    # distributor window settings
    window_dis = Toplevel(main_window)
    window_dis.geometry('300x200')
    window_dis.title("開發人員")
    window_dis.resizable(0, 0)

    # distributor label
    dis_text = Label(window_dis, text="程式開發：\n雪野穗香雪野櫻華\n 美術：雪、野櫻華", font=("jf-openhuninn-1.0", 20))
    dis_text.pack(pady=10, side=TOP)

    # dis quit button
    dis_quitbtn = Button(window_dis, text="好的", font=("jf-openhuninn-1.0", 16), command=window_dis.destroy)
    dis_quitbtn.pack(side=BOTTOM, pady=10)


# menu_title
# title = Label(main_window, text="日麻程式", width = "10", font = ("jf-openhuninn-1.0", 50))
# title.pack(side = RIGHT)

# menu_startbtn
startbtn = Button(main_window, text="開始使用", font=("jf-openhuninn-1.0", 16), command=start)
startbtn.place(x=50, y=100, width="200", height="50", )

# menu_signupbtn
signupbtn = Button(main_window, text="用戶註冊", font=("jf-openhuninn-1.0", 16), command=signup)
signupbtn.place(x=50, y=200, width="200", height="50", )

# menu_pointbtn
pointbtn = Button(main_window, text="點數查詢", font=("jf-openhuninn-1.0", 16), command=point)
pointbtn.place(x=50, y=300, width="200", height="50", )

# menu_statbtn
statbtn = Button(main_window, text="數據查詢", font=("jf-openhuninn-1.0", 16), command=data)
statbtn.place(x=50, y=400, width="200", height="50", )

# menu_staff
staffbtn = Button(main_window, text="開發人員", font=("jf-openhuninn-1.0", 16), command=dis)
staffbtn.place(x=50, y=500, width="200", height="50", )

# menu_quit
quitbtn = Button(main_window, text="離開程式", font=("jf-openhuninn-1.0", 16), command=main_window.destroy)
quitbtn.place(x=50, y=600, width="200", height="50", )

main_window.mainloop()
