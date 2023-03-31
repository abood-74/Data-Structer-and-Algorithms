"""Given is an ordered deck of n cards numbered 1 to n with card 1 at the top and card nat the bottom.

    The following operation is performed as long as there are at least two cards in the deck:
    
    Throw away the top card and move the card that is now on the top of the deck to the bottom of the deck.
    Your task is to find the sequence of discarded cards and the last remaining card.
"""


from queue_array_based import Queue
def card_game(n):
    cards = []
    q = Queue(n)
    for i in range(1,n+1):
        q.enqueue(i)

    while len(q) > 1 :
        cards.append(q.dequeue())
        q.enqueue(q.dequeue())
    return cards, q.first()
    
    

if __name__ == "__main__":
    print(card_game(19))    
    print(card_game(10))
    print(card_game(4))
    