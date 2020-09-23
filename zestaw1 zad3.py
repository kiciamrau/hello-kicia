import pandas as pd

df = pd.read_csv("train.tsv", delimiter='\t', encoding="utf-8",
                 names=["Cost", "NumR", "Area", "Floor", "Address", "Descr"])
df2 = pd.read_csv("description.csv", delimiter=',', header=0, encoding='utf-8')
# connecting choosen data frame columns
df = pd.merge(df, df2, left_on='Floor', right_on='Liczba', how='left')
with open('out2.csv', 'w', encoding="utf-8") as csvfile:
    df.to_csv(csvfile, header=False, index=False, line_terminator='\n')
