import random

FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class Card(object):
    """A card has a face and suit."""
    def __init__(self, face, suit):
        assert (face in FACES and suit in SUITS) # assert : 사용자가 잘입력했나 확인
        self.face = face
        self.suit = suit

    def __str__(self):
        article = "a "
        if self.face in [8, "Ace"]: article = "an "
        return article + str(self.face) + " of " + self.suit

    def value(self):
        """Returns the face value of the card."""
        if type(self.face) == int:
            return self.face
        if self.face == "Ace":
            return 11
        return 10

class Deck(object):
    """A deck of cards."""
    def __init__(self):
        """Create a deck of 52 cards and shuffle them."""
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards) # shuffle로 랜덤 제공

    def draw(self):
        """Draw the top card from the deck."""
        return self.cards.pop()

def hand_value(hand):
    """Computes the value of a hand of cards."""
    value = 0
    for card in hand:
        value += card.value()
    return value

def ask_yesno(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("I beg your pardon!") # 잘못입력해써

def blackjack():
    """Play one round of Blackjack.
    Returns 1 if player wins, -1 if dealer wins, and 0 for a tie."""
    deck = Deck()

    dealer = []
    player = []

    # initial two cards
    player.append(deck.draw())
    print("You are dealt", player[0])
    dealer.append(deck.draw())
    print("Dealer is dealt a hidden card")
    player.append(deck.draw())
    print("You are dealt", player[1])
    dealer.append(deck.draw())
    print("Dealer is dealt", dealer[1])
    print("Your total is", hand_value(player))

    # player's turn to draw cards
    while hand_value(player) < 21:
        if not ask_yesno("Would you like another card? (y/n) "):
            break

        player.append(deck.draw())
        print("You are dealt", player[-1])
        print("Your total is", hand_value(player))

    # if the player's score is over 21, the player loses immediately.
    if hand_value(player) > 21:
        print("You went over 21! You lost!")
        return -1

    print("The dealer's hidden card was", dealer[0])
    while hand_value(dealer) < 17:
        dealer.append(deck.draw())
        print("Dealer is dealt", dealer[-1])

    print("The dealer's total is", hand_value(dealer))

    # summary
    player_total = hand_value(player)
    dealer_total = hand_value(dealer)
    print("\nYour total is", player_total)
    print("The dealer's total is", dealer_total)

    if dealer_total > 21:
        print("The dealer went over 21! You win!")
        return 1

    if player_total > dealer_total:
        print("You win!")
        return 1

    if player_total < dealer_total:
        print("You lost!")
        return -1

    print("You have a tie!")
    return 0

def game_loop():
    print("Welcome to Blackjack 101!")
    while True:
        blackjack()
        if not ask_yesno("\nPlay another round? (y/n) "):
            break

game_loop()
