'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''


"""
I am building two classes that represents object either Shirt Order or Pants order from my custome clothes shop online
"""

class ShirtOrder:
    """This class creates object normal ShirtOrder"""
    company_name = "Adwan's Store"
    company_address = "adwanstore.sa"

    def __init__(self, quantity=1, color="white", text="no_text"):
        self.quantity = quantity
        self.color = color
        self.text = text
        # Object can add sleeve style

    def __str__(self):
        return 'Object ShirtOrder %g :%s :%s' % (self.quantity, self.color, self.text)


    def print_ShirtOrder(self):
        return print(f"ShirtOrder object with attributes color is {self.color}, text printed ({self.text}) and quantity set to ({self.quantity}) \n")





class PantsOrder:
    """Class PantsOrder to create PantsOrder objects with relevant attributes"""
    company_name = "Adwan's Store"
    company_address = "adwanstore.sa"

    def __init__(self, quantity=1, color="sky blue", back_pocket=False):
        self.quantity = quantity
        self.color = color
        self.back_pocket = back_pocket
        # object can add short or normal PantsOrder

    def __str__(self):
        return 'Object PantsOrder %s :%s :%s' % (self.quantity, self.color, self.back_pocket)

    def __add__(self, other):
        self.quantity = self.quantity + other.quantity
        return self.quantity


    def print_PantsOrder(self):
        return print(f"PantsOrder object with attributes color is {self.color}, quantity set to ({self.quantity}) and back pocket set to ({self.back_pocket})")




# ##########################################################

# Create one ShirtOrder
myShirtOrder = ShirtOrder(15, "blue", "Love CodingNomads")
print(myShirtOrder)

#Print ShirtOrder information nicely
myShirtOrder.print_ShirtOrder()




# Create two pants object, and add quantity of the two
myPantsOrder1 = PantsOrder()
print(myPantsOrder1)

myPantsOrder2 = PantsOrder(11, "Red", True)
print(myPantsOrder2)


# Creat object 3 and add their quanity attributes using operand override.
print(myPantsOrder1 + myPantsOrder2)

