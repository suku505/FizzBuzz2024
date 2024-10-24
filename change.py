money = 980
price = 130
coin = [500, 100, 50, 10]
result = []
change = 0

if money < price:
    print("お金が足りないよ！！")
    exit

money -= price
for i in coin:
    result.append(int(money / i))
    money = money % i

change += sum(coin[i] * result[i] for i in range(4))
print(f"お釣りは{change}円です。")
print("以下の硬貨を排出します")
for i in range(4):
    if result[i] == 0:
        continue
    print(f"{coin[i]}円を{result[i]}枚")
