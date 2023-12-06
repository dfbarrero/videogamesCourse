import pickle

list_number = [2, 5, 7, 8]

f = open('list.pickle', 'wb')

pickle.dump(list_number, f)

f.close()
