#!/usr/local/bin/python3

# --- a minimal web application --- #

people = ['mum', 'dad']

# our minimal HTTP header to clarify what type of content follows
print("Content-type: text/html\n")

# printing a basic HTML structure that allow to display a website
print("<html>")
print("<body>")
# the following two lines underline that code is executed on the server
# and the generated HTML is what is being displayed on the client side
print(f"<h1>Hello {people[0]} & {people[1]}</h1>")
print(f"<p>Sending some &lt;{1+2}</p>")
print("</body>")
print("</html>")
