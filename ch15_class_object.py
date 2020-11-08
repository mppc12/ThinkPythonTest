# %%
import copy
import math

class Point:
    """ Represents 一個在平面上的點 """


def print_point(p):
    """ 使用 f-string 列印出 Point 物件的 attributes x, y 的內容 """
    print(f"{p.x}, {p.y}")


class Rectangle:
    """ Represents 一個矩形
        attributes: width, height, corner. """


def find_center(rect):
    """ 尋找矩陣的中心
        rect: 一個 Rectangle 的物件
        return: 一個 new Point 的物件 """
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def grow_rectangle(rect, dwidth, dheight):
    """ 透過添加寬度跟高度來修改矩形的大小
        rect: 一個 Rectangle 的物件
        dwidth: 想增加的寬度 (可為負數)
        dheight: 想增加的高度 (可為負數) """
    rect.width += dwidth
    rect.height += dheight

def distance_between_points(p1, p2):
    """ 列印出兩點的距離
        p1: Point 的物件
        p2: Point 的物件
        return: float """
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

def move_rectangle(rect, dx, dy):
    """ 修改矩形的一個角的位子，來移動矩形
        rect: 一個 Rectangle 的物件
        dx: 要改變的 x 座標量 (可以為負數)
        dy: 要改變的 y 座標量 (可以為負數) """
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_copy(rect, dx, dy):
    """ 移動一個矩形，同時回傳一個新的矩形的物件
        rect: 一個 Rectangle 的物件
        dx: 要改變的 x 座標量 (可以為負數)
        dy: 要改變的 y 座標量 (可以為負數)
        return: 一個 new Rectangle 的物件"""
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new


# %%
def main():

    """ 製造一個 blank，它是一個點，來至 Point() """
    blank = Point()     # 類別實體化 (instantiation)，black 則為一個 實體 (instance)
    blank.x = 3.0       # 使用「點記號法」指定"值"給一個實體
    blank.y = 4.0       # 指定的目標是一個物件的具名元素(x,y)，又稱屬性 (attributes)
    print("blank", end=" ")
    print_point(blank)
    print()

    """ 製造一個 box，它是一個矩形，來至 Rectangle() """
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0      # 一個物件是另一個物件的屬性，稱 內嵌的 (embedded)
    box.corner.y = 0.0
    print("box:", end=" \n")
    print(f"width {box.width}")
    print(f"height {box.height}")


    """ 尋找 box 矩形的中心點 """
    center = find_center(box)
    print("center", end=" ")
    print_point(center)
    print()

    """ 修改 box 矩形的寬與高 """
    grow_rectangle(box, 50, 100)
    print("change width and height box:", end=" \n")
    print(f"width {box.width}")
    print(f"height {box.height}")
    center = find_center(box)
    print("center", end=" ")
    print_point(center)
    print()

    """ 移動 box 矩形的位置 """
    move_rectangle(box, 100, 150)
    print("move box:", end=" \n")
    center = find_center(box)
    print("center", end=" ")
    print_point(center)
    print()

    """ 製作新的矩形，同時移動 box 矩形的位置 """
    new_box = move_rectangle_copy(box, -50, -100)
    print("new box center:", end=" ")
    new_center = find_center(new_box)
    print_point(new_center)
    print()


if __name__ == "__main__":
    main()


# %%
