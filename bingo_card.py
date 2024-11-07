import tkinter as tk
import random


class BingoCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Card Generator")

        # ビンゴカードの番号範囲を設定
        self.number_ranges = {
            "B": list(range(1, 16)),
            "I": list(range(16, 31)),
            "N": list(range(31, 46)),
            "G": list(range(46, 61)),
            "O": list(range(61, 76)),
        }

        # カードのグリッドを設定
        self.card = [[None for _ in range(5)] for _ in range(5)]
        self.selected = [[False for _ in range(5)] for _ in range(5)]

        # 結果表示用ラベルを作成
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), fg="blue")
        self.result_label.grid(row=6, column=0, columnspan=5)

        self.generate_card()
        self.create_card_ui()

    def generate_card(self):
        # 各列にランダムな番号を割り当て
        for col, letter in enumerate("BINGO"):
            numbers = random.sample(self.number_ranges[letter], 5)
            for row in range(5):
                if col == 2 and row == 2:  # 真ん中はFreeスペース
                    self.card[row][col] = "Free"
                    self.selected[row][col] = True
                else:
                    self.card[row][col] = numbers[row]

    def create_card_ui(self):
        # BINGOの文字を表示
        for col, letter in enumerate("BINGO"):
            label = tk.Label(self.root, text=letter, font=("Arial", 16, "bold"))
            label.grid(row=0, column=col)

        # カードのUIを作成
        for row in range(5):
            for col in range(5):
                num = self.card[row][col]
                button = tk.Button(
                    self.root,
                    text=str(num),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.select_number(r, c),
                )
                button.grid(row=row + 1, column=col)

                if self.selected[row][col]:  # Freeマスは最初から選択状態
                    button.config(state="disabled", relief="sunken")

    def select_number(self, row, col):
        # 数字が選択されたときの処理
        if not self.selected[row][col]:  # 未選択のマスのみ選択可能
            self.selected[row][col] = True
            button = self.root.grid_slaves(row=row + 1, column=col)[0]
            button.config(state="disabled", relief="sunken")
            self.check_bingo()

    def check_bingo(self):
        # リーチとビンゴの判定を行い、結果をGUIに表示
        bingo_found = False
        message = ""

        # 横方向のビンゴとリーチ判定
        for row in range(5):
            if all(self.selected[row][col] for col in range(5)):
                message += f"Bingo on row {row + 1}!\n"
                bingo_found = True
            elif sum(self.selected[row][col] for col in range(5)) == 4:
                message += f"Reach on row {row + 1}!\n"

        # 縦方向のビンゴとリーチ判定
        for col in range(5):
            if all(self.selected[row][col] for row in range(5)):
                message += f"Bingo on column {col + 1}!\n"
                bingo_found = True
            elif sum(self.selected[row][col] for row in range(5)) == 4:
                message += f"Reach on column {col + 1}!\n"

        # 斜めのビンゴとリーチ判定
        if all(self.selected[i][i] for i in range(5)):
            message += "Bingo on diagonal (\\)!\n"
            bingo_found = True
        elif sum(self.selected[i][i] for i in range(5)) == 4:
            message += "Reach on diagonal (\\)!\n"

        if all(self.selected[i][4 - i] for i in range(5)):
            message += "Bingo on diagonal (/)!\n"
            bingo_found = True
        elif sum(self.selected[i][4 - i] for i in range(5)) == 4:
            message += "Reach on diagonal (/)\n"

        # 結果をGUI上で表示
        if bingo_found:
            self.result_label.config(text="Bingo! Congratulations!")
        else:
            self.result_label.config(text=message if message else "")


root = tk.Tk()
app = BingoCard(root)
root.mainloop()
