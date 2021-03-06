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
I am building two classes that represents object either T-shirt Order or Pants order
We are a company that mass produce t-shirts and pants with custom message printing
"""


class TShirt:
    """This class creates object normal TShirt"""
    brand_tag = "Adwan Online"
    washing_type = "dry clean only"

    def __init__(self, quantity, color="white", text="no_text"):
        self.quantity = quantity
        self.color = color
        self.text = text
        # sub class can add sleeve style

    def __str__(self):
        return 'Object TShirt %g :%s :%s' % (self.quantity, self.color, self.text)

    def print_TShirt(self):
        return print(f"TShirt object with attributes color is {self.color}, text printed ({self.text}) and quantity set to ({self.quantity}) \n")


class TrouserOrder:
    """Class TrouserOrder to create TrouserOrder objects with relevant attributes"""
    company_name = "Adwan's Store"
    company_address = "adwanstore.sa"

    def __init__(self, quantity, color="blue", back_pocket=False):
        self.quantity = quantity
        self.color = color
        self.back_pocket = back_pocket
        # sub class can add short not necessiraly pants

    def __str__(self):
        return 'Object TrouserOrder %g :%s :%s' % (self.quantity, self.color, self.back_pocket)

    def __add__(self, other):
        self.quantity = self.quantity + other.quantity
        return self.quantity

    def print_TrouserOrder(self):
        return print(f"TrouserOrder object with attributes color is {self.color}, quantity set to ({self.quantity}) and back pocket set to ({self.back_pocket})")


# ##########################################################
# Create one TShirt
myTShirt = TShirt(15, "Green", "Love CodingNomads")
print(myTShirt)

# Print TShirt information nicely
myTShirt.print_TShirt()


# Create two pants object, and add quantity of the two
myTrouserOrder1 = TrouserOrder(4, "white", True)
print(myTrouserOrder1)

myTrouserOrder2 = TrouserOrder(11, "Red", True)
print(myTrouserOrder2)


# Creat object 3 and add their quanity attributes using operand override.
print(myTrouserOrder1 + myTrouserOrder2)

