'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
def sed (pattern, replacement, input_file, output_file):
    output_string = read_file(input_file)
    write_file(output_string.replace(pattern, replacement), output_file)
    # using method replace to replace pattern


def read_file(input_file):
    '''
This function takes string name of the file and store text in string data
Also, here I am trying try!
'''
    try:
        f= open(input_file, 'r')
        data = f.read()
        f.close()
        print(f"Read completed successfully from file '{input_file}'")
        return data
    except IOError:
        print('An error occured trying to read the file.')

    except EOFError:
        print('Why did you do an EOF on me?')

    except KeyboardInterrupt:
        print('You cancelled the operation.')

    except:
        print('An error occured.')




def write_file(output_string, output_file):
    '''
This function takes output string from read_file, try to catch errors
 and store text output file
'''
    try:
        f= open(output_file, 'w')
        f.write(output_string)
        f.close()
        print(f"Write completed successfully to file '{output_file}'")
    except IOError:
        print('An error occured trying to read the file.')

    except EOFError:
        print('Why did you do an EOF on me?')

    except KeyboardInterrupt:
        print('You cancelled the operation.')

    except:
        print('An error occured.')


############## End of code!  below is for resting script only##########
if __name__ == '__main__':
    # Delete output file content just to make sure it's empty, for testing over and over again
    write_file("", "output_file_for_12_02.txt")

    # Call the sed function to replace pattern and write to output file
    sed("Name", "Adwan", "input_file_for_12_02.txt", "output_file_for_12_02.txt")
