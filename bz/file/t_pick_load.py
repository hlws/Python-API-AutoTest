import pickle
with open("data.dat","rb") as f:
    resume=pickle.load(f)
    print(resume)