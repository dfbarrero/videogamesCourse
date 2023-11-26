count_line = 0
with open('/Users/julia/code/names.txt') as arch_names:
    for line in arch_names:
        count_line += 1
        print('{:<10}{}'.format(count_line, line.rstrip()))