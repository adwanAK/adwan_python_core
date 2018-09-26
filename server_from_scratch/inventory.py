import json
import sys

class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        fileinfo = self.filereader()

         #Use special function parse_url (see function docstring end of the page)
        url_dict = self.parse_url(path, query)

        if method == 'GET':
            if 'category' not in url_dict:
                inven = json.dumps(fileinfo)
                return inven
            else:
                print(url_dict['category'])
                print(fileinfo[url_dict['category']])
                inven = json.dumps(fileinfo[url_dict['category']])
                return inven



        elif method == 'PATCH':
            if url_dict['category'] in fileinfo:
                fileinfo[url_dict['category']] = int(fileinfo[\
                    url_dict['category']]) + int(url_dict['amount'])
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven
            else:
                return (f"Category {url_dict['category']} doesn't exit\
                Create using method POST. Or Bad PATCH request.")



        elif method == 'DELETE':
            #If no amount specified, then delete the whole category from inventory
            if url_dict['category'] in fileinfo and 'amount' not in url_dict:
                fileinfo.pop(url_dict['category'])
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven

            elif url_dict['category'] in fileinfo: #If amount specified, then only subtract from inventory
                fileinfo[url_dict['category']] = int(fileinfo[\
                    url_dict['category']]) - int(url_dict['amount'])
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven
            else:
                return f"Bad DELETE!Category does not exist! Use PATCH to add "



        elif method =='POST':
            if url_dict['category'] in fileinfo:
                return "Bad POST! Category exists! Use method PATCH to edit"
            elif 'amount' not in url_dict:
                return f"Bad POST! Specify amount to create i.e. Category?amount=5"
            else:
                fileinfo[url_dict['category']] = url_dict['amount']
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven

        return "Your request is invalid, please try new URL. Remember you can only view /inventory/"



    def filewriter(self, fileinfo):
        json.dump(fileinfo, open("inventory_api.txt", 'w'))
        return "Your inventory has been updated"

    def filereader(self):
        _dict = {}
        with open('inventory_api.txt', 'r') as f:
            _dict = json.loads(f.read())
        return _dict



    def parse_url(self, path, query):
        '''
            Function parses path and query and return new dictionary
            with useful information to execute any http method
        '''
        url_dict = {}
        if path[0] == '/':  # Clean up leading '/'' or trailing '/''
            path = path[1:]
        if path[-1] == '/':
            path = path[:-1]
        path_list = path.split("/") #i.e.[inventory", "socks"]
        url_dict = {path_list[0]: path_list[0]}

        if len(path_list) == 2: # i.e. Add catgory socks in dictionary
            url_dict['category'] = path_list[1]

        elif len(path_list) >2:
            exit()

        if len(query) > 1:
            query_list= query.split('=') # amount=5 i.e. [amount, 5]
            url_dict['amount'] = query_list[1] #Add amount in dictionary
            print(url_dict)

        return url_dict


