try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist")
except PermissionError:
    print("Error: You don't have permission")
except IOError as e:
    print("Error: I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
