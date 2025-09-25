# Access Modifiers in OOPs (Python)

# Access modifiers define how and where the members (variables/methods) of a class
# can be accessed in your program.

# Example: You have a variable (called 'number'), you may want to allow only specific
# classes or methods to use it. Access modifiers help in controlling this access.

"""
Types of Access Modifiers in Python:
--> Public      : (default) Can be accessed from anywhere.
--> Protected   : (convention: one underscore "_") Should be accessed only within the same
                  class and subclasses (child classes).
                  --> Note: Python doesn’t enforce this strictly, it’s just a convention.
--> Private     : (two underscores "__") Name mangling is used, so it can only be accessed
                  inside the class where it is defined.
"""


class AccessModifiers:

    # constructor
    def __init__(self, input_arguments_1, input_arguments_2):
        self.input_arguments_1 = input_arguments_1  # public variable
        self._protected_var = input_arguments_2  # protected variable
        self.__private_var = 42  # private variable

    # Public method - can be accessed anywhere
    def public_method(self):
        print("This is a public method.")

    # Protected method - meant to be used within the class or subclasses
    def _protected_method(self):
        print("This is a protected method.")

    # Private method - can only be accessed inside this class
    def __private_method(self):
        print("This is a private method.")


# Example usage
obj = AccessModifiers(10, 20)

# Public members
# print(obj.input_arguments_1)      # ✅ Accessible
# obj.public_method()               # ✅ Accessible

# Protected members (can still be accessed, but should not be used outside class/subclass)
# print(obj._protected_var)         # ⚠️ Convention says "don’t use directly"
# obj._protected_method()           # ⚠️ Same as above

# Private members (Python uses name mangling: _ClassName__member)
print(obj.__private_var)  # ❌ AttributeError
obj.__private_method()  # ❌ AttributeError: 'AccessModifiers' object has no attribute '__private_var'
print(obj._AccessModifiers__private_var)  # ✅ Possible (but not recommended)
