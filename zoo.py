from animals import Penguin, PaintedDog
from habitats import Aquarium

# Create a penguin
bob = Penguin("Bob")
bob.walk()
bob.swim()


# Create painted dog instance
ralph = PaintedDog("Ralph")

# Create a habitat
seaworld = Aquarium("Sea World")
seaworld.add_swimmer_pythonic(bob) # or seaworld.add_swimmer_type_check(bob)
seaworld.add_swimmer_pythonic(ralph) # or seaworld.add_swimmer_type_check(ralph)

for animal in seaworld.animals:
  print(f'{animal} lives in Sea World')
