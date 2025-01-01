# import DeckOfCards module
from DeckOfCards import *

# introduce the user
print("Welcome to Black Jack! Best of Luck!")
print()

# name deck "deck"
deck = DeckOfCards()

# loop game until they want to quit playing
while True:
    
    # Ace counter
    u_ace = 0
    d_ace = 0

    # print deck
    print("Deck before shuffle:")
    print()
    deck.print_deck()
    print()
    
    # shuffle deck and print again
    deck.shuffle_deck()
    print("Deck after shuffle:")
    print()
    deck.print_deck()
    print()
    
    # deal 2 cards to the user and show them to him
    user_card1 = deck.get_card()
    user_card2 = deck.get_card()
    print("Card 1:", user_card1.face, "of", user_card1.suit)
    print()
    print("Card 2:", user_card2.face, "of", user_card2.suit)
    print()
    
    # increment ace counter if ace
    if user_card1.face == "Ace":
        u_ace += 1
    if user_card2.face == "Ace":
        u_ace += 1
    
    # deal 2 cards to the dealer
    dealer_card1 = deck.get_card()
    dealer_card2 = deck.get_card()
    
    # increment ace counter if ace
    if dealer_card1.face == "Ace":
        d_ace += 1
    if dealer_card2.face == "Ace":
        d_ace += 1
    
    # calculate dealer score
    d_score = dealer_card1.value + dealer_card2.value
    
    # check if over 21
    if d_score > 21:
        if d_ace >= 1:
            d_score -= 10
            d_ace -= 1
    
    # calculate and print user score
    score = user_card1.value + user_card2.value
    
    # check if over 21
    if score > 21:
        if u_ace >= 1:
            score -= 10
            u_ace -= 1
    
    print("Your score is", score)
    print()
    
    
    # counter for card number
    card_num = 3
    d_card_num = 3
    
    # continue while users wants to keep hitting
    hit = 'y'
    while hit == 'y':
    
        # ask if they want to hit
        hit = input("Would you like a hit? (y/n): ")
        print()
        
        # give them another card if they hit and calculate score
        if hit == 'y':
            
            # create variable for drawing a card
            draw_card = deck.get_card()
            
            print("Card " + str(card_num) + ":", draw_card.face, "of", draw_card.suit)
            print()
            
            # increment ace counter if ace
            if draw_card.face == "Ace":
                u_ace += 1
            
            score += draw_card.value
            
            # check if over 21
            if score > 21:
                if u_ace >= 1:
                    score -= 10
                    u_ace -= 1
            
            print("Your score is", score)
            print()
            
            # increase counter
            card_num += 1
            
            # end if score exceeds 21 (check 2x in odd case)
            if score > 21:
                if u_ace >= 1:
                    score -= 10
                    u_ace -= 1
            if score > 21:
                print("You busted, you lose!")
                print()
                break
            
        # if user wants to stop hitting show dealers score
        else:
            print("Dealer card 1:", dealer_card1.face, "of", dealer_card1.suit)
            print()
            print("Dealer card 2:", dealer_card2.face, "of", dealer_card2.suit)
            print()
            
            # if dealer score is under 17 they keep hitting
            if d_score < 17:
                while d_score < 17:
                    
                    # update card
                    draw_card = deck.get_card()
    
                    print("Dealer hits. Dealer card " + str(d_card_num) + ":", draw_card.face, "of", draw_card.suit)
                    print()
                    
                    # increment ace counter if ace
                    if draw_card.face == "Ace":
                        d_ace += 1
                    
                    # add to dealer score
                    d_score += draw_card.value
                    
                    # increase counter
                    d_card_num += 1
                    
                    # check if over 21 (check 2x in odd case)
                    if d_score > 21:
                        if d_ace >= 1:
                            d_score -= 10
                            d_ace -= 1
                            if d_score > 21:
                                if d_ace >= 1:
                                    d_score -= 10
                                    d_ace -= 1
                    
            # display dealer score
            print("Dealer score is", d_score)
            print()
            
            # dealer busts if they exceed 21
            if d_score > 21:
                print("The dealer busted! You win!")
                print()
            else:
                # display final results
                if d_score > score:
                    print("The dealer's score is higher, you lose!")
                    print()
                elif d_score == score:
                    print("It's a tie! So you lose.")
                    print()
                else:
                    print("Your score is higher, you win! Congratulations!!!")
                    print()
                    
    # ask the user if they want to play again      
    again = input("Would you like to play again? (y/n): ")
    print()
    if again == 'y':
        continue
    else:
        break
                
            