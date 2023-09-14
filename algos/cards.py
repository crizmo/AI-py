import itertools, random

# it create a list of tuples
deck = list(itertools.product(range(1,14),['SPADE','HEART','DIAMOND','CLUB']))

random.shuffle(deck) #shuffle
print("Your Cards are:")

for i in range(5):
    print(deck[i][0], "\t of ", deck[i][1])
