'''
Complete Exercise 8.3 (p.95) from the textbook.

'''

# noon is palindram so it should return True
print("noon"[::] == "noon"[::-1])

# hello is not palindram so it should return False
print("hello"[::] == "hello"[::-1])
