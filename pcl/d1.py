import pickle

auto = {'mark': 'tesla', 'model': 'model s', 'year': 2023, 'power': 400}

with open('auto_dict.pickle', 'wb') as f:
    f.write(pickle.dumps(auto))
    print(pickle.dumps(auto))
