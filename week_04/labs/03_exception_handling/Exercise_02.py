'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

# Read each number and catch errors, if no error then raise to power of 2
if __name__ == '__main__':

    try:
        f = open('integers.txt', 'r')
    except FileNotFoundError as exc:
        exc.message = "File not found!"
        print(exc.message)
    else:
        while (True):
            try:
                char = f.readline()
                if(char == ""):
                    break
                my_int = int(char)
                print(my_int)
            except IOError as exc:
                exc.message = f"Custom IOError error message! {char}"
                print(exc.message)
            except ValueError as exc:
                exc.message = f"Custom ValueError error message! {char}"
                print(exc.message)
    finally:
        f.close()



