characters = 0
lines= 0

file = open('example.txt', 'r')

for line in file:
	characters+= 1
	lines += len(line)

file.close()

print(f"Characters: {characters}, number of lines: {lines}")
