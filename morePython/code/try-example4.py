file = None
try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File 'data.txt' not found")
except PermissionError:
    print("Error: Permission denied")
except IOError as e:
    print(f"I/O error occurred: {e}")
finally:
    # This always executes, even if there's an error
    if file is not None:
        file.close()
        print("File closed successfully")
