# Inheritance In OOP's

# Inheritance Means variables or Methods(function) can be accessed to other class(sub-class)
# In-otherwords using variables or Methods(function) of parent class is used by child class


class parent:

    def __init__(self, input_1, input_2):
        self.input1 = input_1
        self.input2 = input_2

    def function_1(self):
        return f"I'm Learning Inheritance and input_1_2 = {self.input1,self.input2}"

    def function_2(self):
        return f"OOP's Concept is return and input_1_2 = {self.input1,self.input2}"


# In python to Inherite , you must pass the parent class name to child class ex: "class child(parent)"


class child(parent):
    # Printing all variables and functions in child class

    def parent_methods_variables(self):

        # Note : If self is not used while accessing the parent class variables and methods, you get an error must use "self.variable & self.methods"

        print(self.input1)
        print(self.input2)
        print(self.function_1())
        print(self.function_2())


class grand_child(child):
    def access_parent_variable_from_child(self):
        print(self.input2)


parent_class = parent(10,20)
print(parent_class.function_1()) #output: I'm Learning Inheritance and input_1_2 = (10, 20)


child_class = child(10,20)
child_class.parent_methods_variables()
# output :
#           10
#           20
#           I'm Learning Inheritance and input_1_2 = (10, 20)
#           OOP's Concept is return and input_1_2 = (10, 20)

grand_child_class = grand_child(10, 20)
grand_child_class.access_parent_variable_from_child()  # output : 20
