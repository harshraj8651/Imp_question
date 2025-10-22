import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")
print(data,"n")

d = np.array(data)[:,:-1]
print("n The attributes are: ",d)

target = np.array(data)[:,-1]
print("n The target is: ",target)

def train(c,t):

    specific_hypothesis = None
    for i, val in enumerate(t):
        if val == "Yes": 
            specific_hypothesis = c[i].copy()
            break

    if specific_hypothesis is None:
       
        print("No positive examples found in the training data.")
        return None 

    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
    return specific_hypothesis


print("n The final hypothesis is:",train(d,target))