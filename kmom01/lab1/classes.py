
"""
mudole docstring oopython lab1 v2 alhz22
made for use in lab1 BTH exercise as a class mudole
"""
class Cat():
    """
    class med namn Cat
    """
    nr_of_paws = 4
    def __init__(self, eye_color, name, lives_left):
        """
        funktion som innehåller alla parametrar för classen Cat
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
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
        namestr = f"My cat's name is {self.name}"
        eyecolor_str = f", has {self.eye_color} eyes "
        lives_str = f"and {self.lives_left} lives left to live."
        to_return = f"{namestr}{eyecolor_str}{lives_str}"
        return to_return
class Duration():
    """
    class för extercise 1.7
    """
    def __init__(self, hours, minutes, seconds):
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
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
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
        hh = self.hours
        mm = self.minutes
        ss = self.seconds
        if mm < 10:
            mm = f"0{mm}"
        to_return = f"{hh}-{mm}-{ss}"
        return to_return
    def duration_to_sec(self, other):
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
        self.hours = int(other[:2]) * 3600
        self.minutes = int(other[3:5]) * 60
        self.seconds = int(other[-2:])
        self.total = self.hours + self.minutes + self.seconds
        return self.total
    def __add__(self, other):
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
        if isinstance(other, Duration):
            self.total += other.total
        return self.total
    def __iadd__(self, other):
        """
        funktion som returnerar svar meningen i form av class.
        Man kan använda 'str()' så ändras det till string typ.
        """
        if isinstance(other, Duration):
            hours_together = self.hours + other.hours
            minut_together = self.minutes + other.minutes
            secontogether = self.seconds + other.seconds
        return f"{hours_together}-{minut_together}-{secontogether}"
    def __lt__(self, other):
        """
        funktion som gemförar två duration och ger svar i form
        av boolean.
        """
        if isinstance(self, Duration):
            selff = self.hours
        if isinstance(other, Duration):
            other = int(other.hours)
        return int(selff)<int(other)
