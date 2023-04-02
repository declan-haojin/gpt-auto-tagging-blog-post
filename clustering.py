import numpy as np
import openai
import pandas as pd
openai.api_key = "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"

def get_embedding(text, model="text-embedding-ada-002"):
   print(text)
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']


df = pd.read_csv('data.csv')
# print(df.iloc[:, 1])
# print(type(df.iloc[:, 1][0]))
df['ada_embedding'] = df.iloc[:, 1].apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
df.to_csv('embedded_data.csv', index=False)
