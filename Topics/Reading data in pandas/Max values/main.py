import pandas as pd

df = pd.read_csv('./data/dataset/input.txt', sep=',')
print(int(df['Age'].max()))
