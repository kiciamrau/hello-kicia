import pandas as pd

df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Cost", "NumR", "Area", "Floor", "Address", "Descr"])
df['CostOfSquareMeter'] = df.Cost/df.Area
# choosing rows
df2 = df[(df.NumR >= 3) &
         (df.CostOfSquareMeter < df.CostOfSquareMeter.mean())]
# choosing columns
df2 = df2[['NumR', 'Cost', 'CostOfSquareMeter']]
with open('out1.csv', 'w', encoding="utf-8") as csvfile:
    df2.to_csv(csvfile, index=False, line_terminator='\n')
