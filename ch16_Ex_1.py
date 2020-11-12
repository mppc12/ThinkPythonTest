# %%
from ch16_class_fanction import Time, print_time, valid_time
from ch16_class_fanction import time_to_int, int_to_time
import copy

def mul_time(time, num):
    """ 將時間乘上一個數字
    time: Time object.
    num: integer.
    return: new Time object.
    """
    if not valid_time(time):
        raise ValueError("請輸入正確的時間格式")
    new_time = copy.deepcopy(time)
    seconds = time_to_int(new_time)     # 轉成整數進行運算
    mul_sec = int(seconds * num)
    return int_to_time(mul_sec)         # 轉回時間格式，回傳新的 Time() 物件

def avg_pace(time, distance):
    """ Represent 結束比賽時每英哩所花的時間
    time: Time object. (比賽所花的時間)
    distance: a number (正數).
    return: Time object. (average pace)
    """
    return mul_time(time, 1/distance)

def mi_to_km(mi):
    """ Represent: 英里轉公里 """
    km = mi * 1.61
    return km

def km_to_mi(km):
    """ Represent: 公里轉英里 """
    mi = km / 1.61
    return mi

def main():
    # start = Time()
    # start.hour = 5
    # start.minute = 10
    # start.second = 50

    # mul_num = 5
    # end = mul_time(start, mul_num)
    # print_time(end)

    game = Time()
    game.hour = 2
    game.minute = 5
    game.second = 30
    print("跑半馬所花的總時間:", end=" ")
    print_time(game)
    distance = 21.0975  # 半馬距離，公里
    mi_dist = km_to_mi(distance)
    mi_avg = avg_pace(game, mi_dist)
    print("平均每英里所要花的時間:", end=" ")
    print_time(mi_avg)
    km_avg = avg_pace(game, distance)
    print("平均每公里所要花的時間:", end=" ")
    print_time(km_avg)


if __name__ == "__main__":
    main()
# %%
