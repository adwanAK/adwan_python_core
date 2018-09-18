# Files

Read through chapter ["Case Study: Word Play"](http://greenteapress.com/thinkpython2/html/thinkpython2010.html) as well as chapter ["Files"](http://greenteapress.com/thinkpython2/html/thinkpython2015.html) from
Allen B. Downey's Think Python 2e book.

- How do you open a file in read mode and print the first line?
    f = open("filename", "r")
    first_line = f.readline()
    f.close()

- How can you use a for loop to iterate through the words of a file?
    with open("fileinput") as f:
        word_list = list(f.read().split(" ")) # or split by any delimeter


- What does it mean when a program is persistent?
    Type of programs that run for a long time such as OS where they keep
    at least some its data stored in permenant storage i.e. hard drive.

- How do you open a file in write mode?
    f=open("file_name", "w")

- Practice using f-strings as a replacement for the .format() method
    f"Hello! My name is {self.name} and my age is {self.age}""

- What is the difference between a relative path and an absolute path?
    relative path corresponds to immediate folder current program in. Absolut is full path.

- What are some IOExceptions that you might encounter? How are they generated?
    ZeroDeivision, IOError, KeyboardInterrupt, EOFError

- What is a try statement used for?
    It used for trying execution lines of codes and then raise exception.

- What is an except statement used for?
    Except will "catch" the raised excetption accordingly.

- Can you have a try without an except? Can you have an except without a try?
    No. and No

- What is the variable `__name__` used for?
    It is used to know if current file is being run directly or imported. Eventually,
    you make sure if the current file is being imported that code in main() is ignored.

    If name not equal to main then skip the testing code
    if __name__ = '__main__':
        # run testing on this file
