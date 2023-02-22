from die import Die

class Hand():
    
    """ Om man skickar in ett argument till parmetern
     i konstruktorn, så ska argumentet vara en lista som 
     innehåller fem heltal. De heltalen ska användas för att 
     skapa en tärning med varje heltal. Om man inte skickar med 
     ett argument så ska dice listan få fem dice objekt med 
     slumpade värden. """
    def __init__(self, dice=[0]):
        self.dice = dice
        self.indexes = []
            #get_name = Die.get_name(i)
            #self.dice.append(get_name)
            #print(self.dice)
    def roll(self, indexes=None):
        if indexes is not None:
            print('if')
            for i in range(5):
                self.dice.append(indexes[i])
        else:
            for i in range(5):
                print('else')
                self.dice.append(Die.get_value(Die()))
            self.dice.pop(0)
        return self.dice
    def __str__(self):
        return str(self.dice)
            



objekt = Hand()
hand = [3,3,3,3,3]
""" 
print('oj', hand)
Die.roll() """
""" 
objekt_hand = Hand(hand)
print('objekt hand', Hand()) 
print('objekt', Die(hand))
                self.dice.append(Die.roll())
print('hand',hand)"""
print('od', objekt.dice)
print(objekt.roll())
print('od', objekt.dice)
