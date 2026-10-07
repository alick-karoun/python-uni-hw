import random
import statistics
import sys

coin = random.choice(["heads", "tails"])
coin = random.randint([1, 2])

cards= ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
print(coin)

#to calc average
print(statistics.mean([100,90]))

