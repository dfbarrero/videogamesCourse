# Read mode (default)
file = open('data.txt', 'r')
# or simply:
file = open('data.txt')

# Write mode - overwrites
file = open('output.txt', 'w')

# Append mode - adds to the end
file = open('log.txt', 'a')

# Read and write mode
file = open('data.txt', 'r+')
