# %%
""" 寫一個 Kangaroo 的類別，替每一個 Kangaroo 命名，每個 Kangaroo 的育兒袋 裝的東西也不同 """
class Kangaroo:

    # def __init__(self, name, content=[]):
    #     """ 這個 __init__ 有 bug，當 Kangaroo 建立的物件，引數只有一個時候，
    #     再建立其他 string 物件時，會共用同一個 屬性列。

    #     為了避免這樣情況，需要改成當未設定 string num 引數時，會得到一個空的 list
    #     """
    #     self.name = name
    #     self.pouch_contents = content

    def __init__(self, name, content=None):
        """ 初始化兩個 attributes.
        name: Kangaroo name.
        pouch_contents: a empty list. Kangaroo 育兒袋內容物 """
        self.name = name
        if content == None:
            content = []
        self.pouch_contents = content

    """
    當使用 __init__ 使用有 bug 的版本時候，當調用 str() 時，
    會引發 RecursionError: maximum recursion depth exceeded.

    理由是：
    因為共用一個屬性列，當將 B 物件當作 A 物件 content 參數時，
    使用 str() 會回頭去找類別底下的所有屬性字串 self.name & self.pouch_contents
    而其中 self.pouch_contents 因為共用，所以會將裡面的東西拿出來給 for 迭代
    然後無限 Loop 下去。

    若改成 object.__str__()，則會直接回傳位置

    當使用 __init__ 改用成第二種版本，調用 str() 時，
    由於 self.number 變成 []，則只會回傳 self.name，故不會發生 Loop 的問題了
    """
    def __str__(self):
        """ return: string. """
        t = [f"{self.name} 的育兒袋有:"]
        for obj in self.pouch_contents:
            # s = str(obj)
            s = object.__str__(obj)
            t.append(s)
        return "\n".join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)


def main():
    Kanga = Kangaroo('Mon')
    roo = Kangaroo('kid')
    Kanga.put_in_pouch('keys')
    Kanga.put_in_pouch(['dollars'])
    Kanga.put_in_pouch(roo)
    print(Kanga)
    print(roo)


if __name__ == "__main__":
    main()
# %%
