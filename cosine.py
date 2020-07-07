import pandas as pd
from pprint import pprint
import numpy as np
import math

def norm(A):

    return math.sqrt(sum([pow(x,2) for x in A]))

def cosine_sim(A,B):

    return (sum([x*y for (x,y) in zip(A,B)])/(norm(A)*norm(B)))

data = pd.read_csv('./dataset.csv',header=None)

b_matrix = d_matrix = np.zeros((len(data),len(data)))

distances = []

for i in range(len(data)):
    row1 = data.iloc[i].to_numpy()
    for j in range(len(data)):
        row2 = data.iloc[j].to_numpy()
        d_matrix[i][j] = ( cosine_sim(row2,row1))
        distances.append(d_matrix[i][j])

pprint(d_matrix)

distances = np.unique(distances)

class_1 = []

for i in range(len(distances)-1):
    s = (distances[i] + distances[i+1])/2
    for j in range(len(d_matrix)):
        for k in range(j):
            if(d_matrix[j][k]<s):
                class_1.append(j)
                class_1.append(k)

    class_1 = np.unique(class_1).tolist()

    if(len(class_1)<len(data) and len(class_1)!=0):
        print("the answer is ",s)
        print(class_1)
        with open('output_cosine.txt','a+') as f:
            for j in range(len(d_matrix)):
                if(j in class_1):
                    f.write("1\n")
                else:
                    f.write("0\n")
            f.write(str(s))
        break
        break
