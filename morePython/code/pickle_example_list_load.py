import pickle

f = open('list.pkl', 'rb')

my_numbers = pickle.load(f)

print(my_numbers)

f.close()
