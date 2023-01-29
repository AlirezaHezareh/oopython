
class cat(): #class
    """
    class för cat 
    """
    nr_of_paws = 4
    def __init__(self, eye_color, name, lives_left): 
        """
        funktion som innehåller alla parametrar för classen cat
        """
        self.eye_color = eye_color
        self.name = name
        self.lives_left = lives_left
        self.nr_of_paws = 4

    def __str__(self): 
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
        return f"My cat's name is {self.name} and has {self.eye_color} eyes."
    
    def description(self):
        return f"My cat's name is {self.name}, has {self.eye_color} eyes and {self.lives_left} lives left to live."

class duration(): #class för extercise 1.7
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total = (self.hours * 3600) + (self.minutes * 60)+(self.seconds)
    def __str__(self):
        hh = self.hours
        mm = self.minutes
        ss = self.seconds
        return f"{hh}-{mm}-{ss}"
    def display(self):
        hh = self.hours
        mm = self.minutes
        ss = self.seconds
        toReturn = f"{hh}-{mm}-{ss}"
        return toReturn
    def duration_to_sec(self, string):
        self.string =  string.replace('-', '')
        self.hours = int(string[:2]) * 3600
        self.minutes = int(self.string[1:3]) * 60
        self.seconds = int(string[-2:])
        self.total = self.hours + self.minutes + self.seconds
        return self.total
    def __add__(self, other):
        selfSTR = self.total 
        other += selfSTR
        return other
    def __iadd__(self, other):
        hoursTogether = []
        for i in str(self):
            if i.isdigit():
                hoursTogether.append(i)
            else:
                print(str(hoursTogether))
        print(hoursTogether)
        


duration1 = duration(30, 6, 13) 
