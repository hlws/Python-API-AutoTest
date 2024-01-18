import pickle
with open("data.dat","wb") as f:
    name="lst"
    age=27
    score=[77,88,99]
    resume={'namen':name,'age':age,'score':score}
    pickle.dump(resume,f)