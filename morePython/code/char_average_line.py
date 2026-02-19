characters = 0
lines= 0

file = open('example.txt', 'r')

for line in file:
	lines+= 1
	characters += len(line)

file.close()

print(f"Characters: {characters}, number of lines: {lines}")
