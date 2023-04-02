import numpy as np
import openai
import pandas as pd
openai.api_key = "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"

def get_embedding(text, model="text-embedding-ada-002"):
   print(text)
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']


df = pd.read_csv('data.csv')
df.dropna()
print(df.iloc[:, 1])
print(type(df.iloc[:, 1][0]))
df['ada_embedding'] = df.iloc[:, 1].apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
df.to_csv('embedded_data.csv', index=False)
