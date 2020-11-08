import copy

class Point:
    """ Represents 一個在平面上的點 """


class Rectangle:
    """ Represents 一個矩形
        attributes: width, height, corner. """


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

p1 = Point()
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)

""" 對實體而言， is 與 == 運算子預設行為是等價的，同樣檢查物件的身分 """
print(p1 is p2)     # False
print(p1 == p2)     # False

""" copy.copy 為淺層拷貝，並不會拷貝內嵌的物件 """
box2 = copy.copy(box)
print(box2 is box)  # False
print(box2.corner is box.corner)  # True 只有拷貝位置，所以內容物一樣

# %%
""" copy.deepcopy 為深層拷貝，會拷貝該物件所參考的物件，及物件所參考的物件 """
box3 = copy.deepcopy(box)
print(box3 is box)  # False
print(box3.corner == box.corner)  # False


# %%
""" Debug 除蟲 """
p = Point()
p.x = 3
p.y = 4
print(p.x)  # 3
print(p.y)  # 4

# %%
""" 當試著存取不存在的屬性時 """
# print(p.z)  # AttributeError: 'Point' object has no attribute 'z'

# %%
"""當不確定一個物件型別時"""
print(type(p))

# %%
"""使用 isinstance 來檢查一個物件是否為某個類別的實體"""
print(isinstance(p, Point))  # True

# %%
"""如果不確定一個物件是否真的有某個特定屬性，可以使用 hasattr"""
print(hasattr(p, 'x'))  # True

print(hasattr(p, 'z'))  # False

"""hasattr第一個引數可以是任何物件，第二個引數是一個字串，含屬性的名稱"""

# %%
"""也可以使用 try 述句來查看物件"""
try:
    x = p.z
except AttributeError:
    x = 0
print(x)

# %%
""" 淺層拷貝內的物件 vs 深層拷貝的物件"""
p_1 = box.corner
p_2 = box2.corner
p_3 = box3.corner
print(p_1.x)
print(p_2.x)
print(p_3.x)

p_1.x += box.width
print(p_1.x)
print(p_2.x)
print(p_3.x)

# %%
