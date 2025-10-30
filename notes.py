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
    def __init__(self, breed = "rotweiler", name = "cupcake", age = 5, favorite_food = "babies"):
        """Initialize a new Dog with breed, name, age, and favorite food"""
        self.breed = breed
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def __str__(self):
        """return a string representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.breed} dog who loves to eat {self.favorite_food}"

    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says GRRR, woof, Woof!!"
    
    def hunger(self):
        """
        dog asks for food politly
        """
        return f"yo, give me FOOD now son"
    
    def birthday(self):
        """
        Celebrates the dog's birthday
        """
        self.age += 1
        print(f"Celebrating {self.name}'s birhtday, they are now {self.age} years old.")

    def change_favorite_food(self, new_food):
        """
        Change the favorite food of the dog
        """
        old_food = self.favorite_food
        self.favorite_food = new_food
        print(f"{self.name} use to love {old_food} and now loves {self.favorite_food}")






my_dog = Dog("golden retriever", "mack", 4, "cheez its")
default_dog = Dog()
print() 
print() 
print(my_dog)
print(my_dog.bark())
print(my_dog.hunger())
print() 
print() 
print(default_dog)
print() 
print() 
enggy_dog = Dog("black and white", "peluchin", 13, "rice")
aaron_dog = Dog("peach and white", "dumbo", favorite_food="anything edible")

print(enggy_dog)
print(aaron_dog)

print() 

print(enggy_dog.bark())
aaron_dog.birthday()

print(aaron_dog)
print() 
print() 
