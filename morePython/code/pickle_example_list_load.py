import pickle

f = open('list.pickle', 'rb')

list_number = pickle.load(f)

print(list_number)

f.close()
