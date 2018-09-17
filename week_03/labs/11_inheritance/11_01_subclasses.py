'''
Build on 10_03_freeform_classes from the section on Classes, Objects and
Methods.
Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in 10_03_freeform_classes.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

# Here we need to import package orders which has the base classes from previous exercise
from orders import TrouserOrder, TShirt


class LongSleeveShirt(TShirt):

    # Class variable long sleeve because all objects must have long sleeve to be in this class
    long_sleeve = True
    category_name = "Long Sleeves Shirts"

    def __init__(self, quantity, color, text="no_text", sleeve_button=False):
        TShirt.__init__(self, quantity, color, text)
        self.sleeve_button =  sleeve_button

    def __str__(self):
        return f"""Object {self.category_name}: {self.quantity}, {self.color},  {self.text}, {self.sleeve_button}"""


    # def print_nicely(self):
    #     TShirt.print_nicely(self)


    def print_category(self):
        TShirt.print_category(TShirt)
        print(f"-->{self.category_name}")





class ShortsOrder(TrouserOrder):
    """ Class to create Shorts Order, shorts are nothing but shortened version of torusers"""
    is_short = True
    category_name = "Shorts"

    def __init__(self, quantity, color, back_pocket):
        TrouserOrder.__init__(self, quantity, color, back_pocket)


# Dynamically extending the category string based on the subclass level. Cool stuf!!
    def print_category(self):
        TrouserOrder.print_category(TrouserOrder)
        print(f"-->{self.category_name}", end="")



class CargoShorts(ShortsOrder):
    """Class to create Cargo Shorts which inherits ShortOrder class"""

    # We need this attribute to highlight the fact all cargo shorts must have large pockets
    is_cargo_short = True
    category_name = "Cargo Shorts"

    def __init__(self, quantity, color, back_pocket, pocket_count=2):
        ShortsOrder.__init__(self, quantity, color, back_pocket)
        self.pocket_count = pocket_count


    def __str__(self):
        return f"""Object {self.category_name}: {self.quantity}, {self.color},{self.back_pocket}, {self.pocket_count} """


    def print_category(self):
        ShortsOrder.print_category(ShortsOrder)
        print(f"-->{self.category_name}")


# End of code here.

# ###############Testing Script only ##############################
# create object long sleeve order and print
myLongSleeve = LongSleeveShirt(14, "blue")
myLongSleeve.print_nicely()
myLongSleeve.print_category()

print() # Print empty line seperation

# Create object of sub sub-class (3 level!), and print
myCargoShort = CargoShorts(15, "white", True)
myCargoShort.print_nicely()
myCargoShort.print_category()
