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
    category_name = "T-shirts"

    def __init__(self, quantity, color="white", text="no_text"):
        self.quantity = quantity
        self.color = color
        self.text = text
        # sub class can add sleeve style

    def __str__(self):
        return '%s %g :%s :%s' % (self.category_name, self.quantity, self.color, self.text)

    def print_nicely(self):
        print(f"""{self.category_name} ordered with attributes color is {self.color}, text printed ({self.text}) and quantity set to ({self.quantity})""")

    def print_category(self):
        print(f"""Category -->{self.category_name}""", end ="")



class TrouserOrder:
    """Class TrouserOrder to create TrouserOrder objects with relevant attributes"""
    company_name = "Adwan's Store"
    company_address = "adwanstore.sa"
    category_name = "Trousers"

    def __init__(self, quantity, color="blue", back_pocket=False):
        self.quantity = quantity
        self.color = color
        self.back_pocket = back_pocket
        # sub class can add short not necessiraly pants

    def __str__(self):
        return '%s %g :%s :%s' % (self.category_name, self.quantity, self.color, self.back_pocket)

    def __add__(self, other):
        self.quantity = self.quantity + other.quantity
        return self.quantity

    def print_nicely(self):
        print(f"{self.category_name} created with attributes color {self.color}, quantity set to ({self.quantity}) and back pocket set to ({self.back_pocket})")

    def print_category(self):
        print(f"""Category -->{self.category_name}""", end="")




