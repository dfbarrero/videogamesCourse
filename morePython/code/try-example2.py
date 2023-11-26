try:
    f = open('file.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("I/O error: " + err)
except ValueError:
    print("Could not convert data to integer")
except:
    print("Unexpected exception")
    raise
