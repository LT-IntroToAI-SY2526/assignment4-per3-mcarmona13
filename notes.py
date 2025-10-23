# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """
    A simple Dog class to learn OOP
    
    Atrributes:
        breed - the color of the dogs fur
        name - the name of the dog
        age - the age of the dog
        favorite_food - the dog's favorite food
    """
    def __init__(self, breed, name, age, favorite_food):
        """Initialize a new Dog with breed, name, age, and favorite food"""
        self.breed = breed
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def __str__(self):
        """return a string representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.breed} dog who loves {self.favorite_food}"

    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says GRRR, woof, Woof!!"
    
    def hunger(self):
        """
        dog asks for food politly
        """
        return f"yo, give me FOOD now son"





my_dog = Dog("golden retriever", "mack", 4, "cheez its")
print(my_dog)

print() 

print(my_dog.bark())
print(my_dog.hunger())
