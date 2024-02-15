count_line = 0
with open('nombres.txt') as arch_names:
    for line in arch_names:
        count_line += 1
        print(f'{count_line}: {line.rstrip()}')
