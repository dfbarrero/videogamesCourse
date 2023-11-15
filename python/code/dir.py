import os

os.system("clear")

path = input("Specify a folder >> ")

for root, dirs, files in os.walk(path):
    print(root)
    print("---------------")
    print(dirs)
    print("---------------")
    print(files)
    print("---------------")
