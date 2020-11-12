# %%
import copy

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    """

def print_time(t):
    """ t: a Time object """
    h = t.hour
    m = t.minute
    s = t.second
    print(f"{h:02d}:{m:02d}:{s:02d}")

def add_time(t1, t2):
    """ t1 and t2 is Time objects
    return: a Time object
    """
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

def modify_time(time):
    """ Time 的修飾器 """
    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    if time.minute >= 60 or time.second >= 60:
        modify_time(time)

def increment(time, seconds):
    """ Functional programming style，會修改所接收的引數。大多修飾器都 void
    seconds: integer.
    """
    time.second += seconds
    modify_time(time)

def increment_1(time, seconds):
    """ Pure function，不會修改引數，大多會產出結果。 """
    new_time = copy.deepcopy(time)
    new_time.second += seconds
    modify_time(new_time)
    return new_time

def time_to_int(time):
    """ 將時間轉換成整數
    return: secnods (總秒數)
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """ 將整數轉換成時間
    return: a Time object """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    # 測試可以用 time_to_int(int_to_time(seconds)) == seconds 檢查一致性

def add_time_2(t1, t2):
    """ 改寫 add_time 函式
    return: integer """
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    """ 針對時間格式進行偵錯
    minute、second 介於 0 ~ 60；hour is positive
    return: boolean
    """
    if time.second < 0 or time.minute < 0 or time.hour < 0:
        return False
    if time.second >= 60 or time.minute >= 60:
        return False
    return True

def add_time_3(t1, t2):
    """ 針對輸入的 time object 進行檢查
    return: integer"""
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError("請輸入正確的時間格式")
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def add_time_4(t1, t2):
    """ 使用斷言序句 (assert statement)，檢查一個 invariant，當不成立時提出一個例外。
    return: integer"""
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def main():
    # time = Time()
    # time.hour = 1
    # time.minute = 1
    # time.second = 15
    # print_time(time)

    start = Time()
    start.hour = 9
    start.minute = 59
    start.second = 59

    duration = Time()
    duration.hour = 0
    duration.minute = 60
    duration.second = 60

    done = add_time(start, duration)
    print_time(done)

    done_2 = add_time_2(start, duration)
    print_time(done_2)

    # done_3 = add_time_3(start, duration)
    # print_time(done_3)

    # done_4 = add_time_4(start, duration)
    # print_time(done_4)


if __name__ == "__main__":
    main()

# %%
