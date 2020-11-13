# %%
class Time1:
    """" Represents: the time of day. """

def print_time(time):
    print(f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}")

time1 = Time1()
time1.hour = 5
time1.minute = 10
time1.second = 5

print_time(time1)

""" 比較上下兩個程式碼，一個是類別 + 函式，另一個將函式寫入類別裡，變成類別裡的方法(method) """

class Time2:
    """" Represents: the time of day. """
    def print_time(self):   # 方法的第一個引數 self，會指定類別自己，相當於函式將類別當作引數，慣例 self 名稱
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

time2 = Time2()
time2.hour = 5
time2.minute = 10
time2.second = 5

time2.print_time()  # 呼叫類別中的方法，需要利用類別的物件使用點記號法呼叫

# %%
class Time:
    """" Represents: the time of day. """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):   # 方法的第一個引數 self，會指定類別自己，相當於函式將類別當作引數
        """ 列印出時間 """
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    def time_to_int(self):
        """ 將時間格式轉成整數
            return: a integer. """
        minute = self.hour * 60 + self.minute
        seconds = minute * 60 + self.second
        return seconds

    def increment(self, seconds):
        """ 將時間增加秒數 """
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        """ 比較 self time 是否在 other time 之後
        other: Time object.
        return: boolean
        """
        return self.time_to_int() > other.time_to_int()

    def add_time(self, other):
        """ Represent: Two Time object add.
        return: new Time object."""
        addt = self.time_to_int() + other.time_to_int()
        return int_to_time(addt)

    def __str__(self):
        """ 回傳一個物件字串的表示值 """
        return (f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    # def __add__(self, other):     # 等同於呼叫 add_time 方法
    #     """ 運算子 + 重載(__str__) """
    #     seconds = self.time_to_int() + other.time_to_int()
    #     return int_to_time(seconds)

    def __add__(self, other):
        """ 運算子重載，此方法設計是基於型別的分發設計 """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """ 當物件本身在 + 運算子右邊時，會調用此方法"""
        return self.__add__(other)

def int_to_time(seconds):
    """ Represent: 將整數轉成時間格式
        return: New Time object. """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    # 不輸入引數，將使用預設引數
    time = Time()
    time.print_time()

    # 分別有 hour, minute, second 三種位置引數
    start = Time(5, 10, 30)
    start.print_time()
    end = start.increment(500)
    end.print_time()
    print(end.is_after(start))

    # __str__ 方法，當 print 一個物件時，Python 會調用 str 方法
    time1 = Time(9, 5)
    print(time1)

    # __add__ 方法，當對 Time 物件使用 + 運算子時，Python 會調用 add 方法
    time2 = Time(6, 30)
    duration = Time(0, 30)
    print(time2 + duration)     # 基於型別進行分發，但 Time 物件一定要在左邊。除非增加 __radd__
    print(time2 + 50)

    # __radd__ 方法，當 Time 物件在 + 運算子右邊時會被調用
    time3 = Time(7, 24)
    print(50 + time3)

    #!! Python 多型的概念，由於 Time 物件有提供 add 的方法，所以它們就能使用 sum
    t1 = Time(2, 30)
    t2 = Time(0, 30)
    t3 = Time(1, 45)
    total = sum([t1, t2, t3])
    print(total)

if __name__ == "__main__":
    main()

# %%
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """ other: Point object or Tuple """
        if isinstance(other, Point):
            return add_point(self, other)
        elif isinstance(other, tuple):
            return (self.x + other[0], self.y + other[1])

    def print_point(self):
        print(f"({self.x}, {self.y})")

def add_point(p1, p2):
    p = Point()
    p.x = p1.x + p2.x
    p.y = p1.y + p2.y
    return p


# 不輸入引數，使用預設引述
p1 = Point()
p1.print_point()

# 輸入引數
p2 = Point(3, 4)
p2.print_point()

# 使用 __str__ 方法
p3 = Point(5,12)
print(p3)

# 使用 __add__ 方法，並增加型別的分發
p4 = (3, 4)
print(p3 + p4)
p5 = Point(5, 12)
print(p3 + p5)


# %%
