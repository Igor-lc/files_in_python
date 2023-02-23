import pickle

with open("auto_dict.pickle", "rb") as f:
    auto1 = pickle.loads(f.read())


print(auto1)
