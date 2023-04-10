	import random


# 生成一个1到100之间的随机整数
answer = random.randint(1, 100)

# 初始化猜测次数
guesses = 0

# 循环直到猜对为止
while True:
    # 获取用户的猜测
    guess = int(input("请猜一个1到100之间的整数："))

    # 猜测次数加1
    guesses += 1

    # 判断猜测是否正确
    if guess == answer:
        print("恭喜你，猜对了！")
        print("你一共猜了%d次。" % guesses)
        break
    elif guess < answer:
        print("你猜的数字太小了，请再试一次。")
    else:
        print("你猜的数字太大了，请再试一次。")
