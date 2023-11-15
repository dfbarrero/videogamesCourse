import sys

# datos introducidos por teclado
data = sys.argv

print('data =  ', data)

print("{0} arguments were passed to the script {1}: ".format(
    len(sys.argv) - 1, sys.argv[0]))

for arg in sys.argv:
    print(arg)

