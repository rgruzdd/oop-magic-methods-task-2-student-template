class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        string = self.name + ' ' + 'bird can fly'
        return string

    def walk(self):
        string = self.name + ' ' + 'bird can walk'
        return string

    def __str__(self):
        string = str(self.name) + ' ' + 'bird can walk and fly'
        return string

    def __getattr__(self, name):
        return lambda: print('AttributeError: ' + self.name + ' object has no attribute ' + "'" + name + "'")

class FlyingBird:
    def __init__(self, name, ration = 'grains'):
        self.name = name
        self.ration = ration

    def fly(self):
        string = self.name + ' ' + 'bird can fly'
        return string

    def walk(self):
        string = self.name + ' ' + 'bird can walk'
        return string

    def eat(self):
        string = 'It eats mostly' + ' ' + self.ration

        return string

    def __str__(self):
        string = self.name + ' ' + 'bird can walk and fly'
        return string

    def __getattr__(self, name):
        return lambda: print('AttributeError: ' + "'" + self.name + "'" + ' object has no attribute ' + "'" + name + "'")


class NonFlyingBird:

    def __init__(self, name, ration = 'fish'):
        self.name = name
        self.ration = ration

    def walk(self):
        string = self.name + ' ' + 'bird can walk'
        return string

    def eat(self):
        string = 'It eats mostly' + ' ' + self.ration
        return string

    def swim(self):
        string = self.name + ' ' + 'bird can swim'
        return string

    def __str__(self):
        string = self.name + ' ' + 'bird can walk and swim'
        return string

    def __getattr__(self, name):
        return lambda: print('AttributeError: ' + self.name + ' object has no attribute ' + "'" + name + "'")



class SuperBird:

    def __init__(self, name, ration = 1):
        self.name = name

    def fly(self):
        string = self.name + ' ' + 'bird can fly'
        return string

    def walk(self):
        string = self.name + ' ' + 'bird can walk'
        return string

    def eat(self):
        string = 'It eats mostly fish'
        return string

    def swim(self):
        string = self.name + ' ' + 'bird can swim'
        return string

    def __str__(self):
        string = self.name + ' ' + 'bird can walk, swim and fly'
        return string

    def __getattr__(self, name):
        return lambda: print('AttributeError: ' + self.name + ' object has no attribute ' + "'" + name + "'")




