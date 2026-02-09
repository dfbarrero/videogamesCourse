# The file closes automatically, even if an exception occurs
try:
    with open('data.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")
except PermissionError:
    print("Error: Permission denied")
except IOError as e:
    print("Error: I/O error occurred: {e}")
except Exception as e:
    print(f"Error: {e}")
