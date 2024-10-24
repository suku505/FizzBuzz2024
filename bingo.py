import tkinter as tk
import random

Max = 75  # 最大値
root = tk.Tk()


class num:
    count = 0
    Number = [i for i in range(1, Max + 1)]  # 1~75までの配列
    Select_Num = [0]  # 選んだ数字格納

    def bingo(event):
        if len(num.Number) > 0:
            num.Select_Num.append(
                num.Number.pop(random.randint(0, len(num.Number) - 1))
            )
            num.count += 1

            num_list = ""  # 結果を表示するようで、用意
            for i in range(1, len(num.Select_Num)):
                num_list += f"{num.Select_Num[i]} "
                if i % 10 == 0:  # 10回抽選する毎に改行し、見やすく
                    num_list += "\n"

            Static1.config(text=f"{num.Select_Num[-1]}")
            Static2.config(text=num_list)
        else:
            Static1.config(text="抽選終了！！")


root.title("Bingo")
root.geometry("800x600")

Static1 = tk.Label(
    text=f"{num.Select_Num[len(num.Select_Num)-1]}",
    font=("bold", 100),  # 大きさ
    foreground="black",  # 文字の色
)
Static1.place(x=30, y=50)
Static1.pack(anchor="center", expand=1)

Static2 = tk.Label(text=0, font=("Times", 30))
Static2.place(x=100, y=200)
Static2.pack(anchor="center", expand=1)

Button1 = tk.Button(text="抽選", width=50)
Button1.bind("<Button-1>", num.bingo)
Button1.pack()

root.mainloop()
