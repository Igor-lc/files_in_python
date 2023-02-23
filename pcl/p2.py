import pickle

with open("auto.pickle", 'rb') as f:
    auto1 = pickle.load(f)


print(auto1)
