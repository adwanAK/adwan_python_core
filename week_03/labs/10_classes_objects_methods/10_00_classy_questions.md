## Classes and OOP

- What is a class?
    it is like template or blueprint of an object. It has initials values,
    attributes and states of the object.

- How do you define a new class called `MyFirstClass`?
    class MyFirstClass:
        """Represents my class and it attributes and methods"""


- How do you create an object of the class `MyFirstClass`?

    my_class = MyFirstClass()

- What is instantiation?
    Instantiation or initilization is the creation of new instance of the object.


- What are attributes?
    it is the class or object values such color and model for Object car.

- What does it mean when an object is embedded?
    It is an object created seperately then placed into another object.They
    are self contained and can work indepenently. It has an advantage to be
    transfered to another location or embed in another object without beraking it.


- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?
    copy.copy returns only shallow copy wherease deepcopy returns deep copy. The
    difference between shallow and deep is that the former constructs new object with its
    and inserts references that are only found the original object. Deep copy constructs the
    compund object and recursively inserts copies of objects found the original.

- What is the difference between a pure function and a modifier?
    Pure function does not make any change to objects attributes that got passed to it.
    Modifier on the other hand causes changes to object's attributes that passed to it as parameters.

- What is object-oriented programming?t
    OOP is  organized around objects rather than actions.
    It is programming in way resembles real life objects.

## Methods

- What is a method?
    It is simply a function but associated with an object.

- How is a method different than a function?
    A method is defined inside class. Function can be defined outside class.

- What is invocation?
    It is calling a function.

- What is the `__init__` method and what is it used for?
    "init" from the word initialize. It is invoked when we objec instantiated.
    Basically, it takes the parameters if passed and put values in class attributes.

- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year`.
    def __init__(self, make="", model="", year=0):
        self.make = make
        self.model = model
        self.year = year


- How do `__init__` methods handle variable arguments?
    Basically, if argument is passed it stores them in the object's "self" corresponding
    attributes.
    Arguments can be optional or mandatory. It can also take one argument and leave others
     unchanged.

- What is the `__str__` method used for?
    It is special method that returns string representation of the object.

- How do you use a `__str__` method?
    You use it by calling function print on the object. __str__ then gets invoked
    and will print its content which is supposed to be the object information string..

- What is operator overloading?
    It is changing the behavior of an operator such as +,- ..etc when used with
    objects that have specified this in __add__ method of object's class.

- What is an example of operator overloading
    Take the subtract operator (-), we want to change it's behavior when
    used between two objects of the same class.
    def __sub__(self, other):
        date_difference = self.getDate() - self.getDate()

    print(objec1 - objec2)

    This will trigger __sub__ which will do something store age difference.



## TYPE-BASED DISPATCH?

- What is polymorphism?
    It is the abilitiy of an objec to adapt the code to the type of data
    it is processing.

- Why is polymorphism beneficial?
    It facilitate code reusability.
