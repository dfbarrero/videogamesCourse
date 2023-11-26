import json

mylist = ["John", 42, "Smith"]

myfile = open("myfile.json", "w")

json.dump(mylist, myfile, indent = 4)
