try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oop!, that was not a number!")
except KeyboardInterrupt:
    print("Got Ctrl-C, good bye!")
