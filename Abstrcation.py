# Abstraction in OOPs
# Abstraction means hiding the complex internal implementation
# and showing only the essential features to the user.

# ✅ Real-life Example:
# Think of the YouTube App.
#
# Abstracted View (What user sees):
# - You click a thumbnail → video plays
# - Double-tap on screen → video skips 10 seconds
# - Press like button → increases like count
#
# Hidden View (What user does NOT see):
# - How video data is fetched from servers
# - How buffering and streaming protocols work
# - How likes are stored in the database
#
# The user only interacts with simple features (abstraction),
# while the complex code runs in the background.


# in python there is an module to achive abstract layer called "ABC ,  abstractmethod"

"""NOTE: Abstract methods are declared in the abstract class but have no implementation; subclasses are required to provide their own implementation."""

# import the module , To achive abstract class you must use @abstractmethod before every methods

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")


class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle engine started.")

    def stop(self):
        print("Motorcycle engine stopped.")


# vehicle = Vehicle() # This would raise a TypeError
car = Car()
car.start()  # Car engine started.
motorcycle = Motorcycle()
motorcycle.stop()  # Motorcycle engine stopped.
