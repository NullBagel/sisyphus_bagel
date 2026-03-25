import random

MAX_PLAYERS = 2

def form_deck():
    HEART = chr(9829)
    CLUBS = chr(9827)
    SPADE = chr(9824)
    DIAMOND = chr(9830)
    
    num_card = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = [HEART, CLUBS, SPADE, DIAMOND]
    
    deck = []
    for i in num_card:
        for s in suits:
            card = i + s
            deck.append(card)
            
    return deck

def remove_dealt_cards(deck):
    deck.pop(0)
    deck.pop(0)

def dealing(MAX_PLAYERS, deck):
    blackjack_table = {}
    
    for i in range(MAX_PLAYERS):
        blackjack_table[f"Player {i+1}"] = [deck[0], deck[1]]
        remove_dealt_cards(deck)
        # print(blackjack_table)
    
    blackjack_table["Dealer"] = [deck[0], deck[1]]
    remove_dealt_cards(deck)
    # print(blackjack_table)
    return blackjack_table

def calculate_initial_points(blackjack_table):
    blackjack_points_dict = {}
    
    for player, cards in blackjack_table.items():
        first_card = cards[0][:-1]
        second_card = cards[1][:-1]
        
        if first_card in ["J","Q","K"]:
            first_card = 10
        elif first_card == "A":
            first_card = 11
    
        if second_card in ["J","Q","K"]:
            second_card = 10
        elif second_card == "A":
            second_card = 11
        
        blackjack_points = int(first_card) + int(second_card)
        blackjack_points_dict[player] = blackjack_points
    return blackjack_points_dict

def count_points(player_hand):
    player_points = 0
    aces = 0

    for i in range(len(player_hand)):
        rank = player_hand[i][:-1]

        if rank == "A":
            player_points += 11
            aces += 1

        elif rank in ["J","Q","K"]:
            player_points += 10

        else:
            player_points += int(rank)

        while player_points > 21 and aces > 0:
            player_points -= 10

    return player_points

def dealt_blackjack_check(blackjack_points_table):
    for player, points in blackjack_points_table.items():
        if points == 21:
            print(f"{player} has blackjack!")

def blackjack_game_core(MAX_PLAYERS):
    deck = form_deck()
    random.shuffle(deck)
    blackjack_table = dealing(MAX_PLAYERS, deck)
    print(blackjack_table)
    blackjack_points_table = calculate_initial_points(blackjack_table)
    dealt_blackjack_check(blackjack_points_table)

    for player in range(len(blackjack_table)-1):
        player_points = blackjack_points_table[f"Player {player+1}"]
        cards = blackjack_table[f"Player {player+1}"]
        print(f"Player {player+1}'s Turn")

        while player_points < 21:
            print(f"Player {player+1}'s points: {player_points}")
            player_input = input("Hit? Y/N").upper()

            if player_input == "Y":
                cards.append(deck[0])
                deck.pop(0)
                print(cards)
                player_points = count_points(cards)
                print(player_points)
                blackjack_points_table[f"Player {player+1}"] = player_points
            
            elif player_input == "N":
                break

            else:
                print("Please only input Y or N")

blackjack_game_core(MAX_PLAYERS)
