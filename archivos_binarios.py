import pickle

Lista = [1,2,3,4,5, ["Juanes"], "Pedro"]

with open("Lista.dat", "wb") as fp:
    pickle.dump(Lista, fp)

with open("Lista.dat", "rb") as fp:
    Lista2 = pickle.load(fp)
    print(Lista2)