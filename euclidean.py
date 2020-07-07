import pandas as pd
from pprint import pprint
import numpy as np
import math

def norm(A):

    return math.sqrt(sum([pow(x,2) for x in A]))

data = pd.read_csv('./dataset.csv',header=None)

b_matrix = d_matrix = np.zeros((len(data),len(data)))

distances = []

for i in range(len(data)):
    row1 = data.iloc[i].to_numpy()
    for j in range(len(data)):
        row2 = data.iloc[j].to_numpy()
        d_matrix[i][j] = norm(row2-row1)
        distances.append(round(d_matrix[i][j],1))

distances = np.unique(distances)

class_1 = []

for i in range(len(distances)-1):
    d = (distances[i] + distances[i+1])/2
    for j in range(len(d_matrix)):
        for k in range(j):
            if(d_matrix[j][k]<d):
                class_1.append(j)
                class_1.append(k)
    class_1 = np.unique(class_1).tolist()
    if(len(class_1)<len(data) and len(class_1)!=0):
        print("answer is ",d)
        print(class_1)
        print(len(class_1))
        with open('output_euclidean.txt','a+') as f:
            for j in range(len(d_matrix)):
                if(j in class_1):
                    f.write("0\n")
                else:
                    f.write("1\n")
            f.write(str(d))
        break
