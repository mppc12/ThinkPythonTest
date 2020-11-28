# %%
import random
class Card:
    """ Represents a standard playing card.
    rank:
    Spades   -> 3
    Hearts   -> 2
    Diamonds -> 1
    Clubs    -> 0

    face cards:
    Jack    -> 11
    Queen   -> 12
    King    -> 13
    """
    """ suit_names 與 rank_names 為類別屬性，所關聯的是類別物件 Card """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [ None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'Jack', 'Queen', 'King']     # None 是為了能直觀選出，所以讓 0 這個索引用 空值 取代

    def __init__(self, suit=0, rank=2):
        """ 預設 梅花2 (2 of Clubs)
        suit 和 rank 為實體屬性，通常關聯某個特定實體，與類別屬性有所區隔.
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ Represents 使用物件 self 的屬性 rank 作為 Card 類別的 rank_name 串列(類別屬性) 的一個索引. """
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def __lt__(self, other):
        """ __lt__ 接受兩個引數，屬於內建的運算子，當 self 嚴格地小於 other 時( < 運算子) 回傳 True """
        """ __gt__ 則相當 >= 運算子，但當建立好 __lt__ 會預設將 __gt__ 反向設立 """
        # # 檢查數字(位階)
        # if self.rank < other.rank:
        #     return True
        # if self.rank > other.rank:
        #     return False
        # # 如果數字一樣，檢查花色
        # return self.suit < other.suit

        # 使用 tuple 以更簡潔方式寫出:
        t1 = self.rank, self.suit   # tuple 寫法
        t2 = other.rank, other.suit
        return t1 < t2


class Deck:
    """ 製作一副卡牌 """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        """ 移除最後一張牌，並回傳 """
        return self.cards.pop()

    def add_card(self, card):
        """ 新增一張牌，由於沒有使用其他方法，被稱為 veneer (薄層) """
        self.cards.append(card)

    def shuffle(self):
        """ 將卡牌進行洗牌 (隨機排列)，也是一種 veneer ."""
        random.shuffle(self.cards)

    def sort(self):
        """ 將卡牌進行排序 """
        self.cards.sort()

    def move_cards(self, hand, num):
        """ Represents: 將卡牌從 Deck 轉移到 Hand 上
        hand: 繼承 Deck 類別的 Hand 所製造的物件
        num: 要處理卡牌的數量.
        """
        for i in range(num):
            hand.add_card(self.pop_card())
            i = i

""" 繼承 (inheritance)
此處 Hand 類別就繼承 Deck.
Deck 為父類別，而 Hand 為子類別.
Hand 能使用 父類別中的所有屬性跟方法，若要修改則需要進行覆寫 (overrides)
"""
class Hand(Deck):
    """ Represents: 擁有一副手牌 """
    def __init__(self, label=''):     # 子類別重寫 __init__ 等於覆寫父類別的 __init__ (若父類別有的話)
        self.cards = []
        self.label = label



def main():
    # card1 = Card(3, 11)
    # print(card1)

    # # 呼叫 __lt__ 方法
    # card2 = Card(2, 11)
    # card3 = Card(2, 13)
    # print(card1 < card2)
    # print(card2 < card3)

    deck = Deck()
    # print(deck)

    hand = Hand('New hand')
    # print(hand.cards)
    print(hand.label)

    # card = deck.pop_card()
    # hand.add_card(card)
    # print(hand)
    deck.shuffle()
    deck.move_cards(hand, 5)
    print(hand)



if __name__ == "__main__":
    main()
# %%
