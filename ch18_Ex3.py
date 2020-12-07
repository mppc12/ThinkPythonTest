""" 計算撲克牌各種型態出現的機率，以五張為基準
先比牌型 > 點數 > 花色
牌型：同花順 > 鐵支 > 葫蘆 > 同花 > 順子 > 三條 > 兩對 > 一對 > 散牌
點數：A > K > Q > J > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2
但做順子時，A 搭配 2345 當作 1，搭配 KQJ10 則當作 14
花色：黑桃 > 紅心 > 方塊 > 梅花
"""
# %%
import random
import time

class Card:
    """ Represents 標準撲克牌

    Attributes:
    suit: integer 0:黑桃 1:紅心 2:方塊 3:梅花
    rank: integer 1-13
    """
    suit_names = ['黑桃', '紅心', '方塊', '梅花']
    rank_names = [None, "A", '2', '3', '4', '5','6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ Returns 可以閱讀的字串(ex: 黑桃 7)"""
        return f'{Card.suit_names[self.suit]} {Card.rank_names[self.rank]}'

    def __lt__(self, other):
        """ 比較單張撲克牌，優先比點數，再比花色
        returns: boolean
        """
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2

class Deck:
    """ Represents 一副完整的撲克牌 (52張，不含鬼牌)
    Attributes:
        cards: 串列 屬於 Card 類別的物件
    """

    def __init__(self):
        """ 初始化52張撲克牌 """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """ 用字串格式列印出整副 deck. """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """ 對 deck 增加單張撲克牌
        card: Card 的物件
        """
        self.cards.append(card)

    def remove_card(self, card):
        """ 從 deck 移除一張指定的撲克牌；若沒有該撲克牌，則會發生例外
        card: Card 的物件
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """ 從 deck 取出一張撲克牌，並回傳
        i: 指定 deck 的索引值；預設最後一張
        """
        return self.cards.pop(i)

    def shuffle(self):
        """ 對 deck 進行洗牌. """
        random.shuffle(self.cards)

    def sort(self):
        """ 對 deck 進行排序 """
        self.cards.sort()

    def move_cards(self, hand, num):
        """ 從 hand 取出 N 張牌，發給 hand
        hand: Hand 類別的物件，撲克牌要發的目標
        num: integer 要移動的卡片數量
        """
        for _ in range(num):
            hand.add_card(self.pop_card())



class Hand(Deck):
    """ Represents 一位玩家的手牌. """
    def __init__(self, label=''):
        self.cards = []
        self.label = label


class PokerHand(Hand):
    """ Represents 檢查一位撲克牌玩家的手牌牌型. """
    def suit_hist(self):
        """ 確認手上的撲克牌花色數量. """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1    # dict.get(key, 找不到的預設值)

    def rank_hist(self):
        """ 確認手上的撲克牌點數的數量. """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """ 回傳 True 如果這組手牌有一對(pair) """
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):
        """ 回傳 True 如果這組手牌有二對(two pair)
        Note: 四張一樣，未包含在內 """
        kind = 0
        for val in self.ranks.values():
            if val >= 2:
                kind += 1
        if kind == 2:
            return True
        return False

    def has_three(self):
        """ 回傳 True 如果這組手牌有三條(three of a kind)"""
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        """ 回傳 True 如果這組手牌有順子 (straight)
        Note: 特殊情況, A > K > Q > J > 10
        """
        stra = 0
        i = 0
        for val in self.ranks.keys():
            if stra == 0:
                stra = val
                i += 1
            elif stra == 1 and val == 10:
                stra = val
                i += 1
            elif val == stra + 1:
                stra = val
                i += 1
            else:
                return False
        if i == 5:
            return True
        else:
            return False

    def has_flush(self):
        """ 回傳 True 如果這組手牌有同花(flush),
        Note: 只有手牌在5張以上才正確使用
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_fullhouse(self):
        """ 回傳 True 如果這組手牌有葫蘆(full house)
        只有在手牌5張情況下成立.
        """
        if self.has_three() and self.has_pair():
            return True
        return False

    def has_four(self):
        """ 回傳 True 如果這組手牌有鐵支(four of a kind)"""
        kind = 0
        for val in self.ranks.values():
            if val == 4:
                kind += 1
        if kind == 1:
            return True
        return False

    def has_straflush(self):
        """ 回傳 True 如果這組手牌有同花順(straight flush)
        只有在手牌5張情況下成立.
        """
        if self.has_flush() and self.has_straight():
            return True
        return False

    def classify(self):
        """ 針對5張牌的牌型做分類 """
        self.suit_hist()
        self.rank_hist()
        if self.has_pair():
            if self.has_twopair():
                if self.has_three():
                    self.label = '葫蘆'
                else:
                    self.label = '兩對'
            else:
                if self.has_three():
                    if self.has_four():
                        self.label = '鐵支'
                    else:
                        self.label = '三條'
                else:
                    self.label = '一對'
        else:
            if self.has_straight():
                if self.has_flush():
                    self.label = '同花順'
                else:
                    self.label = '順子'
            else:
                if self.has_flush():
                    self.label = '同花'
                else:
                    self.label = '散牌'


        # if self.has_straflush():
        #     self.label = '同花順'
        # elif self.has_four():
        #     self.label = '鐵支'
        # elif self.has_fullhouse():
        #     self.label = '葫蘆'
        # elif self.has_flush():
        #     self.label = '同花'
        # elif self.has_straight():
        #     self.label = '順子'
        # elif self.has_three():
        #     self.label = '三條'
        # elif self.has_twopair():
        #     self.label = '兩對'
        # elif self.has_pair():
        #     self.label = '一對'
        # else:
        #     self.label = '散牌'

if __name__ == '__main__':
    # # 製作一副撲克牌組
    # deck = Deck()
    # deck.shuffle()

    # # 發5張牌到玩家手上
    # hand = PokerHand()
    # deck.move_cards(hand, 5)
    # print(hand)
    # hand.sort()
    # hand.classify()
    # print(hand.label)

    # # 測試各種牌型
    # test_hand = PokerHand()
    # card_1 = Card(0, 1)
    # card_2 = Card(0, 10)
    # card_3 = Card(0, 11)
    # card_4 = Card(0, 9)
    # card_5 = Card(0, 12)
    # test_hand.add_card(card_1)
    # test_hand.add_card(card_2)
    # test_hand.add_card(card_3)
    # test_hand.add_card(card_4)
    # test_hand.add_card(card_5)
    # test_hand.sort()
    # print(test_hand)
    # test_hand.classify()
    # print(test_hand.label)

    # 測試各種牌型機率
    card_type = {}
    fre = 500000
    start_t = time.time()
    for i in range(fre):
        deck = Deck()
        deck.shuffle()
        probability = PokerHand()
        deck.move_cards(probability, 5)
        probability.sort()
        probability.classify()
        card_type[probability.label] = card_type.get(probability.label, 0) + 1
    end_t = time.time()
    for p in card_type:
        print(f'{p}牌型: {(card_type[p]/fre):.6%}')
    print(f'程式執行時間 {end_t - start_t}')
# %%