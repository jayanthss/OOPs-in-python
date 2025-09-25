# In Python, to declare an Object-Oriented Program (OOP), we use the keyword "class".
# A class is like a blueprint for creating objects.

# 🔑 Important:
# - "self" in Python refers to the current object (similar to "this" in JavaScript or Java).
# - "self" must be the first parameter in methods if we want to access variables inside the class.


class ClassName:

    # constructor
    def __init__(self, input_argument_1, input_argument_2):
        # Assigning variables from input arguments
        self.input_argument_1 = input_argument_1
        self.input_argument_2 = input_argument_2
        # You can add more variables here

    # Methods (functions inside a class)
    # Note: "self" is required to access variables defined in the constructor
    def function1(self):
        # Example logic: access constructor variables
        return f"Function1: {self.input_argument_1}"

    def function2(self):
        # Another example
        return f"Function2: {self.input_argument_2}"

    def function3(self):
        # Example: combine both
        return f"Function3: {self.input_argument_1 + self.input_argument_2}"

    # So on...


# Example usage:
obj = ClassName(10, 20)

print(obj.function1())  # Output: Function1: 10
print(obj.function2())  # Output: Function2: 20
print(obj.function3())  # Output: Function3: 30
