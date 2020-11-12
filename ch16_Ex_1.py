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
    seconds = time_to_int(new_time)
    mul_sec = seconds * num
    return int_to_time(mul_sec)

def avg_pace(time, distance):
    """ Represent a player over """

def main():

    start = Time()
    start.hour = 5
    start.minute = 10
    start.second = 50

    mul_num = 5
    end = mul_time(start, mul_num)
    print_time(end)



if __name__ == "__main__":
    main()
# %%
