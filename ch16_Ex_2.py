""" 學習使用 datetime 模組 """
# %%
from datetime import date, datetime

def today_week():
    """ Represent: 今天的日期以及星期"""
    today = date.today()

    return today


def birthday(bday):
    """ Represent: 顯示使用者的年齡，與距離生日還有多久
    bir: User birthday (date object)
    return: Age and how long next borthday."""

    birthday = datetime(bday.year, bday.month, bday.day)
    now = datetime.now()
    next_bir = birthday.replace(year = now.year)
    age = now.year - birthday.year
    if now > next_bir:
        """ 表示已經過今年生日，長了1歲 """
        next_bir = birthday.replace(year = now.year + 1)    # 計算至明年生日
    else:
        """ 表示還未過今年生日 """
        age -= 1
    interval = next_bir - now

    return age, interval


def bdaydate():
    """ Represent: 輸入日期，回傳一個 date object. """
    date = input("請輸入生日 (yyyy/mm/dd): ")
    date = date.split('/')
    return date(int(date[0]), int(date[1]), int(date[2]))


def double_day(bday1, bday2):
    """ Represent: 其中一個人出生日至另一個人出生日兩倍的日子，這天叫 Double day """
    d1 = max(bday1, bday2)
    d2 = min(bday1, bday2)
    dd = d1 + (d1 - d2)

    return dd


def main():
    print("今天日期為:", end=" ")
    today = today_week()
    print(f"{today}, {today.strftime('%A')}")

    s = input("請輸入生日 (yyyy/mm/dd): ")
    s = s.split('/')
    bday = date(int(s[0]), int(s[1]), int(s[2]))
    age , interval = birthday(bday)
    print(f"使用者年齡: {age} 歲")
    print(f"距離下一次生日還有: {interval}")

    bday1 = bdaydate()
    bday2 = bdaydate()
    dd = double_day(bday1, bday2)
    print(f"兩人 Double day 是: {dd}")



if __name__ == "__main__":
    main()
# %%
