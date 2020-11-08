# %%
import math, copy
from ch15_class_object import Point, Rectangle
from ch15_class_object import print_point, distance_between_points, find_center


class Circle:
    """ Represents 一個圓
        Attributes: center, radius
        其中 center(圓心) 是一個 Point 物件，
        而 radius(半徑) 是一個數字。 """


def point_in_circle(point, circle):
    """ Check point 是否在 circle 內或是邊界上.
        point: Point object
        circle: Circle object
        return: point in/on circle is ture """
    dist = distance_between_points(point, circle.center)
    return dist <= circle.radius


def rect_in_circle(rect, circle):
    """ Check rectangle 是否在 circle 內或是邊界上
        rect: Rectangle object
        circle: Circle object """

    """ Check rect 四個角的點是否都在 circle 內或是邊界上 """
    p = copy.deepcopy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y += rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """ Check rectangle any corner in/on circle """

    p = copy.deepcopy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y += rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False

def rect_circle_overlap_anywhere(rect, circle):
    """ 寫出一個函式，能判斷矩形與圓形任何一處是有重疊 """

    box = find_center(rect)     # 矩形中心點

    if rect_circle_overlap(rect, circle):
        return True

    # 判斷矩形寬邊是否與圓心有重疊
    elif rect.corner.x <= circle.center.x <= rect.corner.x + rect.width:
        if abs(circle.center.y - box.y) <= circle.radius + rect.height/2:
            return True
        else:
            return False

    # 判斷矩形長邊是否與圓心有重疊
    elif rect.corner.y <= circle.center.y <= rect.corner.y + rect.height:
        if abs(circle.center.x - box.x) <= circle.radius + rect.width/2:
            return True
        else:
            return False

    return False

def main():
    """ 實體化一個圓 """
    circle = Circle()
    circle.center = Point()
    circle.center.x = 4
    circle.center.y = 5
    circle.radius = 0.25
    print("Circle:")
    print_point(circle.center)
    print(f"radius {circle.radius}")
    print()


    """ 實體化一個矩形 """
    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = 2
    rect.corner.y = 2
    rect.width = 4
    rect.height = 2
    print("Rectangle:")
    print_point(rect.corner)
    print(f"width {rect.width}")
    print(f"height {rect.height}")
    print()

    # print(point_in_circle(rect.corner, circle))
    # print(rect_in_circle(rect, circle))
    # print(rect_circle_overlap(rect, circle))
    print(rect_circle_overlap_anywhere(rect, circle))

# %%
if __name__ == "__main__":
    main()

# %%
