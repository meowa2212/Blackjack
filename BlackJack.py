'''
Wojciech Gorzynski
09-06-2025 v1

My implementation of blackjack for use in a discord bot.
'''

from DeckOfCards import Deck


class Blackjack(Deck):
    def __init__(self, bet):
        super().__init__()
        self.shuffle()
        self.bet = bet
        self.used_cards = []
        self.dealer_cards = []
        self.dealer_finished = False
        self.player_finished = False
    
    def calculate_score(self, dealer = False):
        if dealer:
            values = [x[:-1] for x in self.dealer_cards]
        else:
            values = [x[:-1] for x in self.used_cards]
            
        score_small = 0
        score_big = 0
        for value in values:
            if value in ["K", "Q", "J"]:
                score_small += 10
                score_big += 10
            if value == "A":
                score_small += 1
                score_big += 11
            else:
                score_small += int(value)
                score_big += int(value)
        return score_small, score_big
    
    def dealer(self):
        score_small, score_big = self.calculate_score(1)
        if score_small >= 17 or 17 <= score_big <= 21
            self.dealer_finished = True
        else:
            self.dealer_cards.append(self.last_card(1))
            if min(score_small, score_big) > 21:
                self.dealer_finished = True
        
    def player(self, choice):
        score_small, score_big = self.calculate_score()
        
                





if __name__ == "__main__":
    game = Blackjack(100)
    game.calculate_score()