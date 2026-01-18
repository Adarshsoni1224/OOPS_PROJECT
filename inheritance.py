# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
# Child Class inheriting from Animal
class Dog(Animal):
    # Override speak method
    def speak(self):
        return "Woof!"
# Example usage
my_dog = Dog("Buddy")
print(f"{my_dog.name} says: {my_dog.speak()}")