import numpy as np
import openai
from sklearn.metrics.pairwise import cosine_distances
from scipy.spatial.distance import cosine
import csv
import json
import ast

# openai.api_key = "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"

# def get_embedding(text, model="text-embedding-ada-002"):
#    print(text)
#    text = text.replace("\n", " ")
#    return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

# predefined_tags = ["travel", "F1", "Microsoft", "holiday", "festival", "Utah", "Beijing",
#                    "school", "Canada", "Mexico", "flight", "food", "hiking", "algorithm",
#                    "coding", "cooking", "extracurricular", "photography", "movie", "New York City",
#                    "park", "nature", "history", "tech", "project", "sports", "summer", "winter"]
# predefined_tags_embeddings = {value: '' for value in predefined_tags}

# for tag in predefined_tags:
#     predefined_tags_embeddings[tag] = get_embedding(tag, model='text-embedding-ada-002')

# # print(predefined_tags_embeddings)
# json_str = json.dumps(predefined_tags_embeddings)
# print(json_str)
# with open('predefined_tags_embeddings.json', 'w') as f:
#     json.dump(predefined_tags_embeddings, f)

with open('predefined_tags_embeddings.json', 'r') as f:
    predefined_tags_embeddings = json.load(f)

# print(predefined_tags_embeddings)


# Open the CSV file
with open('embedded_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)
    for row in reader:
        [post_title, post_tag, ada_embedding] = row
        # print(title, tag, ada_embedding)
        ada_embedding = ast.literal_eval(ada_embedding)
        # print(np.array(predefined_tags_embeddings['travel']))
        # print(np.array(ada_embedding))
        for tag in predefined_tags_embeddings:
            distance = cosine(np.array(ada_embedding), np.array(predefined_tags_embeddings[tag]))
            if distance < 0.15:
                print(f'{post_title}: {post_tag} distance to {tag} is ***{distance}***')



