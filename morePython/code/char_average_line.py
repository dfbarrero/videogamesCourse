file_ex = open('example.txt', 'r')
num_total_char = 0
count_line= 0

for line in file_ex:
	count_line += 1
	num_total_char += len(line)
file_ex.close()
print('average', float(num_total_char) / float(count_line))