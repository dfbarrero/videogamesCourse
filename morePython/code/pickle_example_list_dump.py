import pickle

numbers = [2, 5, 7, 8]

f = open('list.pkl', 'wb')

pickle.dump(numbers, f)

f.close()
