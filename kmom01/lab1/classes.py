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
