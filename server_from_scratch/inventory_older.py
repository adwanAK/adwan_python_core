import json
import sys

class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        fileinfo = self.filereader()
        if method == 'GET':
            if path == '/inventory' or path == '/inventory/':
                inven = json.dumps(fileinfo)
                return inven
            else:
                path_list = path.split('/')
                inven = json.dumps(fileinfo[path_list[2]])
                return inven


        elif method == 'PATCH':
            path_list = path.split("/") #i.e.["", "inventory", "socks"]
            category = path_list[2]
            query_list= query.split('=')# ['amount', '5']
            amount = query_list[1]
            fileinfo[category] = int(fileinfo[category]) + int(amount)
            self.filewriter(fileinfo)
            inven = json.dumps(fileinfo)

            return inven

        elif method == 'DELETE':
            path_list = path.split("/") #/inventory/socksi.e.["", "inventory", "socks"]
            category = path_list[2]

            if query == "": #Then delete the whole category from inventory
                fileinfo.pop(category)
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven


            else: #Subtract amount
                query_list= query.split('=')# ['amount', '5']
                amount = query_list[1]
                query_list = query.split('=') # amount=5 i.e. [amount, 5]
                fileinfo[category] = int(fileinfo[category]) - int(amount)
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven

        elif method =='POST':
            path_list = path.split("/") #i.e.["", "inventory", "socks"]
            category = path_list[2] # = socks
            query_list= query.split('=')# amount=5 i.e. [amount, 5]
            amount = query_list[1]
            if category in fileinfo:
                return "Category exists! You can use method PATCH to edit"
            else:
                fileinfo[category] = amount
                self.filewriter(fileinfo)
                inven = json.dumps(fileinfo)
                return inven

        return "Your request is invalid, please try new URL"


    def filewriter(self, fileinfo):
        json.dump(fileinfo, open("inventory_api.txt", 'w'))
        return "Your inventory has been updated"

    def filereader(self):
        _dict = {}
        with open('inventory_api.txt', 'r') as f:
            _dict = json.loads(f.read())
        return _dict


