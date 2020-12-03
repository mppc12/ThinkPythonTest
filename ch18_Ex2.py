# %%
from ch18_inheritance import Deck, Hand

class Deck_2(Deck):

    def deal_hands(self, num_hands, num_cards):
        """ Represents 初始建立幾位玩家，手上分到幾張牌
        num_hands: 幾位玩家
        num_cards: 每位玩家分到幾張牌
        列印出 每位玩家手上的牌
        Question: 如何將牌平均分給每位玩家 (一次發一張)；
        超過52張牌會發出 IndexError
        """
        self.shuffle()
        for i in range(num_hands):
            player = f'玩家{i+1}'
            hand = Hand(player)
            print(hand.label)
            self.move_cards(hand, num_cards)
            print(hand)

def main():
    deck = Deck_2()
    deck.deal_hands(4, 13)

if __name__ == "__main__":
    main()
# %%
