import pandas as pd

df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Cost", "NumR", "Area", "Floor", "Address", "Descr"])
with open('out0.csv', 'w') as csvfile:
    csvfile.write(str(df.cost.mean().round(0)))
