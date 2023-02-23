from __init__ import Auto
import pickle

auto = Auto("tesla", "model s", 2023, 400)

with open("auto.pickle", "wb") as f:
    pickle.dump(auto, f)

print(auto)
